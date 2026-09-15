#!/usr/bin/env python3
"""Bind the current distribution to retained evidence; never rerun mathematics.

Historical verify_repository.py metadata is deliberately outside this module.
Default checks authenticate committed result records and actual completion logs.
An optional archive argument also authenticates every final ZIP member. Neither
mode turns saved records into a new execution or a formal mathematical proof.
"""
from pathlib import Path,PurePosixPath
import datetime,hashlib,json,re,stat,unicodedata,zipfile
from urllib.parse import quote
from current_replay_coverage import EXPECTED_COVERAGE,EXPECTED_PRIOR_MARKERS,EXPECTED_SECTOR_MARKERS

HEX=re.compile(r'[0-9a-f]{64}\Z')
ROLES={'tested_public_manifest','final_public_manifest','logical_manifest','replay_file_map',
       'external_lock','replay_contract','externalized_result','integrated_result',
       'independent_envelope','prior_result','sector_result','rank_result','retained_artifacts',
       'isolated_driver','driver_log','isolation_profile','isolation_probes','suite_selection'}
MARKERS={'prior':'PASS_SELECTED_PRIOR_GROUPS','rank_local':'PASS_FRESH_RANK_LOCAL_COMPONENT',
         'sectors':'PASS_FRESH_TEN_SECTORS_AND_INTERFACES'}

def need(ok,msg):
    if not ok:raise ValueError(msg)
def unique(pairs):
    d={}
    for k,v in pairs:
        need(k not in d,'Duplicate JSON key: '+k);d[k]=v
    return d
def parse(data):return json.loads(data,object_pairs_hook=unique)
def sha(data):return hashlib.sha256(data).hexdigest()
def rel(name):
    need(isinstance(name,str) and name and '\\' not in name and '\x00' not in name,'Malformed relative path')
    p=PurePosixPath(name)
    need(not p.is_absolute() and all(x not in ('','.','..') for x in name.split('/')) and str(p)==name,'Unsafe relative path')
    return name
def identity(row):
    need(type(row['bytes']) is int and row['bytes']>=0 and isinstance(row['sha256'],str) and HEX.fullmatch(row['sha256']),'Malformed identity')
    return {k:row[k] for k in ('bytes','sha256')}
def read_bound(root,row):
    name=rel(row['path']);path=Path(root)/name
    for q in (path,*path.parents):need(not q.is_symlink(),'Symlink in bound path: '+str(q))
    need(path.is_file() and stat.S_ISREG(path.stat().st_mode),'Missing regular bound file: '+name)
    data=path.read_bytes();need({'bytes':len(data),'sha256':sha(data)}==identity(row),'Changed bound file: '+name)
    return data
def indexed(rows,key='path',ordered=False):
    need(isinstance(rows,list) and rows,'Empty record list');d={};aliases=set()
    for r in rows:
        name=r[key];need(isinstance(name,str) and name not in d,'Duplicate record')
        alias=unicodedata.normalize('NFC',name).casefold();need(alias not in aliases,'Case-colliding record');aliases.add(alias);d[name]=r
        if key=='path':rel(name);identity(r)
    if key=='path':
        for name in d:
            need(not any('/'.join(name.split('/')[:i]) in d for i in range(1,len(name.split('/')))),'File/directory path collision')
    if ordered:need(list(d)==sorted(d),'Unsorted records')
    return d
def manifest(data,schema,tag):
    obj=parse(data);need(obj.get('schema')==schema and obj.get('release_tag')==tag,'Manifest identity/schema')
    return indexed(obj['files'],ordered=True)
def exact_ids(rows,key,expected,label):
    actual=indexed(rows,key);need(list(actual)==list(expected),label+' IDs/order mismatch');return actual
def zero(value,label):need(type(value) is int and value==0,label+' did not exit successfully')
def timestamp(s):
    d=datetime.datetime.fromisoformat(s.replace('Z','+00:00'));need(d.tzinfo is not None,'Timestamp lacks timezone');return d

