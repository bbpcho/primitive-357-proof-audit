#!/usr/bin/env python3
"""Check current paper/archive and recorded public-download bindings offline.

Requires verify_current_distribution.py beside this module or on PYTHONPATH.
No network request, mathematical replay, peer review or arXiv submission occurs.
"""
from pathlib import Path
import argparse,io,json,stat,zipfile
from urllib.parse import quote

def verify_current_publication(root,status,companion_archive=None):
    from verify_current_distribution import (need,read_bound,parse,identity,rel,
        indexed,sha,timestamp,verify_current_distribution)
    root=Path(root)
    for key in ('arxiv_submitted','arxiv_submission_made'):
        need(key not in status or status[key] is False,'This check does not accept an arXiv submission claim')
    current=status.get('current_publication')
    if current is None or current.get('state')=='pending':
        need(status.get('arxiv_submission_ready') is False,'Pending publication cannot claim submission readiness')
        return {'status':'CURRENT_PUBLICATION_NOT_VERIFIED','state':'unbound' if current is None else 'pending',
                'arxiv_submission_made':False,'network_requests_made':False}
    need(current.get('state')=='published','Unknown publication state')
    roles=('paper_revision','publication','public_access')
    need(set(current)=={'state',*roles},'Publication binding roles')
    raw={key:read_bound(root,current[key]) for key in roles}
    revision,publication,access=(parse(raw[key]) for key in roles)
    for key,role in [('current_paper_revision','paper_revision'),('current_paper_publication','publication'),('public_access_check','public_access')]:
        need(status.get(key)==current[role]['path'],'Current paper/publication pointer mismatch: '+key)
    need(revision.get('schema')=='primitive357_current_paper_revision_v1','Paper revision schema')
    need(publication.get('schema')=='primitive357_current_publication_v1','Publication schema')
    need(access.get('schema')=='primitive357_current_public_access_v1','Public-access schema')
    companion_check=verify_current_distribution(root,status,companion_archive)
    need(companion_check['status'] in ('PASS_CURRENT_DISTRIBUTION_RECORD_BINDING','PASS_CURRENT_DISTRIBUTION_ARCHIVE_AND_RECORD_BINDING'),'Current companion has no completed binding')
    need(revision['companion_binding']==status['current_distribution']['binding'],'Paper identifies a different companion binding')
    binding=parse(read_bound(root,revision['companion_binding']))
    tag=binding['release_tag'];repo=status['github_repository'].rstrip('/')
    need(revision['release_tag']==publication['release_tag']==access['release_tag']==tag,'Paper/publication/companion tag mismatch')
    need(publication['repository']==access['repository']==repo,'Publication repository mismatch')
    need(type(publication['release_id']) is int and publication['release_id']>0 and type(access['release_id']) is int and access['release_id']==publication['release_id'],'Published release ID binding')
    need(publication['draft'] is False and access['draft'] is False,'Draft release is not public publication')
    need(publication['paper_revision_sha256']==sha(raw['paper_revision']),'Published paper revision identity mismatch')
    need(publication['arxiv_submission_made'] is False,'Publication claims arXiv submission')
    submission=revision['submission']
    need(submission['arxiv_submission_made'] is False,'Paper revision claims arXiv submission')
    need(type(submission['arxiv_submission_ready']) is bool and type(submission['dahmen_reply_pending']) is bool,'Submission gate types')
    holds=submission['holds'];need(isinstance(holds,list) and all(isinstance(x,str) and x.strip() for x in holds),'Submission holds')
    need(status.get('arxiv_submission_ready') is submission['arxiv_submission_ready'] and status.get('arxiv_submission_holds')==holds,'Status and paper submission gates disagree')
    if submission['dahmen_reply_pending']:
        need(not submission['arxiv_submission_ready'] and any('dahmen' in x.lower() for x in holds),'Pending Dahmen reply must remain a submission hold')
    if submission['arxiv_submission_ready']:
        need(not submission['dahmen_reply_pending'] and not holds,'Submission readiness asserted with unresolved holds')

    paper=revision['paper_files']
    required={'manuscript.tex','rank-proof.tex','manuscript.pdf'}
    need(set(paper)==required,'Canonical paper file coverage')
    for name,row in paper.items():
        need(row['path']=='paper/'+name,'Wrong canonical paper path')
        read_bound(root,row)
    bundle=revision['source_bundle'];archive_row=bundle['archive']
    archive_bytes=read_bound(root,archive_row)
    members=indexed(bundle['members'],ordered=True)
    need({'paper/manuscript.tex','paper/rank-proof.tex'}<={r['repository_path'] for r in members.values()},'Source ZIP omits canonical TeX')
    need(len({r['repository_path'] for r in members.values()})==len(members),'Duplicate source mapping')
    for row in members.values():
        read_bound(root,dict(row,path=rel(row['repository_path'])))
    with zipfile.ZipFile(io.BytesIO(archive_bytes)) as z:
        items=z.infolist();names=[x.filename for x in items]
        need(len(names)==len(set(names)) and set(names)==set(members),'Source ZIP exact member coverage')
        for item in items:
            row=members[item.filename]
            need(not item.is_dir() and stat.S_IFMT(item.external_attr>>16) in (0,stat.S_IFREG),'Source ZIP contains link or special member')
            need(item.file_size==row['bytes'] and sha(z.read(item))==row['sha256'],'Source ZIP member identity mismatch')

    assets=revision['assets'];asset_roles={'paper_pdf','source_zip','companion'}
    need(set(assets)==asset_roles,'Paper asset roles')
    need(identity(assets['paper_pdf'])==identity(paper['manuscript.pdf']),'PDF asset differs from canonical paper')
    need(identity(assets['source_zip'])==identity(archive_row),'Source asset differs from checked ZIP')
    need(assets['companion']==binding['asset'],'Companion asset differs from current binding')
    expected={}
    for role,row in assets.items():
        identity(row);name=rel(row['name']);need('/' not in name,'Asset name must be a filename')
        url=repo+'/releases/download/'+quote(tag,safe='')+'/'+quote(name,safe='')
        need(row['url']==url,'Wrong asset URL/tag/name')
        expected[role]={k:row[k] for k in ('name','bytes','sha256','url')}
    need(len({r['name'] for r in expected.values()})==3,'Duplicate asset name')
    published=indexed(publication['assets'],'role')
    downloads=indexed(access['downloads'],'role')
    need(set(published)==set(downloads)==asset_roles,'Incomplete published/downloaded asset roles')
    asset_ids=[]
    for role,wanted in expected.items():
        need({k:published[role][k] for k in wanted}==wanted,'Published asset identity mismatch: '+role)
        need({k:downloads[role][k] for k in wanted}==wanted,'Downloaded asset identity mismatch: '+role)
        need(type(downloads[role]['http_status']) is int and downloads[role]['http_status']==200,'Asset download was not successful')
        asset_id=published[role]['asset_id']
        need(type(asset_id) is int and asset_id>0 and type(downloads[role]['asset_id']) is int and downloads[role]['asset_id']==asset_id,'Published/downloaded asset ID binding')
        asset_ids.append(asset_id)
    need(len(set(asset_ids))==3,'Duplicate published asset ID')
    need(access['unauthenticated_request'] is True and access['repository_visibility']=='public','Download evidence is not unauthenticated public access')
    need(timestamp(publication['published_utc'])<=timestamp(access['checked_utc']),'Download record precedes publication')
    return {'status':'PASS_CURRENT_PUBLICATION_OFFLINE_BINDING','release_tag':tag,'paper_files':3,
            'source_zip_members':len(members),'public_assets':3,'arxiv_submission_made':False,
            'arxiv_submission_ready':submission['arxiv_submission_ready'],
            'submission_holds':holds,'network_requests_made':False,
            'companion_archive_bytes_checked':companion_check['archive_payloads_checked'],
            'boundary':'Authenticates actual local paper/source ZIP and saved publication/download records. Public access was observed at the recorded time; this checker makes no network request, mathematical replay, peer-review or arXiv-submission claim.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--status',default='audit/status.json');p.add_argument('--companion-archive',type=Path)
    a=p.parse_args()
    from verify_current_distribution import parse,rel
    status=parse((a.root/rel(a.status)).read_bytes())
    print(json.dumps(verify_current_publication(a.root,status,a.companion_archive),indent=2))
if __name__=='__main__':main()
