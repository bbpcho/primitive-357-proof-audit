#!/usr/bin/env python3
"""Synthetic positive/negative controls; does not claim an arithmetic replay."""
from pathlib import Path
import argparse, copy, hashlib, json, os, shutil, subprocess, sys, tempfile

SOURCE=Path(__file__).resolve().parents[1]
TAG='verified-2026-09-14.1'
AID='PRIMITIVE_357_VERIFIED_RELEASE_2026_09_14_V1'
RDIR='audit/verified-2026-09-14/'

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(root,path,value):
 p=root/path;p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(value,indent=2)+'\n' if isinstance(value,(dict,list)) else value)
def read(root,path):return json.loads((root/path).read_text())
def manifest(root):
 files=[]
 for p in root.rglob('*'):
  r=p.relative_to(root)
  if r.parts[0] in ('.git','build') or r.as_posix()=='evidence/TRACKED_SNAPSHOT_SHA256.txt':continue
  if p.is_file() and not(p.parent.name=='__pycache__' and p.suffix in ('.pyc','.pyo')):
   files.append((r.as_posix(),digest(p)))
 put(root,'evidence/TRACKED_SNAPSHOT_SHA256.txt',''.join(f'{h}  {n}\n' for n,h in sorted(files)))
def refresh_assets(root,assets):
 d=read(root,'evidence/assets.json');d['assets']=assets;put(root,'evidence/assets.json',d)
 put(root,'evidence/checksums/RELEASE_ASSETS_SHA256.txt',''.join(f"{x['sha256']}  {x['filename']}\n" for x in assets))
def binding_update(root,key):
 b=read(root,RDIR+'REPLAY_BINDING.json');b[key]['sha256']=digest(root/b[key]['path']);put(root,RDIR+'REPLAY_BINDING.json',b)
def mutate_record(root,path,fn,key):
 d=read(root,RDIR+path);fn(d);put(root,RDIR+path,d);binding_update(root,key)
