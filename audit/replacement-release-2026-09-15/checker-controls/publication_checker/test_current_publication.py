#!/usr/bin/env python3
"""Synthetic publication controls joined to the real companion-checker fixture."""
import copy,hashlib,json,sys,tempfile,unittest,zipfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'current_binding'))
from test_current_distribution import Fixture as CompanionFixture
from verify_current_publication import verify_current_publication

def encoded(x):return (json.dumps(x,indent=2)+'\n').encode()
def sha(b):return hashlib.sha256(b).hexdigest()
def row(path,b):return {'path':path,'bytes':len(b),'sha256':sha(b)}

class Fixture:
    def __init__(self,root):
        self.c=CompanionFixture(root);self.c.build();self.root=Path(root);self.status=self.c.status
        payloads={'manuscript.tex':b'\\input{rank-proof}\n','rank-proof.tex':b'Rank appendix\n','manuscript.pdf':b'%PDF-1.4\nsynthetic fixture\n'}
        paper={}
        for name,b in payloads.items():
            p=self.root/'paper'/name;p.parent.mkdir(exist_ok=True);p.write_bytes(b);paper[name]=row('paper/'+name,b)
        self.source=self.root/'release/source.zip';self.source.parent.mkdir()
        with zipfile.ZipFile(self.source,'w') as z:
            for name in ('manuscript.tex','rank-proof.tex'):z.writestr(name,payloads[name])
        source_row=row('release/source.zip',self.source.read_bytes())
        tag=self.c.tag;repo=self.c.repo
        assets={'paper_pdf':{'name':'paper.pdf',**{k:paper['manuscript.pdf'][k] for k in ('bytes','sha256')}},'source_zip':{'name':'source.zip',**{k:source_row[k] for k in ('bytes','sha256')}},'companion':copy.deepcopy(self.c.binding['asset'])}
        for x in assets.values():x['url']=repo+'/releases/download/'+tag+'/'+x['name']
        self.revision={'schema':'primitive357_current_paper_revision_v1','release_tag':tag,'companion_binding':self.status['current_distribution']['binding'],'paper_files':paper,'source_bundle':{'archive':source_row,'members':[dict(row(name,payloads[name]),repository_path='paper/'+name) for name in sorted(('manuscript.tex','rank-proof.tex'))]},'assets':assets,'submission':{'arxiv_submission_made':False,'arxiv_submission_ready':False,'dahmen_reply_pending':True,'holds':['Requested Dahmen reply pending']}}
        self.publication={'schema':'primitive357_current_publication_v1','repository':repo,'release_tag':tag,'release_id':101,'draft':False,'paper_revision_sha256':'','arxiv_submission_made':False,'published_utc':'2026-09-15T16:00:00+00:00','assets':[dict(x,role=k,asset_id=i) for i,(k,x) in enumerate(assets.items(),201)]}
        self.access={'schema':'primitive357_current_public_access_v1','repository':repo,'release_tag':tag,'release_id':101,'draft':False,'checked_utc':'2026-09-15T16:01:00+00:00','unauthenticated_request':True,'repository_visibility':'public','downloads':[dict(x,role=k,http_status=200,asset_id=i) for i,(k,x) in enumerate(assets.items(),201)]}
        self.status.update(arxiv_submission_ready=False,arxiv_submission_holds=['Requested Dahmen reply pending'])
        self.seal()
    def seal(self):
        rbytes=encoded(self.revision);self.publication['paper_revision_sha256']=sha(rbytes)
        current={'state':'published'}
        for role,name,data in [('paper_revision','PAPER_REVISION.json',rbytes),('publication','PUBLICATION.json',encoded(self.publication)),('public_access','PUBLIC_ACCESS_CHECK.json',encoded(self.access))]:
            p='audit/new/'+name;path=self.root/p;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(data);current[role]=row(p,data)
        self.status['current_publication']=current
        self.status.update(current_paper_revision=current['paper_revision']['path'],current_paper_publication=current['publication']['path'],public_access_check=current['public_access']['path'])
    def verify(self):return verify_current_publication(self.root,self.status,self.c.archive)

