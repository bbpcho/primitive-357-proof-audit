from pathlib import Path
import zipfile,tarfile,io,hashlib,json,subprocess,collections,time
O=Path(__file__).resolve().parent
TARGET='8b69da80fe79959ed1e05d35b613f7f728f599571b8f84f0a0d29c78e4c205c6'
SIZE=235180
ARCH=('.zip','.tar','.tar.gz','.tgz','.gz')
def scan(data,label,stats,depth=0):
 if depth>12:raise RuntimeError('archive nesting exceeds 12: '+label)
 stats['objects_checked']+=1
 if len(data)==SIZE and hashlib.sha256(data).hexdigest()==TARGET:
  stats['matches'].append(label);print('MATCH',label,flush=True)
 if data[:4] in (b'PK\x03\x04',b'PK\x05\x06'):
  stats['archives_opened']+=1
  with zipfile.ZipFile(io.BytesIO(data)) as z:
   for i in z.infolist():
    if i.is_dir():continue
    if i.file_size==SIZE or i.filename.lower().endswith(ARCH):scan(z.read(i),label+'!'+i.filename,stats,depth+1)
 elif data[:2]==b'\x1f\x8b' or (len(data)>262 and data[257:262]==b'ustar'):
  stats['archives_opened']+=1
  try:
   with tarfile.open(fileobj=io.BytesIO(data),mode='r:*') as t:
    for i in t:
     if i.isfile() and (i.size==SIZE or i.name.lower().endswith(ARCH)):
      scan(t.extractfile(i).read(),label+'!'+i.name,stats,depth+1)
  except tarfile.ReadError:
   import gzip
   scan(gzip.decompress(data),label+'!<gzip payload>',stats,depth+1)
def result(data,label):
 s={'name':label,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'objects_checked':0,'archives_opened':0,'matches':[]}
 scan(data,label,s);return s
paths=[Path('work/p5_archive_audit/2026-09-13_p5_literal_c_obstruction_dependency_closure_v1.zip'),Path('work/rank_closure_audit/2026-09-13_corrected66_predyadic_and_p2_place2_dependency_closure_v1.zip'),Path('work/verified_release_2026_09_14/dist/PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1.zip'),Path('work/v3_audit/submission/anc/PRIMITIVE_357_REPRODUCIBILITY_V3.tar.gz')]
out={'target_sha256':TARGET,'target_bytes':SIZE,'archive_scans':[]}
for p in paths:
 print('START',p,flush=True)
 r=result(p.read_bytes(),str(p));out['archive_scans'].append(r);print('FINISHED',json.dumps(r),flush=True)
 (O/'PUBLIC_COPY_SCAN.json').write_text(json.dumps(out,indent=2)+'\n')
# The public companion embeds the already scanned verified archive. Authenticate it separately.
p=Path('work/PRIMITIVE_357_FIRST_SUBMISSION_COMPANION_V1.zip')
r={'name':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'embedded_verified':[]}
with zipfile.ZipFile(p) as z:
 for i in z.infolist():
  if i.filename.endswith('PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1.zip'):
   d=z.read(i);r['embedded_verified'].append({'member':i.filename,'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest()})
out['companion_binding']=r;(O/'PUBLIC_COPY_SCAN.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPANION',json.dumps(r),flush=True)
# Scan every reachable archive blob and every direct blob of the target length.
git='/Library/Developer/CommandLineTools/usr/bin/git'; repo='work/pre_submission_revision_2026_09_15/repository'
cmd=lambda *args:subprocess.check_output([git,'-C',repo,*args])
lines=cmd('rev-list','--objects','--all').decode().splitlines(); paths_by_id=collections.defaultdict(list)
for line in lines:
 parts=line.split(' ',1)
 if len(parts)==2:paths_by_id[parts[0]].append(parts[1])
ids=[line.split(' ',1)[0] for line in lines]
batch=subprocess.run([git,'-C',repo,'cat-file','--batch-check=%(objectname) %(objecttype) %(objectsize)'],input=('\n'.join(ids)+'\n').encode(),stdout=subprocess.PIPE,check=True).stdout.decode().splitlines()
tracked={'git_refs':cmd('show-ref').decode().splitlines(),'is_shallow':cmd('rev-parse','--is-shallow-repository').decode().strip(),'reachable_commit_count':int(cmd('rev-list','--count','--all')),'reachable_blob_count':0,'scanned_blob_count':0,'archive_blobs':[],'direct_pdf_matches':[]}
for line in batch:
 oid,typ,size=line.split();size=int(size)
 if typ!='blob':continue
 tracked['reachable_blob_count']+=1
 names=paths_by_id[oid]
 if size==SIZE or any(n.lower().endswith(ARCH) for n in names):
  data=cmd('cat-file','blob',oid);rr=result(data,'git:'+oid+':'+','.join(names));tracked['scanned_blob_count']+=1
  if any(n.lower().endswith(ARCH) for n in names):tracked['archive_blobs'].append(rr)
  if len(data)==SIZE and hashlib.sha256(data).hexdigest()==TARGET:tracked['direct_pdf_matches'].append(rr)
out['git_history_scan']=tracked;(O/'PUBLIC_COPY_SCAN.json').write_text(json.dumps(out,indent=2)+'\n');print('GIT_HISTORY',json.dumps(tracked),flush=True)
