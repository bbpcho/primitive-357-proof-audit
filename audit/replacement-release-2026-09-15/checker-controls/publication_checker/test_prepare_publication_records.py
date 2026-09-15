#!/usr/bin/env python3
"""Explicitly synthetic staging controls; these are not live observations."""
from pathlib import Path
import copy, hashlib, json, shutil, subprocess, sys, tempfile, zipfile

N = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(N));sys.path.insert(0, str(N / 'current_binding'))
import prepare_publication_records as prepare
from test_current_distribution import Fixture as CompanionFixture

def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + '\n')

def load(path):return json.loads(path.read_text())
def ident(path):return {'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}

class Fixture:
    def __init__(self, base):
        self.base=base;self.root=base/'overlay';self.inputs=base/'inputs';self.inputs.mkdir()
        self.downloads=base/'downloads';self.downloads.mkdir()
        self.c=CompanionFixture(self.root);self.c.tag=prepare.TAG;self.c.build()
        self.archive=self.inputs/prepare.NAMES['companion'];self.c.archive.rename(self.archive)
        self.c.binding['asset'].update(name=self.archive.name,url=prepare.url(self.archive.name));self.c.write_binding()
        write(self.root/'audit/status.json',dict(self.c.status,release_tag='verified-2026-09-14.1',
              release_asset_id='historical-baseline',fresh_replay={'state':'pass','binding':'historical-only.json'},
              arxiv_submission_ready=False))
        for name,data in {'manuscript.tex':b'\\input{rank-proof}\n', 'rank-proof.tex':b'Rank test data\n',
                          'manuscript.pdf':b'%PDF-1.4\nexplicit synthetic test data\n'}.items():
            path=self.root/'paper'/name;path.parent.mkdir(exist_ok=True);path.write_bytes(data)
        self.source=self.root/'release'/prepare.NAMES['source_zip'];self.source.parent.mkdir()
        self.rebuild_source()
        shutil.copyfile(self.archive,self.downloads/self.archive.name)
        shutil.copyfile(self.root/'paper/manuscript.pdf',self.downloads/prepare.NAMES['paper_pdf'])
        shutil.copyfile(self.source,self.downloads/self.source.name)
        (self.downloads/prepare.NAMES['replay_guide']).write_text('Synthetic guide\n')
        (self.downloads/prepare.NAMES['checksums']).write_text('Synthetic checksum asset\n')
        self.final={'schema':'primitive357_final_archive_identity_v1','status':'PASS_FINAL_APPEND_ONLY_COMPANION',
                    'name':self.archive.name,'release_tag':prepare.TAG,**ident(self.archive)}
        self.paper={'schema':'primitive357_final_paper_build_v1','status':'PASS_PAPER_BUILD_AND_CLEAN_SOURCE_REBUILD','companion':copy.deepcopy(self.final),
                    'paper':{n:ident(self.root/'paper'/n)['sha256'] for n in ('manuscript.tex','rank-proof.tex','manuscript.pdf')},
                    'pdf':{'filename':prepare.NAMES['paper_pdf'],**ident(self.root/'paper/manuscript.pdf')},
                    'source_bundle':{'filename':self.source.name,**ident(self.source)},
                    'source_members':[{'name':n,'sha256':ident(self.root/'paper'/n)['sha256']} for n in ('manuscript.tex','rank-proof.tex')],
                    'clean_source_rebuild':'PASS_BYTE_IDENTICAL_PDF','undefined_references':False,'overfull_boxes':False,
                    'visual_review':'PASS_VISUAL_REVIEW',
                    'arxiv_submitted':False,'submission_holds':['Requested Dahmen reply pending']}
        rows=[{'role':role,'name':name,'url':prepare.url(name),'asset_id':i,'http_status':200,**ident(self.downloads/name)}
              for i,(role,name) in enumerate(prepare.NAMES.items(),201)]
        self.observation={'schema':'primitive357_full_public_download_observation_v1','status':'PASS_PUBLIC_DOWNLOADS_AND_IDENTITIES',
                          'repository':prepare.REPO,'repository_visibility':'public','unauthenticated_request':True,
                          'release_tag':prepare.TAG,'release_id':101,'draft':False,'published_utc':'2026-09-15T18:00:00Z',
                          'checked_utc':'2026-09-15T18:01:00Z','downloads':rows,'tag_commit':'a'*40}
        self.apis={'REPOSITORY_API.json':{'full_name':'bbpcho/primitive-357-proof-audit','private':False},
                   'RELEASE_API.json':{'id':101,'tag_name':prepare.TAG,'draft':False,'published_at':self.observation['published_utc'],
                       'assets':[{'name':r['name'],'id':r['asset_id'],'size':r['bytes'],'state':'uploaded','digest':'sha256:'+r['sha256'],
                                  'browser_download_url':r['url']} for r in rows]},
                   'TAG_REF_API.json':{'ref':'refs/tags/'+prepare.TAG,'object':{'type':'commit','sha':'a'*40}}}
        self.withdrawal={'schema':'primitive357_old_asset_withdrawal_observation_v1','status':'PASS_WITHDRAWN_PUBLIC_ENDPOINTS',
                         'repository':prepare.REPO,'replacement_release_tag':prepare.TAG,'checked_utc':'2026-09-15T18:02:00Z',
                         'unauthenticated_request':True,'assets':[{'asset_id':i,'name':name,'bytes':size,'sha256':sha,
                           'api_url':prepare.API+'/releases/assets/'+str(i),'download_url':prepare.url(name,'audit-2026-09-13.1'),
                           'api_http_status':404,'download_http_status':404} for i,(name,size,sha) in prepare.OLD.items()]}
        self.seal()
    def rebuild_source(self, kind='good'):
        with zipfile.ZipFile(self.source,'w') as z:
            z.writestr('manuscript.tex',b'altered' if kind=='wrong_member' else (self.root/'paper/manuscript.tex').read_bytes())
            if kind!='missing_member':z.writestr('rank-proof.tex',(self.root/'paper/rank-proof.tex').read_bytes())
            if kind=='duplicate':z.writestr('rank-proof.tex',(self.root/'paper/rank-proof.tex').read_bytes())
            if kind=='symlink':
                x=zipfile.ZipInfo('link');x.external_attr=0o120777<<16;z.writestr(x,'manuscript.tex')
    def rehash_source(self, kind):
        self.rebuild_source(kind);shutil.copyfile(self.source,self.downloads/self.source.name)
        self.paper['source_bundle'].update(ident(self.source))
        for row in self.observation['downloads']:
            if row['role']=='source_zip':row.update(ident(self.source))
        for row in self.apis['RELEASE_API.json']['assets']:
            if row['name']==self.source.name:row.update(size=ident(self.source)['bytes'],digest='sha256:'+ident(self.source)['sha256'])
    def seal(self):
        for name,value in self.apis.items():write(self.downloads/name,value)
        self.observation['api_records']={n:ident(self.downloads/n) for n in self.apis}
        for name,value in [('final.json',self.final),('paper.json',self.paper),('observation.json',self.observation),('withdrawal.json',self.withdrawal)]:write(self.inputs/name,value)
    def command(self,mode):
        return [sys.executable,*mode,'-B',str(N/'prepare_publication_records.py'),
                '--repo-overlay',str(self.root),'--download-root',str(self.downloads),'--companion-archive',str(self.archive),
                '--final-identity',str(self.inputs/'final.json'),'--paper-build',str(self.inputs/'paper.json'),
                '--observation',str(self.inputs/'observation.json'),'--withdrawal-record',str(self.inputs/'withdrawal.json'),
                '--binding-path','binding.json','--output',str(self.base/'staged')]

def main():
    cases={
      'valid_five_observations_select_three':(True,lambda f:None),
      'archive_not_final':(False,lambda f:f.final.update(status='RUNNING')),
      'paper_for_other_companion':(False,lambda f:f.paper['companion'].update(sha256='0'*64)),
      'visual_review_pending':(False,lambda f:f.paper.update(visual_review='PENDING')),
      'canonical_tex_changed':(False,lambda f:(f.root/'paper/manuscript.tex').write_text('wrong')),
      'rehashed_wrong_zip_member':(False,lambda f:f.rehash_source('wrong_member')),
      'rehashed_missing_zip_member':(False,lambda f:f.rehash_source('missing_member')),
      'rehashed_duplicate_zip_member':(False,lambda f:f.rehash_source('duplicate')),
      'rehashed_symlink_zip_member':(False,lambda f:f.rehash_source('symlink')),
      'not_public_repository':(False,lambda f:f.observation.update(repository_visibility='private')),
      'authenticated_downloads':(False,lambda f:f.observation.update(unauthenticated_request=False)),
      'missing_fifth_role':(False,lambda f:f.observation['downloads'].pop()),
      'duplicate_download_role':(False,lambda f:f.observation['downloads'].append(copy.deepcopy(f.observation['downloads'][0]))),
      'failed_download':(False,lambda f:f.observation['downloads'][0].update(http_status=404)),
      'bool_release_id':(False,lambda f:f.observation.update(release_id=True)),
      'wrong_release_id':(False,lambda f:f.observation.update(release_id=102)),
      'wrong_download_asset_id':(False,lambda f:f.observation['downloads'][0].update(asset_id=998)),
      'duplicate_api_asset_id':(False,lambda f:f.apis['RELEASE_API.json']['assets'][1].update(id=201)),
      'wrong_api_digest':(False,lambda f:f.apis['RELEASE_API.json']['assets'][0].update(digest='sha256:'+'0'*64)),
      'wrong_tag_commit':(False,lambda f:f.apis['TAG_REF_API.json']['object'].update(sha='b'*40)),
      'wrong_tag_ref':(False,lambda f:f.apis['TAG_REF_API.json'].update(ref='refs/tags/wrong')),
      'draft_api':(False,lambda f:f.apis['RELEASE_API.json'].update(draft=True)),
      'download_precedes_publication':(False,lambda f:f.observation.update(checked_utc='2026-09-15T17:00:00Z')),
      'naive_timestamp':(False,lambda f:f.observation.update(checked_utc='2026-09-15T18:01:00')),
      'missing_withdrawal':(False,lambda f:f.withdrawal['assets'].pop()),
      'withdrawal_api_still_public':(False,lambda f:f.withdrawal['assets'][0].update(api_http_status=200)),
      'withdrawal_download_still_public':(False,lambda f:f.withdrawal['assets'][0].update(download_http_status=200)),
      'wrong_withdrawn_hash':(False,lambda f:f.withdrawal['assets'][0].update(sha256='0'*64)),
      'wrong_withdrawal_endpoint':(False,lambda f:f.withdrawal['assets'][0].update(download_url=prepare.url('unrelated.zip'))),
      'withdrawal_before_new_publication':(False,lambda f:f.withdrawal.update(checked_utc='2026-09-15T17:00:00Z')),
      'withdrawal_before_download_checks':(False,lambda f:f.withdrawal.update(checked_utc='2026-09-15T18:00:30Z')),
      'withdrawal_example_rejected':(False,lambda f:f.withdrawal.update(_example_only=True)),
      'arxiv_submission_claim':(False,lambda f:f.paper.update(arxiv_submitted=True)),
      'missing_dahmen_hold':(False,lambda f:f.paper.update(submission_holds=[])),
      'duplicate_json_key':(False,lambda f:None),
      'missing_downloaded_bytes':(False,lambda f:None),
      'changed_api_record_bytes':(False,lambda f:None),
      'symlink_downloaded_file':(False,lambda f:None),
      'overlay_arxiv_ready_claim':(False,lambda f:None),
      'existing_output_refused':(False,lambda f:None),
    }
    output=[]
    with tempfile.TemporaryDirectory(prefix='publication-preparation-tests-') as temp:
        for mode in ([],['-O']):
            for name,(accepted,edit) in cases.items():
                base=Path(temp).resolve()/(('normal-' if not mode else 'optimized-')+name);base.mkdir()
                f=Fixture(base);edit(f);f.seal()
                if name=='duplicate_json_key':
                    p=f.inputs/'observation.json';p.write_text(p.read_text().replace('"draft": false,','"draft": false, "draft": false,'))
                if name=='missing_downloaded_bytes':(f.downloads/prepare.NAMES['replay_guide']).unlink()
                if name=='changed_api_record_bytes':(f.downloads/'REPOSITORY_API.json').write_text('{}')
                if name=='symlink_downloaded_file':
                    p=f.downloads/prepare.NAMES['paper_pdf'];p.unlink();p.symlink_to(f.root/'paper/manuscript.pdf')
                if name=='overlay_arxiv_ready_claim':write(f.root/'audit/status.json',{'github_repository':prepare.REPO,'arxiv_submission_ready':True})
                if name=='existing_output_refused':(base/'staged').mkdir()
                before={p.relative_to(f.root).as_posix():ident(p) for p in f.root.rglob('*') if p.is_file()}
                done=subprocess.run(f.command(mode),capture_output=True,text=True)
                passed=(done.returncode==0)==accepted
                after={p.relative_to(f.root).as_posix():ident(p) for p in f.root.rglob('*') if p.is_file()}
                passed=passed and before==after
                if not accepted and name!='existing_output_refused':passed=passed and not (base/'staged').exists()
                if accepted and done.returncode==0:
                    result=load(base/'staged/PUBLICATION_RECORD_PREPARATION.json')
                    pub=load(base/'staged'/prepare.BASE/'PUBLICATION.json')
                    status=load(base/'staged/PROSPECTIVE_STATUS.json')
                    passed=passed and len(pub['assets'])==3 and {r['role'] for r in pub['assets']}==set(prepare.CORE)
                    passed=passed and result['publication_check']['status']=='PASS_CURRENT_PUBLICATION_OFFLINE_BINDING' and status['arxiv_submission_ready'] is False
                    passed=passed and status['release_tag']=='verified-2026-09-14.1' and status['fresh_replay']=={'state':'pass','binding':'historical-only.json'}
                output.append({'case':name,'python_mode':'normal' if not mode else '-O','expected_success':accepted,'exit_code':done.returncode,'passed':passed,
                               'diagnostic':done.stderr.strip().splitlines()[-1] if done.stderr.strip() else ''})
                if not passed:print(done.stdout,done.stderr);raise SystemExit('Control failed: '+name)
    result={'status':'PASS_SYNTHETIC_PUBLICATION_STAGING_CONTROLS','synthetic_fixtures_not_live_observations':True,'cases':len(output),'results':output}
    write(N/'publication_checker/PREPARATION_TEST_RESULTS.json',result)
    print(json.dumps({'status':result['status'],'cases':len(output)},indent=2))

if __name__=='__main__':main()