def verify_current_distribution(root,status,archive=None):
    current=status['current_distribution']
    if current.get('state') in {'full_companion_withdrawn','pending_complete_replay'}:
        need(current.get('public_complete_replay_inputs_available') is False and current.get('replacement_complete_companion_published') is False,'Pending/withdrawn distribution claims publication')
        return {'status':'CURRENT_DISTRIBUTION_NOT_VERIFIED','state':current['state']}
    need(current.get('state')=='verified_externalized_replay','Unknown current distribution state')
    need(current.get('public_complete_replay_inputs_available') is True and current.get('replacement_complete_companion_published') is True and current.get('original_mathematical_replay_status_unchanged') is True,'Current distribution flags disagree')
    binding=parse(read_bound(root,current['binding']))
    need(binding.get('schema')=='primitive357_current_distribution_binding_v1','Current binding schema')
    tag=binding['release_tag'];need(isinstance(tag,str) and re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*',tag),'Bad release tag')
    asset=binding['asset'];identity(asset);rel(asset['name']);need('/' not in asset['name'] and asset['name'].endswith('.zip'),'Bad archive name')
    repository=status['github_repository'].rstrip('/')
    need(re.fullmatch(r'https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+',repository),'Bad repository URL')
    need(asset['url']==repository+'/releases/download/'+quote(tag,safe='')+'/'+quote(asset['name'],safe=''),'Archive URL/tag/name mismatch')
    records=binding['records'];need(set(records)==ROLES,'Missing/extra current binding role')
    raw={k:read_bound(root,v) for k,v in records.items()}
    tested=manifest(raw['tested_public_manifest'],'primitive357_externalized_companion_v1',tag)
    final=manifest(raw['final_public_manifest'],'primitive357_externalized_companion_v1',tag)
    final_meta=parse(raw['final_public_manifest'])
    need(final_meta.get('fresh_replay_result')==records['externalized_result']['archive_path'] and final_meta.get('tested_distribution_manifest_sha256')==sha(raw['tested_public_manifest']),'Final manifest replay pointers')
    need('COMPANION_MANIFEST.json' not in tested and 'COMPANION_MANIFEST.json' not in final,'Self-referential public manifest')
    prefix=rel(binding['verification_prefix'])+'/'
    need(prefix.startswith('records/'),'Verification additions must be records')
    for name,row in tested.items():need(name in final and row==final[name],'Tested public input changed/disappeared: '+name)
    need(set(final)-set(tested) and all(n.startswith(prefix) for n in set(final)-set(tested)),'Nonverification addition or no completed records')
    for role,row in records.items():
        name=rel(row['archive_path'])
        if role=='final_public_manifest':need(name=='COMPANION_MANIFEST.json','Wrong final manifest archive path')
        else:need(name in final and identity(final[name])==identity(row),'Record not bound into final archive: '+role)
    for role,path in [('replay_file_map','inputs/REPLAY_FILE_MAP.json'),('external_lock','inputs/EXTERNAL_INPUTS_LOCK.json'),('replay_contract','inputs/BASELINE_REPLAY_CONTRACT.json')]:
        need(records[role]['archive_path']==path and path in tested and identity(tested[path])==identity(records[role]),'Tested input role binding: '+role)
    logical_tag=binding['logical_release_tag'];need(logical_tag=='verified-2026-09-14.1','Unexpected historical logical tag')
    logical=manifest(raw['logical_manifest'],'primitive357_verified_release_manifest_v1',logical_tag)
    need('RELEASE_MANIFEST.json' not in logical,'Self-referential logical manifest')
    mapping=parse(raw['replay_file_map']);need(mapping.get('schema')=='primitive357_replay_file_map_v1','Logical mapping schema')
    mapped=indexed(mapping['files'],ordered=True);need(set(mapped)==set(logical)|{'RELEASE_MANIFEST.json'},'Logical map coverage')
    for name,row in logical.items():need(identity(row)==identity(mapped[name]),'Logical mapping identity mismatch')
    need(identity(mapped['RELEASE_MANIFEST.json'])==identity(records['logical_manifest']),'Logical manifest/map binding')
    lock=parse(raw['external_lock']);need(lock.get('schema')=='primitive357-external-inputs-lock-v1','External lock schema')
    external=indexed(lock['inputs']+lock.get('derived_inputs',[]),'id');dest={}
    for e in external.values():
        identity(e)
        for n in e['logical_destinations']:
            rel(n);need(n not in dest,'Duplicate external logical destination');dest[n]=e['id']
    need(set(dest)<=set(mapped),'External destination missing from logical mapping')
    for name,row in mapped.items():
        if name in dest:need(row['source']=={'kind':'external','id':dest[name]} and identity(row)==identity(external[dest[name]]),'External mapping substitution')
        else:
            obj='objects/'+row['sha256'];need(row['source']=={'kind':'object','path':obj} and obj in tested and identity(row)==identity(tested[obj]),'Object mapping substitution')
    contract=parse(raw['replay_contract'])
    for k,v in EXPECTED_COVERAGE.items():need(contract[k]==v,'Changed replay coverage contract: '+k)
    artifacts=parse(raw['retained_artifacts']);need(artifacts.get('schema')=='primitive357_retained_replay_artifacts_v1','Artifact index schema')
    need(artifacts['source_suite_selection_sha256']==sha(raw['suite_selection']),'Artifact selection binding')
    selection=parse(raw['suite_selection'])
    need(selection['schema']=='primitive357_final_artifact_selection_v1' and selection['inspection_only'] is False and selection['component']=='integrated' and selection['candidate_manifest_sha256']==sha(raw['logical_manifest']) and selection['candidate_file_count']==len(logical),'Wrong/incomplete suite artifact selection')
    artifacts=indexed(artifacts['files'],ordered=True)
    for name,row in artifacts.items():
        target=rel(row['archive_path']);need(target in final and identity(final[target])==identity(row),'Missing/substituted retained artifact: '+name)
    selected=indexed(selection['files'],ordered=True)
    need(selection['selected_file_count']==len(selected) and selection['selected_bytes']==sum(r['bytes'] for r in selected.values()),'Selection counts')
    for name,row in selected.items():need('suite/'+name in artifacts and identity(row)==identity(artifacts['suite/'+name]),'Selected output missing from final records')
    excluded={}
    for row in selection['excluded']:
        name=row['path'];rel(name.removesuffix('/'))
        need(name not in excluded,'Duplicate excluded artifact');excluded[name]=row
    need(not set(selected)&set(excluded),'Selected/excluded overlap')
    def artifact(name,digest,local=False):
        name=rel(name)
        if name not in artifacts and not local:
            # The trusted selection excludes only unchanged named input copies.
            # Preserve that explicit path binding instead of guessing by hash.
            old=excluded.get(name.removeprefix('suite/'))
            need(old is not None and old.get('reason')=='identical_sealed_input_copy','Missing retained artifact: '+name)
            candidate=old['candidate_path'];need(candidate in logical and identity(old)==identity(logical[candidate]) and old['sha256']==digest,'Changed excluded input copy: '+name)
            return old
        need(name in artifacts and artifacts[name]['sha256']==digest,'Replay artifact identity mismatch: '+name)
        row=artifacts[name]
        if local:
            local_path=row.get('local_path',rel(binding['local_artifact_root'])+'/'+name)
            return read_bound(root,dict(row,path=local_path)).decode('utf8')
        return row
    outer=parse(raw['externalized_result']);main=parse(raw['integrated_result']);envelope=parse(raw['independent_envelope'])
    expected_input={'files':len(logical),'manifest_sha256':sha(raw['logical_manifest'])}
    need(outer['status']=='PASS_FRESH_EXTERNALIZED_COMPLETE_REPLAY' and outer['input_preservation']=='all public, expanded and external inputs unchanged','Outer replay not complete/preserved')
    need(outer['distribution_manifest_sha256']==sha(raw['tested_public_manifest']) and outer['logical_manifest_sha256']==sha(raw['logical_manifest']) and outer['external_lock_sha256']==sha(raw['external_lock']),'Outer tested input binding')
    need(outer['integrated_result_sha256']==sha(raw['integrated_result']) and outer['independent_envelope_sha256']==sha(raw['independent_envelope']),'Outer result/envelope binding')
    integrated_log=artifact('INTEGRATED_REPLAY.log',outer['INTEGRATED_REPLAY.log_sha256'],True)
    need(sum(line.strip()=='PASS_FRESH_INTEGRATED_REPLAY' for line in integrated_log.splitlines())==1,'Outer integrated completion log')
    need(parse(artifact('INDEPENDENT_ENVELOPE.log',outer['INDEPENDENT_ENVELOPE.log_sha256'],True))==envelope,'Independent envelope printed/result disagreement')
    observed=indexed(outer['external_inputs'],'id');need(set(observed)==set(external) and all(identity(observed[k])==identity(external[k]) for k in external),'Outer external input coverage')
    need(outer['public_files']==len(tested) and outer['logical_files']==len(mapped),'Outer input counts')
    need(main['schema']=='primitive357_integrated_replay_v1' and main['status']=='PASS_FRESH_INTEGRATED_REPLAY' and main['input_manifest']==expected_input,'Integrated replay input/status')
    components=indexed(main['components'],'id');need(set(components)==set(MARKERS),'Component coverage')
    for key,row in components.items():
        zero(row['exit_code'],key);text=artifact('suite/'+row['log'],row['sha256'],True)
        need(sum(line.strip()==MARKERS[key] for line in text.splitlines())==1,'Component completion marker: '+key)
    need(envelope['status']=='PASS_INDEPENDENT_REPLAY_ENVELOPE' and envelope['input_manifest']==expected_input,'Independent envelope input/status')
    need([envelope[k] for k in ('sectors','prior_jobs','rank_checks','fresh_rank_upstream_bindings')]==[13,65,16,5],'Independent envelope coverage')
    prior=parse(raw['prior_result']);sectors=parse(raw['sector_result']);rank=parse(raw['rank_result'])
    groups=EXPECTED_COVERAGE['prior_required_job_ids_by_group'];jobs=[j for v in groups.values() for j in v]
    need(prior['status']==MARKERS['prior'] and prior['groups']==list(groups) and main['prior_groups']==list(groups),'Prior group coverage')
    need(prior['fresh_replay'] is True and prior['all_required_prior_jobs_passed'] is True and type(prior['required_full_prior_job_count']) is int and prior['required_full_prior_job_count']==65 and type(prior['observed_successful_job_count']) is int and prior['observed_successful_job_count']==65,'Partial/resumed prior replay')
    prior_rows=exact_ids(prior['records'],'id',jobs,'Prior')
    for row in prior_rows.values():
        zero(row['exit_code'],row['id']);need(row['success'] is True,'Failed prior check')
        text=artifact('suite/prior/'+row['log'],row['log_sha256'],True);markers=row['required_markers']
        need(markers==EXPECTED_PRIOR_MARKERS[row['id']] and all(m in text for m in markers),'Prior completion marker contract')
        artifact('suite/prior/'+row['source'],row['source_sha256'])
    need(sectors['status']==MARKERS['sectors'],'Sector status')
    for row in exact_ids(sectors['records'],'id',EXPECTED_COVERAGE['sector_ids'],'Sector').values():
        zero(row['exit_code'],row['id']);text=artifact('suite/sectors/'+row['log'],row['sha256'],True)
        need(row['marker']==EXPECTED_SECTOR_MARKERS[row['id']] and row['marker'] in text,'Sector completion marker contract')
    need(rank['status']==MARKERS['rank_local'],'Rank-local status')
    for row in exact_ids(rank['fresh_checks'],'name',EXPECTED_COVERAGE['rank_check_names'],'Rank-local').values():
        zero(row['returncode'],row['name']);artifact('suite/rank_local/'+row['log'],row['log_sha256'],True)
    need(rank['conclusions']==main['rank_conclusions']==EXPECTED_COVERAGE['rank_conclusions'],'Rank conclusion join')
    need(set(rank['fresh_upstream_sha256'])==set(EXPECTED_COVERAGE['rank_upstream_relative_paths']),'Missing producer join')
    for name,digest in rank['fresh_upstream_sha256'].items():artifact('suite/prior/'+name,digest)
    need(rank['evidence_sha256'],'Missing rank evidence inputs')
    for name,digest in rank['evidence_sha256'].items():need(name in logical and logical[name]['sha256']==digest,'Rank evidence input join')
    for k,v in {'H0':['D2','D3','D4','D5'],'H1':['D2','E','D4','D5'],'relation':'5E=D3+D4+3D5'}.items():need(prior['subgroups'][k]==main['subgroups'][k]==v,'H0/H1 scope mismatch')
    # Bind the full retained result JSONs to their original output paths too.
    for role,name in [('externalized_result','EXTERNALIZED_REPLAY_RESULT.json'),('integrated_result','suite/REPLAY_RESULT.json'),('independent_envelope','INDEPENDENT_ENVELOPE.json'),('prior_result','suite/prior/PRIOR_REPLAY_RESULT.json'),('sector_result','suite/sectors/SECTOR_REPLAY_RESULT.json'),('rank_result','suite/rank_local/rank_local_results.json')]:artifact(name,sha(raw[role]))
    driver=parse(raw['isolated_driver']);need(driver.get('schema')=='primitive357-isolated-driver-v1' and driver['status']=='PASS_ISOLATED_DRIVER' and driver['output_did_not_exist'] is True,'Isolated driver schema/status/fresh output');zero(driver['exit_code'],'Isolated driver')
    for field,role in [('distribution_manifest_sha256','tested_public_manifest'),('logical_manifest_sha256','logical_manifest'),('sandbox_profile_sha256','isolation_profile'),('outer_log_sha256','driver_log')]:need(driver[field]==sha(raw[role]),'Isolated driver binding: '+field)
    cmd=driver['command'];need(isinstance(cmd,list) and all(isinstance(s,str) and s for s in cmd) and Path(cmd[0]).name=='sandbox-exec' and '-f' in cmd and any(Path(s).name=='replay_companion.py' for s in cmd),'Driver was not the isolated complete replay command')
    need(cmd.count('-f')==1 and cmd.index('-f')+1<len(cmd) and Path(cmd[cmd.index('-f')+1]).name==Path(records['isolation_profile']['archive_path']).name,'Driver profile path mismatch')
    need(driver['env'].get('PYTHONOPTIMIZE')=='0','Driver disabled Python assertions')
    need(timestamp(driver['started_utc'])<=timestamp(outer['started_utc'])<timestamp(outer['finished_utc'])<=timestamp(driver['finished_utc']),'Driver/outer time interval mismatch')
    marker='PASS_FRESH_EXTERNALIZED_COMPLETE_REPLAY';need(sum(marker in line for line in raw['driver_log'].decode().splitlines())==1,'Driver completion marker missing/repeated')
    need(parse(raw['driver_log'])==outer,'Isolated driver printed a different outer result')
    probes=parse(raw['isolation_probes']);need(probes['status']=='PASS_OFFLINE_ISOLATION_PROBES','Isolation probes failed');probe_rows=indexed(probes['checks'],'id')
    required={'allowed_distribution_read','allowed_logical_read','allowed_private_read','fresh_write_and_read','immutable_logical_write_denied','network_tcp_connect_denied','network_udp_send_denied','native_flint_execute_and_old_input_denied','ordinary_python_packages','sage_matrix','pari_gp','pdf_text_extractor','pdf_actual_text'}
    need(required<=set(probe_rows) and all(r.get('passed') is True for r in probe_rows.values()) and len([n for n in probe_rows if n.startswith('denied_read_')])>=3,'Isolation probe coverage/outcome')
    result={'status':'PASS_CURRENT_DISTRIBUTION_RECORD_BINDING','release_tag':tag,'asset':asset,'sectors':13,'prior_jobs':65,'rank_checks':16,'producer_joins':5,'archive_payloads_checked':False,'boundary':'Authenticates retained records and completion logs for the observed isolated run; not a new replay or independent mathematical proof.'}
    if archive is not None:
        archive=Path(archive)
        for q in (archive,*archive.parents):need(not q.is_symlink(),'Symlink archive path')
        need(archive.is_file() and stat.S_ISREG(archive.stat().st_mode),'Archive is not a regular file')
        data=archive.read_bytes();need(identity(asset)=={'bytes':len(data),'sha256':sha(data)},'Archive bytes differ from binding')
        expected={n:identity(r) for n,r in final.items()};expected['COMPANION_MANIFEST.json']={'bytes':len(raw['final_public_manifest']),'sha256':sha(raw['final_public_manifest'])}
        prefix=rel(binding['archive_root'])+'/'
        with zipfile.ZipFile(archive) as z:
            names={}
            for item in z.infolist():
                need(item.filename.startswith(prefix),'Archive root mismatch');name=item.filename[len(prefix):]
                mode=item.external_attr>>16
                if item.is_dir():
                    need(stat.S_IFMT(mode) in (0,stat.S_IFDIR),'Non-directory ZIP directory entry')
                    if name:rel(name.rstrip('/'))
                    continue
                rel(name);need(name not in names,'Duplicate ZIP member');need(stat.S_IFMT(mode) in (0,stat.S_IFREG),'Nonregular ZIP member')
                names[name]=item
            need(set(names)==set(expected),'ZIP exact member set differs from final manifest')
            for name,item in names.items():
                need(item.file_size==expected[name]['bytes'],'ZIP member size');need(sha(z.read(item))==expected[name]['sha256'],'ZIP member hash')
        result.update(status='PASS_CURRENT_DISTRIBUTION_ARCHIVE_AND_RECORD_BINDING',archive_payloads_checked=True)
    return result

if __name__=='__main__':
    import argparse,sys
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,required=True)
    p.add_argument('--status',default='audit/status.json')
    p.add_argument('--archive',type=Path)
    a=p.parse_args()
    try:
        path=a.root/rel(a.status)
        for q in (path,*path.parents):need(not q.is_symlink(),'Symlink status path')
        result=verify_current_distribution(a.root,parse(path.read_bytes()),a.archive)
        print(json.dumps(result,indent=2))
    except (OSError,ValueError,KeyError,TypeError,zipfile.BadZipFile) as exc:
        print('CURRENT_DISTRIBUTION_VERIFICATION=FAIL '+str(exc),file=sys.stderr)
        sys.exit(1)
