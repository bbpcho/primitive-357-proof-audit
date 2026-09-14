#!/usr/bin/env python3
"""Synthetic promotion/join controls; never certify or promote the actual proof."""
import argparse,hashlib,json,os,shutil,subprocess,sys,tempfile,zipfile
from pathlib import Path
import test_verifiers as fixtures
import promote_release as promote
HERE=Path(__file__).resolve().parent

def put(p,obj):
 p.parent.mkdir(parents=True,exist_ok=True)
 p.write_bytes(promote.dump(obj) if isinstance(obj,(dict,list)) else obj)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def state(root):return {str(p.relative_to(root)):digest(p) for p in root.rglob('*') if p.is_file()}
def rows(root):
 return [{'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':digest(p)} for p in sorted(root.rglob('*')) if p.is_file() and p.name!='RELEASE_MANIFEST.json']
def seal(root,manifest,archive):
 value={'schema':'primitive357_verified_release_manifest_v1','release_tag':promote.TAG,'files':rows(root)}
 put(manifest,value);put(root/'RELEASE_MANIFEST.json',value)
 with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
  for p in sorted(root.rglob('*')):
   if p.is_file():z.write(p,'payload/'+p.relative_to(root).as_posix())
def inputs(base):
 root=base/'control';flat=base/'flat';workspace=base/'workspace';fixtures.fixture(root,flat,workspace)
 for name in ('test_verifiers.py','promote_release.py','test_promotion.py','select_final_artifacts.py'):
  shutil.copy2(HERE/name,root/'scripts'/name)
 hist=[]
 for i,key in enumerate(sorted(promote.HISTORICAL)):
  hist.append({'id':key,'filename':'old'+str(i)+'.zip','sha256':hashlib.sha256(('old'+str(i)).encode()).hexdigest(),'bytes':4,'source_path_from_workspace':'old'+str(i)+'.zip','role':'synthetic historical fixture'})
 fixtures.refresh_assets(root,hist)
 payload=base/'payload';pdf=workspace/'separate.pdf';put(pdf,b'%PDF-1.7\nsynthetic fixture only\n')
 put(payload/'paper/manuscript.pdf',pdf.read_bytes());put(root/'paper/manuscript.pdf',pdf.read_bytes())
 for name in ('paper/manuscript.tex','paper/rank-proof.tex'):put(payload/name,(root/name).read_bytes())
 fixtures.manifest(root)
 contract={'required_job_ids_by_group':{k:[k+'_job'] for k in promote.verifier.PRIOR_GROUPS}}
 put(payload/'audit/work/integration_prior/REQUIRED_PRIOR_EVIDENCE.json',contract)
 put(payload/'scripts/verify_release.py',b'# synthetic source; never executed\n')
 tested=base/'tested.json';candidate=workspace/'candidate.zip';seal(payload,tested,candidate)
 tested_value=json.loads(tested.read_text());replay=base/'replay';components=[]
 def joblog(prefix,name,key='sha256'):
  rel='logs/'+name+'.log';p=replay/prefix/rel;put(p,('SYNTHETIC PASS '+name+'\n').encode())
  return {'log':rel,key:digest(p)}
 for name,marker in [('prior','PASS_SELECTED_PRIOR_GROUPS'),('rank_local','PASS_FRESH_RANK_LOCAL_COMPONENT'),('sectors','PASS_FRESH_TEN_SECTORS_AND_INTERFACES')]:
  log=replay/'logs'/(name+'.log');put(log,(marker+'\n').encode());components.append({'id':name,'exit_code':0,'log':'logs/'+name+'.log','sha256':digest(log)})
 conclusions={'equals_B_plus_literal_c':True}
 result={'schema':'primitive357_integrated_replay_v1','status':'PASS_FRESH_INTEGRATED_REPLAY','input_manifest':{'files':len(tested_value['files']),'manifest_sha256':digest(tested)},'components':components,'prior_groups':promote.verifier.PRIOR_GROUPS,'rank_conclusions':conclusions,'retained_premises':['synthetic fixture premise']}
 put(replay/'REPLAY_RESULT.json',result)
 prior={'status':'PASS_SELECTED_PRIOR_GROUPS','groups':promote.verifier.PRIOR_GROUPS,'required_full_prior_job_count':7,'fresh_replay':True,'all_required_prior_jobs_passed':True,'records':[dict(id=k+'_job',exit_code=0,success=True,**joblog('prior',k+'_job','log_sha256')) for k in promote.verifier.PRIOR_GROUPS]}
 put(replay/'prior/PRIOR_REPLAY_RESULT.json',prior)
 put(replay/'sectors/SECTOR_REPLAY_RESULT.json',{'status':'PASS_FRESH_TEN_SECTORS_AND_INTERFACES','records':[dict(id=k,exit_code=0,**joblog('sectors',k)) for k in promote.SECTOR_IDS]})
 put(replay/'rank_local/rank_local_results.json',{'status':'PASS_FRESH_RANK_LOCAL_COMPONENT','conclusions':conclusions,'fresh_checks':[dict(name='rank_fixture',returncode=0,**joblog('rank_local','rank_fixture','log_sha256'))]})
 put(replay/'RUNTIME_VERSIONS.json',{k:'synthetic runtime fixture' for k in ('ordinary_python','sage','pari_gp','pdf_text_extractor')})
 put(replay/'prior/generated_math.bin',b'\x7fELFsynthetic mathematical object; retained by explicit extension\n')
 driver=base/'driver.log';put(driver,b'PASS_FRESH_INTEGRATED_REPLAY\n')
 host=base/'host.json';put(host,{'host':'synthetic fixture'})
 selection=promote.artifact_selector.select_final_artifacts(replay,payload)
 dest=payload/'verification'
 for row in selection['files']:put(dest/row['path'],(replay/row['path']).read_bytes())
 put(dest/'ARTIFACT_SELECTION.json',selection);put(dest/'TESTED_RELEASE_MANIFEST.json',tested.read_bytes())
 put(dest/'PROOF_INPUTS_SHA256.json',{'schema':'primitive357_proof_inputs_v1','release_tag':promote.TAG,'files':[{k:r[k] for k in ('path','sha256','bytes')} for r in tested_value['files']]})
 put(dest/'INTEGRATED_REPLAY.log',driver.read_bytes());put(dest/'HOST_ENVIRONMENT.json',host.read_bytes())
 put(dest/'ASSET_CONSTRUCTION.json',{'schema':'primitive357_verified_asset_construction_v1','release_tag':promote.TAG,'tested_manifest':result['input_manifest'],'tested_candidate_archive':{'bytes':candidate.stat().st_size,'sha256':digest(candidate)},'scope':result['retained_premises']})
 put(dest/'tools/select_final_artifacts.py',(HERE/'select_final_artifacts.py').read_bytes())
 put(dest/'tools/append_verification_records.py',b'# synthetic assembly fixture; never executed\n')
 put(dest/'README.md',b'Synthetic test records, not mathematical evidence.\n')
 final=base/'final.json';archive=workspace/promote.ARCHIVE_NAME;seal(payload,final,archive)
 return {'control-root':root,'final-replay':replay,'tested-manifest':tested,'final-archive':archive,'final-manifest':final,'paper-pdf':pdf,'workspace-root':workspace,'candidate-archive':candidate,'driver-log':driver,'host-record':host},payload,hist

