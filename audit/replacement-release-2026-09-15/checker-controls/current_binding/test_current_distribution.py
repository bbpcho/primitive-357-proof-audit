#!/usr/bin/env python3
"""Compact positive and adversarial fixtures for the additive current binding."""
import copy,hashlib,json,stat,sys,tempfile,unittest,zipfile
from pathlib import Path
from verify_current_distribution import (verify_current_distribution,EXPECTED_COVERAGE,MARKERS,
    EXPECTED_PRIOR_MARKERS,EXPECTED_SECTOR_MARKERS)

def encoded(obj):return (json.dumps(obj,indent=2)+'\n').encode()
def digest(b):return hashlib.sha256(b).hexdigest()
def row(path,data):return {'path':path,'bytes':len(data),'sha256':digest(data)}

class Fixture:
 def __init__(self,root):
  self.root=Path(root);self.root.mkdir(parents=True);self.public={};self.roles={};self.artifacts={};self.payloads={};self.edits={}
  self.tag='replay-companion-test.2';self.prefix='records/completed-replay/';self.repo='https://github.com/bbpcho/primitive-357-proof-audit'
 def role(self,name,data,path=None):
  data=encoded(data) if not isinstance(data,bytes) else data
  self.roles[name]=(data,path or self.prefix+name+'.json');return digest(data)
 def artifact(self,name,data):
  data=encoded(data) if not isinstance(data,bytes) else data;self.payloads[name]=data
  self.artifacts[name]=dict(row(name,data),archive_path=self.prefix+name)
  self.public[self.prefix+name]=data
  return digest(data)
 def apply(self,name,obj):
  if name in self.edits:self.edits[name](obj)
  return obj
 def build(self):
  code=b'print("original mathematical source")\n';logicals=[row('source.py',code)]
  logical={'schema':'primitive357_verified_release_manifest_v1','release_tag':'verified-2026-09-14.1','files':logicals}
  self.role('logical_manifest',logical,'objects/'+digest(encoded(logical)))
  mapping={'schema':'primitive357_replay_file_map_v1','files':sorted([dict(r,source={'kind':'object','path':'objects/'+r['sha256']}) for r in logicals]+[dict(row('RELEASE_MANIFEST.json',encoded(logical)),source={'kind':'object','path':'objects/'+digest(encoded(logical))})],key=lambda r:r['path'])}
  lock={'schema':'primitive357-external-inputs-lock-v1','inputs':[{'id':'source-reference','bytes':1,'sha256':digest(b'x'),'logical_destinations':[],'private_destinations':['reference.txt']}],'derived_inputs':[]}
  self.role('replay_file_map',mapping,'inputs/REPLAY_FILE_MAP.json');self.role('external_lock',lock,'inputs/EXTERNAL_INPUTS_LOCK.json');self.role('replay_contract',copy.deepcopy(EXPECTED_COVERAGE),'inputs/BASELINE_REPLAY_CONTRACT.json')
  self.public['objects/'+digest(code)]=code
  for name in ('logical_manifest','replay_file_map','external_lock','replay_contract'):
   data,path=self.roles[name];self.public[path]=data
  tested={'schema':'primitive357_externalized_companion_v1','release_tag':self.tag,'files':sorted([row(n,b) for n,b in self.public.items()],key=lambda r:r['path'])}
  self.role('tested_public_manifest',tested)
  subgroups={'H0':['D2','D3','D4','D5'],'H1':['D2','E','D4','D5'],'relation':'5E=D3+D4+3D5'}
  components=[]
  for key,marker in MARKERS.items():
   name='logs/'+key+'.log';sha=self.artifact('suite/'+name,(marker+'\n').encode());components.append({'id':key,'exit_code':0,'log':name,'sha256':sha})
  main={'schema':'primitive357_integrated_replay_v1','status':'PASS_FRESH_INTEGRATED_REPLAY','input_manifest':{'files':1,'manifest_sha256':digest(encoded(logical))},'components':components,'prior_groups':list(EXPECTED_COVERAGE['prior_required_job_ids_by_group']),'rank_conclusions':EXPECTED_COVERAGE['rank_conclusions'],'subgroups':subgroups}
  self.apply('main',main)
  rows=[]
  for names in EXPECTED_COVERAGE['prior_required_job_ids_by_group'].values():
   for n in names:
    log='logs/'+n+'.log';source='source/'+n+'.py';markers=EXPECTED_PRIOR_MARKERS[n]
    logsha=self.artifact('suite/prior/'+log,('\n'.join(markers)+'\n').encode());srcsha=self.artifact('suite/prior/'+source,code)
    rows.append({'id':n,'success':True,'exit_code':0,'log':log,'log_sha256':logsha,'source':source,'source_sha256':srcsha,'required_markers':markers})
  prior={'status':MARKERS['prior'],'groups':list(EXPECTED_COVERAGE['prior_required_job_ids_by_group']),'fresh_replay':True,'all_required_prior_jobs_passed':True,'required_full_prior_job_count':65,'observed_successful_job_count':65,'records':rows,'subgroups':subgroups};self.apply('prior',prior)
  rows=[]
  for n in EXPECTED_COVERAGE['sector_ids']:
   log='logs/'+n+'.log';marker=EXPECTED_SECTOR_MARKERS[n];sha=self.artifact('suite/sectors/'+log,(marker+'\n').encode());rows.append({'id':n,'exit_code':0,'log':log,'sha256':sha,'marker':marker})
  sectors={'status':MARKERS['sectors'],'records':rows};self.apply('sectors',sectors)
  rows=[]
  for n in EXPECTED_COVERAGE['rank_check_names']:
   log='logs/'+n+'.log';sha=self.artifact('suite/rank_local/'+log,b'actual finite check passed\n');rows.append({'name':n,'returncode':0,'log':log,'log_sha256':sha})
  upstream={n:self.artifact('suite/prior/'+n,b'finite producer output\n') for n in EXPECTED_COVERAGE['rank_upstream_relative_paths']}
  rank={'status':MARKERS['rank_local'],'fresh_checks':rows,'conclusions':EXPECTED_COVERAGE['rank_conclusions'],'fresh_upstream_sha256':upstream,'evidence_sha256':{'source.py':digest(code)}};self.apply('rank',rank)
  env={'status':'PASS_INDEPENDENT_REPLAY_ENVELOPE','input_manifest':main['input_manifest'],'sectors':13,'prior_jobs':65,'rank_checks':16,'fresh_rank_upstream_bindings':5};self.apply('envelope',env)
  for role,obj,name in [('integrated_result',main,'suite/REPLAY_RESULT.json'),('prior_result',prior,'suite/prior/PRIOR_REPLAY_RESULT.json'),('sector_result',sectors,'suite/sectors/SECTOR_REPLAY_RESULT.json'),('rank_result',rank,'suite/rank_local/rank_local_results.json'),('independent_envelope',env,'INDEPENDENT_ENVELOPE.json')]:
   self.role(role,obj,self.prefix+name);self.artifact(name,obj)
  intlogsha=self.artifact('INTEGRATED_REPLAY.log',b'PASS_FRESH_INTEGRATED_REPLAY\n');envlogsha=self.artifact('INDEPENDENT_ENVELOPE.log',encoded(env))
  outer={'status':'PASS_FRESH_EXTERNALIZED_COMPLETE_REPLAY','input_preservation':'all public, expanded and external inputs unchanged','distribution_manifest_sha256':digest(encoded(tested)),'logical_manifest_sha256':digest(encoded(logical)),'external_lock_sha256':digest(encoded(lock)),'integrated_result_sha256':digest(encoded(main)),'independent_envelope_sha256':digest(encoded(env)),'external_inputs':[{k:lock['inputs'][0][k] for k in ('id','bytes','sha256')}],'public_files':len(tested['files']),'logical_files':2,'INTEGRATED_REPLAY.log_sha256':intlogsha,'INDEPENDENT_ENVELOPE.log_sha256':envlogsha,'started_utc':'2026-09-15T12:00:01+00:00','finished_utc':'2026-09-15T12:01:01+00:00'};self.apply('outer',outer)
  self.role('externalized_result',outer,self.prefix+'EXTERNALIZED_REPLAY_RESULT.json');self.artifact('EXTERNALIZED_REPLAY_RESULT.json',outer)
  self.role('isolation_profile',b'(deny default)\n')
  ids=['allowed_distribution_read','allowed_logical_read','allowed_private_read','fresh_write_and_read','immutable_logical_write_denied','network_tcp_connect_denied','network_udp_send_denied','native_flint_execute_and_old_input_denied','ordinary_python_packages','sage_matrix','pari_gp','pdf_text_extractor','pdf_actual_text','denied_read_4','denied_read_5','denied_read_6']
  probes={'status':'PASS_OFFLINE_ISOLATION_PROBES','checks':[{'id':n,'passed':True} for n in ids]};self.apply('probes',probes);self.role('isolation_probes',probes)
  driverlog=encoded(outer);self.role('driver_log',driverlog)
  driver={'schema':'primitive357-isolated-driver-v1','status':'PASS_ISOLATED_DRIVER','output_did_not_exist':True,'exit_code':0,'distribution_manifest_sha256':digest(encoded(tested)),'logical_manifest_sha256':digest(encoded(logical)),'sandbox_profile_sha256':digest(self.roles['isolation_profile'][0]),'outer_log_sha256':digest(driverlog),'env':{'PYTHONOPTIMIZE':'0'},'command':['/usr/bin/sandbox-exec','-f','isolation_profile.json','python','-B','replay_companion.py'],'started_utc':'2026-09-15T12:00:00+00:00','finished_utc':'2026-09-15T12:01:02+00:00'};self.apply('driver',driver);self.role('isolated_driver',driver)
  selected=[dict(row(n.removeprefix('suite/'),b)) for n,b in self.payloads.items() if n.startswith('suite/')]
  selection={'schema':'primitive357_final_artifact_selection_v1','inspection_only':False,'component':'integrated','candidate_manifest_sha256':digest(encoded(logical)),'candidate_file_count':1,'files':sorted(selected,key=lambda r:r['path']),'selected_file_count':len(selected),'selected_bytes':sum(r['bytes'] for r in selected),'excluded':[]};self.apply('selection',selection);self.role('suite_selection',selection)
  index={'schema':'primitive357_retained_replay_artifacts_v1','source_suite_selection_sha256':digest(encoded(selection)),'files':sorted(self.artifacts.values(),key=lambda r:r['path'])};self.apply('artifacts',index);self.role('retained_artifacts',index)
  self.seal()
 def seal(self):
  for data,path in self.roles.values():self.public[path]=data
  final={'schema':'primitive357_externalized_companion_v1','release_tag':self.tag,'fresh_replay_result':self.prefix+'EXTERNALIZED_REPLAY_RESULT.json','tested_distribution_manifest_sha256':digest(self.roles['tested_public_manifest'][0]),'files':sorted([row(n,b) for n,b in self.public.items() if n!='COMPANION_MANIFEST.json'],key=lambda r:r['path'])}
  self.apply('final',final);self.role('final_public_manifest',final,'COMPANION_MANIFEST.json');self.public['COMPANION_MANIFEST.json']=encoded(final)
  records={}
  for role,(data,path) in self.roles.items():
   local='bound/'+role;target=self.root/local;target.parent.mkdir(exist_ok=True,parents=True);target.write_bytes(data);records[role]=dict(row(local,data),archive_path=path)
  for name,data in self.payloads.items():
   target=self.root/'outputs'/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
  self.archive=self.root/'companion.zip'
  with zipfile.ZipFile(self.archive,'w') as z:
   for n,b in sorted(self.public.items()):z.writestr('payload/'+n,b)
  data=self.archive.read_bytes();asset={'name':'companion.zip','bytes':len(data),'sha256':digest(data),'url':self.repo+'/releases/download/'+self.tag+'/companion.zip'}
  self.binding={'schema':'primitive357_current_distribution_binding_v1','release_tag':self.tag,'logical_release_tag':'verified-2026-09-14.1','verification_prefix':'records/completed-replay','local_artifact_root':'outputs','archive_root':'payload','asset':asset,'records':records}
  self.write_binding()
 def write_binding(self):
  data=encoded(self.binding);(self.root/'binding.json').write_bytes(data)
  self.status={'github_repository':self.repo,'current_distribution':{'state':'verified_externalized_replay','public_complete_replay_inputs_available':True,'replacement_complete_companion_published':True,'original_mathematical_replay_status_unchanged':True,'binding':row('binding.json',data)}}
 def verify(self,archive=False):return verify_current_distribution(self.root,self.status,self.archive if archive else None)