def fixture(root,assets,workspace,verified=False):
 (root/'scripts').mkdir(parents=True)
 for f in ('verification_common.py','verify_repository.py','verify_assets.py'):
  shutil.copy2(SOURCE/'scripts'/f,root/'scripts'/f)
 for f in ('README.md','paper/manuscript.tex','paper/rank-proof.tex','paper/manuscript.pdf','docs/PROOF_STATUS.md','docs/RANK_GAP.md','docs/EVIDENCE.md','docs/H0_H1_CORRIGENDUM.md','docs/RELEASE_PROCESS.md',RDIR+'PAPER_BUILD.log'):
  put(root,f,'SYNTHETIC CONTROL FIXTURE — no mathematical evidence\n')
 for f in ('audit/status.json','audit/rank-gap/gates.json'):
  put(root,f,read(SOURCE,f))
 # Fixtures must not inherit the hosting repository's pending/verified phase.
 status=read(root,'audit/status.json')
 status.update(release_state='pending_fresh_replay',proof_complete=False,
               public_proof_release_authorized=False,
               fresh_replay={'state':'pending','binding':None},blocking_gate='synthetic pending fixture')
 for gate in status['gates']:
  if gate['id'] in ('fresh_integrated_replay','public_proof_release'):
   gate.update(state='pending',evidence='docs/RELEASE_PROCESS.md')
 put(root,'audit/status.json',status)
 payload=b'synthetic sealed asset bytes\n';assets.mkdir();workspace.mkdir();(workspace/'assets').mkdir()
 (assets/'archive.zip').write_bytes(payload);(workspace/'assets/archive.zip').write_bytes(payload)
 item={'id':AID,'filename':'archive.zip','sha256':digest(assets/'archive.zip'),'bytes':len(payload),'source_path_from_workspace':'assets/archive.zip'}
 put(root,'evidence/assets.json',{'schema':'primitive_357_release_asset_index_v1','assets':[]});refresh_assets(root,[item])
 if verified:
  row=lambda n,b:{'path':n,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
  rows=[row('a.txt',b'a'),row('scripts/check.py',b'check')]
  m={'schema':'primitive357_verified_release_manifest_v1','files':rows}
  put(root,RDIR+'TESTED_RELEASE_MANIFEST.json',m);put(root,RDIR+'FINAL_RELEASE_MANIFEST.json',m)
  put(root,RDIR+'PROOF_INPUTS_SHA256.json',{'schema':'primitive357_proof_inputs_v1','release_tag':TAG,'files':rows})
  components=[]
  for name,marker in [('prior','PASS_SELECTED_PRIOR_GROUPS'),('rank_local','PASS_FRESH_RANK_LOCAL_COMPONENT'),('sectors','PASS_FRESH_TEN_SECTORS_AND_INTERFACES')]:
   log='logs/'+name+'.log';put(root,RDIR+log,marker+'\n')
   components.append({'id':name,'exit_code':0,'log':log,'sha256':digest(root/(RDIR+log)),'seconds':0.1})
  result={'schema':'primitive357_integrated_replay_v1','status':'PASS_FRESH_INTEGRATED_REPLAY','input_manifest':{'files':len(rows),'manifest_sha256':digest(root/(RDIR+'TESTED_RELEASE_MANIFEST.json'))},'components':components,'prior_groups':['exports','rawdyadic','foundation','fiveplace','p5','logs','finite_maps'],'rank_conclusions':{'equals_B_plus_literal_c':True}}
  put(root,RDIR+'REPLAY_RESULT.json',result)
  bind={'schema':'primitive357_replay_binding_v1','release_tag':TAG,'asset_id':AID,'asset_sha256':item['sha256'],'asset_bytes':item['bytes']}
  for k,p in [('replay_result','REPLAY_RESULT.json'),('tested_manifest','TESTED_RELEASE_MANIFEST.json'),('proof_inputs','PROOF_INPUTS_SHA256.json'),('final_manifest','FINAL_RELEASE_MANIFEST.json')]:
   bind[k]={'path':RDIR+p,'sha256':digest(root/(RDIR+p))}
  put(root,RDIR+'REPLAY_BINDING.json',bind)
  s=read(root,'audit/status.json');s.update(release_state='verified',proof_complete=True,public_proof_release_authorized=True,fresh_replay={'state':'pass','binding':RDIR+'REPLAY_BINDING.json'})
  for g in s['gates']:
   if g['id'] in ('fresh_integrated_replay','public_proof_release'):g['state']='pass'
  put(root,'audit/status.json',s)
 manifest(root)

def main():
 global SOURCE
 parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path,default=SOURCE/'build/verifier-controls');a=parser.parse_args();a.output_dir.mkdir(parents=True,exist_ok=True)
 records=[]
 def run_case(name,change=None,expected=True,verified=False,regenerate=True,tool='repo',source='flat',asset_ids=()):
  with tempfile.TemporaryDirectory(prefix='primitive357-control-') as temp:
   base=Path(temp);root=base/'repo';assets=base/'assets';workspace=base/'workspace';fixture(root,assets,workspace,verified)
   if change:change(root,assets,workspace)
   if regenerate:manifest(root)
   for mode in ([],['-O'],['-OO']):
    cmd=[sys.executable,'-B',*mode,str(root/'scripts'/('verify_repository.py' if tool=='repo' else 'verify_assets.py'))]
    if tool!='repo':cmd+=['--assets-dir',str(assets)] if source=='flat' else ['--workspace-root',str(workspace)]
    for asset_id in asset_ids:cmd+=['--asset-id',asset_id]
    done=subprocess.run(cmd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
    success=done.returncode==0
    rec={'case':name,'mode':mode or ['normal'],'expected_pass':expected,'exit_code':done.returncode,'matched':success==expected,'output':done.stdout.strip()};records.append(rec)
    if success!=expected:raise RuntimeError('negative-control mismatch: '+json.dumps(rec))
 def status_change(fn):
  def edit(r,a,w):d=read(r,'audit/status.json');fn(d);put(r,'audit/status.json',d)
  return edit
 def assets_change(fn):
  def edit(r,a,w):d=read(r,'evidence/assets.json')['assets'];fn(d);refresh_assets(r,d)
  return edit
 def rr(path,fn,key='replay_result'):
  return lambda r,a,w:mutate_record(r,path,fn,key)
 run_case('valid_pending')
 run_case('valid_verified',verified=True)
 # CI runs these controls after the real repository has been promoted.
 # Model that source state explicitly without changing the actual repository.
 with tempfile.TemporaryDirectory(prefix='primitive357-verified-host-fixture-') as temp:
  actual_source=SOURCE;host=Path(temp)
  (host/'scripts').mkdir()
  for name in ('verification_common.py','verify_repository.py','verify_assets.py'):
   shutil.copy2(actual_source/'scripts'/name,host/'scripts'/name)
  host_status=read(actual_source,'audit/status.json')
  host_status.update(release_state='verified',proof_complete=True,public_proof_release_authorized=True,
                     fresh_replay={'state':'pass','binding':RDIR+'REPLAY_BINDING.json'})
  for gate in host_status['gates']:
   if gate['id'] in ('fresh_integrated_replay','public_proof_release'):
    gate.update(state='pass',evidence=RDIR+'REPLAY_BINDING.json')
  put(host,'audit/status.json',host_status)
  put(host,'audit/rank-gap/gates.json',read(actual_source,'audit/rank-gap/gates.json'))
  SOURCE=host
  try:run_case('valid_pending_fixture_from_verified_host')
  finally:SOURCE=actual_source
 run_case('empty_assets',assets_change(lambda x:x.clear()),False)
 run_case('duplicate_gate_id',status_change(lambda d:d['gates'].append(copy.deepcopy(d['gates'][0]))),False)
 run_case('missing_gate',status_change(lambda d:d['gates'].pop()),False)
 run_case('disabled_gate',status_change(lambda d:d['gates'][0].update(mandatory=False)),False)
 run_case('premature_proof_flag',status_change(lambda d:d.update(proof_complete=True)),False)
 run_case('duplicate_asset_id',assets_change(lambda x:x.append(dict(x[0],filename='other.zip'))),False)
 run_case('bool_asset_bytes',assets_change(lambda x:x[0].update(bytes=True)),False)
 run_case('traversing_asset_filename',assets_change(lambda x:x[0].update(filename='../archive.zip')),False)
 run_case('traversing_workspace_path',assets_change(lambda x:x[0].update(source_path_from_workspace='../archive.zip')),False)
 for name,path in [('untracked_file','extra.txt'),('untracked_nested_build','evidence/build/extra.txt'),('untracked_nested_git','evidence/.git/extra.txt'),('untracked_cache_payload','scripts/__pycache__/payload.json')]:
  run_case(name,lambda r,a,w,p=path:put(r,p,'untracked\n'),False,regenerate=False)
 run_case('root_build_exclusion',lambda r,a,w:put(r,'build/generated.log','generated\n'),True,regenerate=False)
 run_case('compiled_cache_exclusion',lambda r,a,w:put(r,'scripts/__pycache__/generated.pyc','generated'),True,regenerate=False)
 run_case('tracked_digest_mismatch',lambda r,a,w:put(r,'README.md','changed\n'),False,regenerate=False)
 def omission(r,a,w):
  p=r/'evidence/TRACKED_SNAPSHOT_SHA256.txt';p.write_text('\n'.join(p.read_text().splitlines()[1:])+'\n')
 run_case('manifest_omission',omission,False,regenerate=False)
 def duplicate(r,a,w):
  p=r/'evidence/TRACKED_SNAPSHOT_SHA256.txt';p.write_text(p.read_text()+p.read_text().splitlines()[0]+'\n')
 run_case('manifest_duplicate',duplicate,False,regenerate=False)
 run_case('directory_symlink',lambda r,a,w:(r/'linked').symlink_to(a,target_is_directory=True),False,regenerate=False)
 run_case('excluded_root_symlink',lambda r,a,w:(r/'build').symlink_to(a,target_is_directory=True),False,regenerate=False)
 def parentlink(r,a,w):
  shutil.move(str(r/'docs'),str(a/'docs'));(r/'docs').symlink_to(a/'docs',target_is_directory=True)
 run_case('parent_component_symlink',parentlink,False,regenerate=False)
 def dupjson(r,a,w):
  p=r/'audit/status.json';p.write_text(p.read_text().replace('"proof_complete": false,','"proof_complete": true, "proof_complete": false,'))
 run_case('duplicate_json_key',dupjson,False)
 run_case('replay_missing_component',rr('REPLAY_RESULT.json',lambda d:d['components'].pop()),False,True)
 run_case('replay_duplicate_component',rr('REPLAY_RESULT.json',lambda d:d['components'].append(copy.deepcopy(d['components'][0]))),False,True)
 run_case('replay_failed_component',rr('REPLAY_RESULT.json',lambda d:d['components'][0].update(exit_code=1)),False,True)
 run_case('replay_bool_exit_code',rr('REPLAY_RESULT.json',lambda d:d['components'][0].update(exit_code=False)),False,True)
 run_case('replay_missing_prior_group',rr('REPLAY_RESULT.json',lambda d:d['prior_groups'].pop()),False,True)
 run_case('replay_wrong_manifest',rr('REPLAY_RESULT.json',lambda d:d['input_manifest'].update(manifest_sha256='0'*64)),False,True)
 run_case('replay_failed_rank_join',rr('REPLAY_RESULT.json',lambda d:d['rank_conclusions'].update(equals_B_plus_literal_c=False)),False,True)
 run_case('proof_index_omits_input',rr('PROOF_INPUTS_SHA256.json',lambda d:d['files'].pop(),'proof_inputs'),False,True)
 run_case('proof_index_changes_input',rr('PROOF_INPUTS_SHA256.json',lambda d:d['files'][0].update(sha256='0'*64),'proof_inputs'),False,True)
 run_case('final_manifest_changes_tested_input',rr('FINAL_RELEASE_MANIFEST.json',lambda d:d['files'][0].update(sha256='0'*64),'final_manifest'),False,True)
 run_case('final_manifest_omits_tested_input',rr('FINAL_RELEASE_MANIFEST.json',lambda d:d['files'].pop(),'final_manifest'),False,True)
 run_case('sealed_asset_binding_mismatch',lambda r,a,w:mutate_binding(r),False,True)
 run_case('replay_log_changed',lambda r,a,w:put(r,RDIR+'logs/prior.log','changed\n'),False,True)
 for source in ('flat','workspace'):
  run_case('valid_assets_'+source,tool='assets',source=source)
  run_case('empty_assets_'+source,assets_change(lambda x:x.clear()),False,tool='assets',source=source)
  run_case('duplicate_asset_id_'+source,assets_change(lambda x:x.append(dict(x[0],filename='other.zip'))),False,tool='assets',source=source)
  run_case('asset_traversal_'+source,assets_change(lambda x:x[0].update(source_path_from_workspace='../archive.zip')),False,tool='assets',source=source)
 def badasset(r,a,w):(a/'archive.zip').write_bytes(b'wrong')
 run_case('wrong_asset_bytes',badasset,False,tool='assets')
 def assetlink(r,a,w):
  (a/'archive.zip').unlink();(a/'archive.zip').symlink_to(w/'assets/archive.zip')
 run_case('asset_file_symlink',assetlink,False,tool='assets')
 def workspace_link(r,a,w):
  shutil.rmtree(w/'assets');(w/'assets').symlink_to(a,target_is_directory=True)
 run_case('asset_parent_symlink',workspace_link,False,tool='assets',source='workspace')
 run_case('selected_asset',tool='assets',asset_ids=(AID,))
 run_case('unknown_asset_selection',expected=False,tool='assets',asset_ids=('UNKNOWN',))
 run_case('duplicate_asset_selection',expected=False,tool='assets',asset_ids=(AID,AID))
 add_absent=assets_change(lambda x:x.append(dict(x[0],id='OTHER',filename='other.zip',source_path_from_workspace='assets/other.zip')))
 run_case('default_still_checks_all_assets',add_absent,False,tool='assets')
 run_case('selection_skips_unrequested_asset_bytes',add_absent,True,tool='assets',asset_ids=(AID,))
 def add_second(r,a,w):
  add_absent(r,a,w);shutil.copy2(a/'archive.zip',a/'other.zip')
 run_case('multiple_selected_assets',add_second,True,tool='assets',asset_ids=(AID,'OTHER'))
 summary={'scope':'synthetic control-verifier tests, not mathematical replay','status':'PASS','cases':len(records)//3,'executions':len(records),'records':records}
 (a.output_dir/'CONTROL_VERIFIER_TESTS.json').write_text(json.dumps(summary,indent=2)+'\n')
 (a.output_dir/'CONTROL_VERIFIER_TESTS.log').write_text('\n'.join(f"PASS {r['case']} {r['mode']} exit={r['exit_code']}" for r in records)+'\n')
 print('PASS_CONTROL_VERIFIER_TESTS '+str(len(records))+' executions')

def mutate_binding(root):
 p=RDIR+'REPLAY_BINDING.json';d=read(root,p);d['asset_sha256']='0'*64;put(root,p,d)

if __name__=='__main__':main()