def main():
 p=argparse.ArgumentParser();p.add_argument('--output-dir',type=Path,required=True);a=p.parse_args();records=[]
 cases=['dry','apply','bad_replay','stale_prior','missing_prior_job','missing_hecke_sector','missing_fano_sector','changed_pdf','control_paper_mismatch','extra_zip_member','symlink_control','unsynced_checker','candidate_only_zip','omitted_fano_log','substituted_fano_log','omitted_runtime','substituted_runtime','omitted_math_binary','forged_selection_omission','substituted_driver','substituted_host','substituted_selector','changed_candidate_identity','unknown_native_output','unknown_symlink_output']
 for case in cases:
  for mode in ([],['-O'],['-OO']):
   with tempfile.TemporaryDirectory(prefix='primitive357-promotion-test-') as td:
    args,payload,hist=inputs(Path(td));root=args['control-root'];replay=args['final-replay'];archive=args['final-archive'];dest=payload/'verification'
    def mutate(p,fn):d=json.loads(p.read_text());fn(d);put(p,d)
    if case=='bad_replay':mutate(replay/'REPLAY_RESULT.json',lambda d:d.update(status='FAIL'))
    if case=='stale_prior':mutate(replay/'prior/PRIOR_REPLAY_RESULT.json',lambda d:d.update(fresh_replay=False))
    if case=='missing_prior_job':mutate(replay/'prior/PRIOR_REPLAY_RESULT.json',lambda d:d['records'].pop())
    if case in ('missing_hecke_sector','missing_fano_sector'):
     missing='independent_hecke_input_foundations' if case=='missing_hecke_sector' else 'independent_fano_resolvent_foundation'
     mutate(replay/'sectors/SECTOR_REPLAY_RESULT.json',lambda d:d.update(records=[r for r in d['records'] if r['id']!=missing]))
    if case=='changed_pdf':put(args['paper-pdf'],b'%PDF-1.7\nchanged\n')
    if case=='control_paper_mismatch':put(root/'paper/manuscript.tex',b'different paper\n')
    if case=='extra_zip_member':
     with zipfile.ZipFile(archive,'a') as z:z.writestr('payload/untracked.txt','x')
    if case=='symlink_control':(root/'linked').symlink_to(args['workspace-root'],target_is_directory=True)
    if case=='unsynced_checker':put(root/'scripts/verify_assets.py',b'print("wrong")\n')
    reseal=False
    if case=='candidate_only_zip':shutil.rmtree(dest);reseal=True
    for label,name in [('fano_log','sectors/logs/independent_fano_resolvent_foundation.log'),('runtime','RUNTIME_VERSIONS.json'),('math_binary','prior/generated_math.bin')]:
     if case=='omitted_'+label:(dest/name).unlink();reseal=True
     if case=='substituted_'+label:put(dest/name,b'SUBSTITUTED SYNTHETIC RECORD\n');reseal=True
    if case=='forged_selection_omission':
     name='prior/generated_math.bin';(dest/name).unlink()
     def omit(d):
      removed=next(r for r in d['files'] if r['path']==name);d['files']=[r for r in d['files'] if r['path']!=name];d['selected_file_count']-=1;d['selected_bytes']-=removed['bytes']
     mutate(dest/'ARTIFACT_SELECTION.json',omit);reseal=True
    if case=='substituted_driver':put(dest/'INTEGRATED_REPLAY.log',b'different run\nPASS_FRESH_INTEGRATED_REPLAY\n');reseal=True
    if case=='substituted_host':put(dest/'HOST_ENVIRONMENT.json',{'host':'different fixture'});reseal=True
    if case=='substituted_selector':put(dest/'tools/select_final_artifacts.py',b'# different selector\n');reseal=True
    if case=='changed_candidate_identity':
     mutate(dest/'ASSET_CONSTRUCTION.json',lambda d:d['tested_candidate_archive'].update(sha256='0'*64));reseal=True
    if case=='unknown_native_output':put(replay/'unclassified-tool',b'\x7fELFunknown synthetic native\n')
    if case=='unknown_symlink_output':(replay/'unknown-link').symlink_to(args['workspace-root'],target_is_directory=True)
    if reseal:seal(payload,args['final-manifest'],archive)
    before=state(root);cmd=[sys.executable,'-B',*mode,str(HERE/'promote_release.py')]
    for flag,value in args.items():cmd+=['--'+flag,str(value)]
    if case=='apply':cmd+=['--apply']
    done=subprocess.run(cmd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
    expected=case in ('dry','apply')
    if (done.returncode==0)!=expected:raise RuntimeError(case+' '+repr(mode)+'\n'+done.stdout)
    if case!='apply' and state(root)!=before:raise RuntimeError('control changed in '+case)
    if case=='apply':
     status=json.loads((root/'audit/status.json').read_text());index=json.loads((root/'evidence/assets.json').read_text())
     if status['release_state']!='verified' or index['assets'][:7]!=hist or len(index['assets'])!=9:raise RuntimeError('bad applied fixture')
    records.append({'case':case,'mode':mode or ['normal'],'expected_success':expected,'exit_code':done.returncode,'control_unchanged':case!='apply','last_line':done.stdout.strip().splitlines()[-1]})
 a.output_dir.mkdir(parents=True,exist_ok=True)
 put(a.output_dir/'PROMOTION_TESTS.json',{'scope':'synthetic promotion fixtures only; no actual proof record generated or repository promoted','status':'PASS','executions':len(records),'records':records})
 print('PASS_PROMOTION_CONTROLS '+str(len(records)))
if __name__=='__main__':main()