class Tests(unittest.TestCase):
 def setUp(self):self.tmp=tempfile.TemporaryDirectory();self.base=Path(self.tmp.name).resolve()
 def tearDown(self):self.tmp.cleanup()
 def fixture(self,edits=None):
  f=Fixture(self.base/'f');f.edits=edits or {};f.build();return f
 def rejection(self,role,edit):
  f=self.fixture({role:edit})
  with self.assertRaises((ValueError,KeyError,TypeError)):f.verify()
 def test_complete_record_binding(self):self.assertEqual(self.fixture().verify()['status'],'PASS_CURRENT_DISTRIBUTION_RECORD_BINDING')
 def test_complete_archive_binding(self):self.assertTrue(self.fixture().verify(True)['archive_payloads_checked'])
 def test_clean2_binding_preserves_failed_clean1(self):
  f=self.fixture();prefix=f.prefix+'isolation/'
  profile=f.roles['isolation_profile'][0];f.role('isolation_profile',profile,prefix+'clean2_offline.sb')
  probes=f.roles['isolation_probes'][0];f.role('isolation_probes',probes,prefix+'CLEAN2_PROBE_RESULTS.json')
  driver=json.loads(f.roles['isolated_driver'][0]);driver['command'][2]='clean2_offline.sb';f.role('isolated_driver',driver,prefix+'CLEAN2_ISOLATED_DRIVER.json')
  failed=dict(driver,status='FAILED_ISOLATED_DRIVER',exit_code=1)
  failed_path=f.prefix+'earlier-incomplete-run/CLEAN1_ISOLATED_DRIVER.json'
  f.public[failed_path]=encoded(failed)
  f.seal();self.assertTrue(f.verify(True)['archive_payloads_checked'])
  self.assertEqual(json.loads(f.public[failed_path])['exit_code'],1)
 def test_unchanged_named_source_copy(self):
  name='prior/source/export_contact_data.py'
  def selection(d):
   r=next(r for r in d['files'] if r['path']==name);d['files'].remove(r)
   d['selected_file_count']-=1;d['selected_bytes']-=r['bytes']
   d['excluded']=[dict(r,reason='identical_sealed_input_copy',candidate_path='source.py')]
  def artifacts(d):d['files'][:]=[r for r in d['files'] if r['path']!='suite/'+name]
  f=self.fixture({'selection':selection,'artifacts':artifacts});self.assertEqual(f.verify()['prior_jobs'],65)
 def test_missing_fano(self):self.rejection('sectors',lambda d:d['records'].pop())
 def test_missing_hecke_foundations(self):self.rejection('sectors',lambda d:d['records'].pop(-2))
 def test_missing_prior_job(self):self.rejection('prior',lambda d:d['records'].pop())
 def test_missing_rank_check(self):self.rejection('rank',lambda d:d['fresh_checks'].pop())
 def test_missing_producer(self):self.rejection('rank',lambda d:d['fresh_upstream_sha256'].pop(next(iter(d['fresh_upstream_sha256']))))
 def test_substituted_producer(self):self.rejection('rank',lambda d:d['fresh_upstream_sha256'].__setitem__(next(iter(d['fresh_upstream_sha256'])),'0'*64))
 def test_resumed_prior(self):self.rejection('prior',lambda d:d.__setitem__('fresh_replay',False))
 def test_failure_hidden_under_pass(self):self.rejection('sectors',lambda d:d['records'][0].__setitem__('exit_code',1))
 def test_bool_not_exit_code(self):self.rejection('prior',lambda d:d['records'][0].__setitem__('exit_code',False))
 def test_empty_required_markers(self):self.rejection('prior',lambda d:d['records'][0].__setitem__('required_markers',[]))
 def test_changed_tested_manifest_binding(self):self.rejection('outer',lambda d:d.__setitem__('distribution_manifest_sha256','0'*64))
 def test_false_envelope_count(self):self.rejection('envelope',lambda d:d.__setitem__('rank_checks',15))
 def test_nonfresh_driver(self):self.rejection('driver',lambda d:d.__setitem__('output_did_not_exist',False))
 def test_failed_driver_not_accepted_as_current(self):self.rejection('driver',lambda d:d.__setitem__('status','FAILED_ISOLATED_DRIVER'))
 def test_driver_wrong_profile(self):self.rejection('driver',lambda d:d['command'].__setitem__(2,'different.sb'))
 def test_driver_optimized_python(self):self.rejection('driver',lambda d:d['env'].__setitem__('PYTHONOPTIMIZE','1'))
 def test_failed_isolation(self):self.rejection('probes',lambda d:d['checks'][0].__setitem__('passed',False))
 def test_incomplete_selection(self):self.rejection('selection',lambda d:d.__setitem__('inspection_only',True))
 def test_missing_selected_output(self):self.rejection('artifacts',lambda d:d['files'].pop())
 def test_changed_log(self):
  f=self.fixture();next((f.root/'outputs/suite/prior/logs').glob('*.log')).write_text('different\n')
  with self.assertRaises(ValueError):f.verify()
 def test_log_symlink(self):
  f=self.fixture();p=next((f.root/'outputs/suite/prior/logs').glob('*.log'));copy=p.with_suffix('.real');p.rename(copy);p.symlink_to(copy)
  with self.assertRaises(ValueError):f.verify()
 def test_nonverification_addition(self):
  def edit(d):d['files'].append(row('unrelated.txt',b'x'));d['files'].sort(key=lambda r:r['path'])
  self.rejection('final',edit)
 def test_wrong_url(self):
  f=self.fixture();f.binding['asset']['url']='https://example.com/companion.zip';f.write_binding()
  with self.assertRaises(ValueError):f.verify()
 def test_extra_zip_member_even_rehashed(self):
  f=self.fixture()
  with zipfile.ZipFile(f.archive,'a') as z:z.writestr('payload/unlisted.txt',b'x')
  b=f.archive.read_bytes();f.binding['asset'].update(bytes=len(b),sha256=digest(b));f.write_binding()
  with self.assertRaises(ValueError):f.verify(True)
 def test_changed_zip_payload_even_rehashed(self):
  f=self.fixture();name=next(n for n in f.public if n.startswith('objects/'))
  with zipfile.ZipFile(f.archive,'w') as z:
   for n,b in f.public.items():z.writestr('payload/'+n,b'x'*len(b) if n==name else b)
  b=f.archive.read_bytes();f.binding['asset'].update(bytes=len(b),sha256=digest(b));f.write_binding()
  with self.assertRaises(ValueError):f.verify(True)
 def test_zip_symlink_payload_even_rehashed(self):
  f=self.fixture();name=next(iter(f.public))
  with zipfile.ZipFile(f.archive,'w') as z:
   for n,b in f.public.items():
    info=zipfile.ZipInfo('payload/'+n);info.external_attr=((stat.S_IFLNK|0o777) if n==name else (stat.S_IFREG|0o644))<<16;z.writestr(info,b)
  b=f.archive.read_bytes();f.binding['asset'].update(bytes=len(b),sha256=digest(b));f.write_binding()
  with self.assertRaises(ValueError):f.verify(True)
 def test_archive_symlink(self):
  f=self.fixture();original=f.archive.with_suffix('.real');f.archive.rename(original);f.archive.symlink_to(original)
  with self.assertRaises(ValueError):f.verify(True)
 def test_duplicate_zip_member_even_rehashed(self):
  f=self.fixture()
  with zipfile.ZipFile(f.archive,'a') as z:z.writestr('payload/COMPANION_MANIFEST.json',f.public['COMPANION_MANIFEST.json'])
  b=f.archive.read_bytes();f.binding['asset'].update(bytes=len(b),sha256=digest(b));f.write_binding()
  with self.assertRaises(ValueError):f.verify(True)
 def test_withdrawn_state_does_not_claim_pass(self):
  s={'current_distribution':{'state':'full_companion_withdrawn','public_complete_replay_inputs_available':False,'replacement_complete_companion_published':False}}
  self.assertEqual(verify_current_distribution(self.base,s)['status'],'CURRENT_DISTRIBUTION_NOT_VERIFIED')

if __name__=='__main__':unittest.main(verbosity=2)