class Tests(unittest.TestCase):
    def setUp(self):self.tmp=tempfile.TemporaryDirectory();self.f=Fixture(Path(self.tmp.name).resolve()/'R')
    def tearDown(self):self.tmp.cleanup()
    def reject(self,edit):
        edit(self.f);self.f.seal()
        with self.assertRaises((ValueError,KeyError,TypeError,zipfile.BadZipFile)):self.f.verify()
    def test_complete_publication_binding(self):
        result=self.f.verify();self.assertEqual(result['status'],'PASS_CURRENT_PUBLICATION_OFFLINE_BINDING');self.assertFalse(result['arxiv_submission_ready']);self.assertFalse(result['network_requests_made']);self.assertTrue(result['companion_archive_bytes_checked'])
    def test_record_binding_without_local_large_companion(self):
        result=verify_current_publication(self.f.root,self.f.status);self.assertFalse(result['companion_archive_bytes_checked'])
    def test_ready_never_means_submitted(self):
        self.f.revision['submission'].update(dahmen_reply_pending=False,arxiv_submission_ready=True,holds=[])
        self.f.status.update(arxiv_submission_ready=True,arxiv_submission_holds=[]);self.f.seal()
        result=self.f.verify();self.assertTrue(result['arxiv_submission_ready']);self.assertFalse(result['arxiv_submission_made'])
    def test_changed_paper(self):self.reject(lambda f:(f.root/'paper/manuscript.pdf').write_bytes(b'changed'))
    def test_changed_tex(self):self.reject(lambda f:(f.root/'paper/rank-proof.tex').write_text('changed'))
    def test_changed_source_zip(self):self.reject(lambda f:f.source.write_bytes(b'changed'))
    def test_rehashed_wrong_source_member(self):
        def edit(f):
            with zipfile.ZipFile(f.source,'w') as z:z.writestr('manuscript.tex',b'changed');z.writestr('rank-proof.tex',b'Rank appendix\n')
            f.revision['source_bundle']['archive']=row('release/source.zip',f.source.read_bytes())
        self.reject(edit)
    def test_source_zip_omits_rank(self):self.reject(lambda f:f.revision['source_bundle']['members'].pop())
    def test_companion_wrong_tag(self):self.reject(lambda f:f.revision.__setitem__('release_tag','different-tag'))
    def test_companion_wrong_binding(self):self.reject(lambda f:f.revision['companion_binding'].__setitem__('sha256','0'*64))
    def test_download_hash_mismatch(self):self.reject(lambda f:f.access['downloads'][0].__setitem__('sha256','0'*64))
    def test_download_wrong_tag_url(self):self.reject(lambda f:f.access['downloads'][0].__setitem__('url','https://github.com/bbpcho/primitive-357-proof-audit/releases/download/wrong/paper.pdf'))
    def test_missing_download(self):self.reject(lambda f:f.access['downloads'].pop())
    def test_failed_download(self):self.reject(lambda f:f.access['downloads'][0].__setitem__('http_status',404))
    def test_authenticated_not_public_evidence(self):self.reject(lambda f:f.access.__setitem__('unauthenticated_request',False))
    def test_private_repository(self):self.reject(lambda f:f.access.__setitem__('repository_visibility','private'))
    def test_draft_release(self):self.reject(lambda f:f.publication.__setitem__('draft',True))
    def test_missing_release_id(self):self.reject(lambda f:f.publication.pop('release_id'))
    def test_bool_release_id(self):self.reject(lambda f:f.publication.__setitem__('release_id',True))
    def test_asset_id_download_mismatch(self):self.reject(lambda f:f.access['downloads'][0].__setitem__('asset_id',999))
    def test_missing_asset_id(self):self.reject(lambda f:f.publication['assets'][0].pop('asset_id'))
    def test_false_ready_dahmen_pending(self):
        def edit(f):f.status['arxiv_submission_ready']=True;f.revision['submission']['arxiv_submission_ready']=True
        self.reject(edit)
    def test_hidden_dahmen_hold(self):
        def edit(f):f.status['arxiv_submission_holds']=[];f.revision['submission']['holds']=[]
        self.reject(edit)
    def test_status_gate_disagreement(self):self.reject(lambda f:f.status.__setitem__('arxiv_submission_ready',True))
    def test_arxiv_submission_claim_rejected(self):self.reject(lambda f:f.publication.__setitem__('arxiv_submission_made',True))
    def test_source_zip_symlink(self):
        def edit(f):old=f.source.with_suffix('.real');f.source.rename(old);f.source.symlink_to(old)
        self.reject(edit)
    def test_pending_is_not_pass(self):
        self.f.status['current_publication']={'state':'pending'};self.assertEqual(self.f.verify()['status'],'CURRENT_PUBLICATION_NOT_VERIFIED')
    def test_pending_cannot_be_ready(self):
        self.f.status['current_publication']={'state':'pending'};self.f.status['arxiv_submission_ready']=True
        with self.assertRaises(ValueError):self.f.verify()
    def test_legacy_unbound_is_not_pass(self):
        del self.f.status['current_publication'];self.assertEqual(self.f.verify()['status'],'CURRENT_PUBLICATION_NOT_VERIFIED')

if __name__=='__main__':unittest.main(verbosity=2)
