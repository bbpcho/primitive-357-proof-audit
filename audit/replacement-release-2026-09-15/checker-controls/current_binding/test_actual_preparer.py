#!/usr/bin/env python3
"""Run the unchanged parent preparer against a small complete synthetic archive."""
from pathlib import Path
import contextlib,hashlib,importlib.util,io,json,shutil,sys,tempfile,zipfile
from test_current_distribution import Fixture,encoded,digest,row

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'prepare_current_binding.py'
sp=importlib.util.spec_from_file_location('actual_parent_preparer',SOURCE)
parent=importlib.util.module_from_spec(sp);sp.loader.exec_module(parent)
with tempfile.TemporaryDirectory(dir=HERE,prefix='actual-preparer-') as tmp:
 root=Path(tmp).resolve();fixture=Fixture(root/'fixture');fixture.build()
 tested_names={r['path'] for r in json.loads(fixture.roles['tested_public_manifest'][0])['files']}
 # Retain all original public objects; give each required compact record its
 # actual finalizer filename. This changes only our synthetic record transport.
 for role,path in parent.ROLES.items():
  if role=='final_public_manifest':continue
  data,old_path=fixture.roles[role]
  if old_path!=path and old_path not in tested_names:fixture.public.pop(old_path,None)
  if role=='isolated_driver':
   obj=json.loads(data);obj['command'][2]=Path(parent.ROLES['isolation_profile']).name;data=encoded(obj)
  fixture.roles[role]=(data,path);fixture.public[path]=data
 final={'schema':'primitive357_externalized_companion_v1','release_tag':fixture.tag,
        'fresh_replay_result':parent.ROLES['externalized_result'],
        'tested_distribution_manifest_sha256':digest(fixture.roles['tested_public_manifest'][0]),
        'files':sorted([row(n,b) for n,b in fixture.public.items() if n!='COMPANION_MANIFEST.json'],key=lambda r:r['path'])}
 fixture.public['COMPANION_MANIFEST.json']=encoded(final)
 public=root/'payload';public.mkdir()
 for name,data in fixture.public.items():
  dest=public/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
 archive=root/'companion.zip'
 with zipfile.ZipFile(archive,'w') as z:
  for name,data in sorted(fixture.public.items()):z.writestr('payload/'+name,data)
 # Redirect only the preparer's workspace/output constant; its source bytes and
 # imported checker functions remain the real, unmodified parent versions.
 parent.N=root
 (root/'current_binding').mkdir()
 for name in ('verify_current_distribution.py','current_replay_coverage.py'):
  shutil.copyfile(HERE/name,root/'current_binding'/name)
 (root/'FINAL_ARCHIVE_IDENTITY.json').write_bytes(encoded({'name':archive.name,'bytes':archive.stat().st_size,'sha256':digest(archive.read_bytes()),'release_tag':fixture.tag}))
 sys.argv=[str(SOURCE),'--final-root',str(public),'--archive',str(archive),'--output',str(root/'prepared')]
 good_args=list(sys.argv)
 forbidden=public/'nested-output'
 sys.argv=good_args[:-1]+[str(forbidden)]
 try:parent.main()
 except ValueError as exc:
  if 'Roots must be disjoint' not in str(exc):raise
 else:raise ValueError('Preparer accepted output inside sealed final root')
 if forbidden.exists():raise ValueError('Preparer created forbidden nested output before rejecting')
 sys.argv=good_args
 stream=io.StringIO()
 with contextlib.redirect_stdout(stream):parent.main()
 result=json.loads(stream.getvalue())
 if result.get('status')!='PASS_CANDIDATE_CONTROL_OVERLAY' or result.get('archive_payloads_checked') is not True:
  raise ValueError('Actual preparer did not pass')
 report={'status':'PASS_ACTUAL_PARENT_PREPARER_COMPACT_FIXTURE','parent_source':str(SOURCE),'parent_source_sha256':digest(SOURCE.read_bytes()),'result':result,'nested_output_rejected_before_creation':True,'fixture_only':True,'public_status_or_original_inputs_modified':False}
 (HERE/'ACTUAL_PREPARER_CHECK.json').write_bytes(encoded(report))
 print(json.dumps(report,indent=2))
