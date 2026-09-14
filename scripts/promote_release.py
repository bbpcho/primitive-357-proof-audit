#!/usr/bin/env python3
"""Review a real completed release promotion; write only with explicit --apply.

This does not run arithmetic, seal an archive, commit, upload, or publish.
A temporary proposal is fully validated before the selected control repository
is changed. All seven historical asset records must retain their identities.
"""
from __future__ import annotations
import argparse, copy, hashlib, json, os, shutil, stat, subprocess, sys, tempfile, zipfile
from pathlib import Path
from urllib.parse import quote
from verification_common import (asset_index, manifest_rows, read_json, regular_file,
    relative_path, require, sha256, unique_records)
import verify_repository as verifier
import select_final_artifacts as artifact_selector

HERE=Path(__file__).resolve().parent
TAG=verifier.TAG
PRIMARY=verifier.ASSET_ID
PAPER='PRIMITIVE_357_VERIFIED_MANUSCRIPT_2026_09_14'
RDIR='audit/verified-2026-09-14/'
ARCHIVE_NAME='PRIMITIVE_357_VERIFIED_RELEASE_2026-09-14_V1.zip'
HISTORICAL={'PRIMITIVE_357_REPRODUCIBILITY_V3','PRIMITIVE_357_ARXIV_UPLOAD_WITH_PROGRAMS_V3_ZIP','PRIMITIVE_357_ARXIV_UPLOAD_WITH_PROGRAMS_V3_TGZ','PRIMITIVE_357_PAPER_AND_RELEASE_GUIDE_V3','P5_LITERAL_C_OBSTRUCTION_DEPENDENCY_CLOSURE_V1','P23_B124_D4_UPSTREAM_RECONSTRUCTION_V1','CORRECTED66_PREDYADIC_AND_P2_PLACE2_DEPENDENCY_CLOSURE_V1'}
SECTOR_IDS=['v3_integrity_and_interfaces','signed-global-algebra','rational-factor-sector','quadratic-factor-router','quadratic-factor-terminal','cubic-quartic-section7-sector','rational-parameter-sieve-and-lifts','irreducible-septic-sector','hilbert-hecke-filter-coverage','hilbert-hecke-ambient-coverage','putz-pvt-interface','independent_hecke_input_foundations','independent_fano_resolvent_foundation']

VERIFICATION_METADATA={'README.md','TESTED_RELEASE_MANIFEST.json','PROOF_INPUTS_SHA256.json',
    'ARTIFACT_SELECTION.json','INTEGRATED_REPLAY.log','HOST_ENVIRONMENT.json',
    'ASSET_CONSTRUCTION.json','tools/append_verification_records.py','tools/select_final_artifacts.py'}

def dump(value):return (json.dumps(value,indent=2,ensure_ascii=False)+'\n').encode()
def regular_input(path):
    require(path.is_file() and not path.is_symlink(),'input must be a regular file: '+str(path))
    return path.resolve()
def checked_zip(archive, final_manifest, rows, records=False):
    """Read every ZIP member and check the exact final manifest, without extraction."""
    with zipfile.ZipFile(archive) as z:
        infos=z.infolist();require(bool(infos),'empty archive')
        names=set();prefixes=set();entries={}
        for info in infos:
            name=info.filename;trim=name[:-1] if info.is_dir() else name
            rel=relative_path(trim)
            require(name not in names,'duplicate ZIP entry: '+name);names.add(name)
            require(len(rel.parts)>1,'archive must have one enclosing directory')
            prefixes.add(rel.parts[0]);mode=(info.external_attr>>16)&0xffff
            require(not stat.S_ISLNK(mode),'ZIP symlink: '+name)
            require(not info.flag_bits&1,'encrypted ZIP member: '+name)
            if info.is_dir():
                require(not stat.S_IFMT(mode) or stat.S_ISDIR(mode),'invalid ZIP directory mode')
                continue
            require(not stat.S_IFMT(mode) or stat.S_ISREG(mode),'nonregular ZIP member: '+name)
            inner='/'.join(rel.parts[1:]);require(inner not in entries,'duplicate payload path')
            entries[inner]=info
        require(len(prefixes)==1,'ZIP has multiple enclosing directories')
        require(set(entries)==set(rows)|{'RELEASE_MANIFEST.json'},'ZIP payload does not equal the final manifest')
        require(z.read(entries['RELEASE_MANIFEST.json'])==final_manifest.read_bytes(),'embedded final manifest differs')
        for name,row in rows.items():
            info=entries[name];require(info.file_size==row['bytes'],'ZIP member size mismatch: '+name)
            h=hashlib.sha256()
            with z.open(info) as f:
                for block in iter(lambda:f.read(1048576),b''):h.update(block)
            require(h.hexdigest()==row['sha256'],'ZIP member digest mismatch: '+name)
        contract_name='audit/work/integration_prior/REQUIRED_PRIOR_EVIDENCE.json'
        require(contract_name in entries,'missing prior required-job contract')
        metadata={}
        if records:
            for name in ('ARTIFACT_SELECTION.json','TESTED_RELEASE_MANIFEST.json',
                         'PROOF_INPUTS_SHA256.json','ASSET_CONSTRUCTION.json'):
                key='verification/'+name
                require(key in entries,'missing archived verification record: '+name)
                metadata[name]=z.read(entries[key])
        return json_bytes(z.read(entries[contract_name])),metadata

def json_bytes(content):
    def pairs(items):
        result={}
        for key,value in items:
            require(key not in result,'duplicate JSON key: '+key);result[key]=value
        return result
    return json.loads(content.decode('utf-8'),object_pairs_hook=pairs)

def checked_record_join(replay,tested_path,tested_rows,final_rows,metadata,
                        candidate_archive,driver_log,host_record,result,prior,sectors,rank):
    """Bind all retained outputs, using local trusted code, never code from a ZIP.

    The selector uses the candidate only as a manifest lookup. Its temporary
    reference directory therefore needs just the already authenticated manifest;
    checked_zip has independently checked every candidate payload against it.
    """
    require(not any(n.startswith('verification/') for n in tested_rows),
            'tested candidate already contains final verification records')
    require(metadata['TESTED_RELEASE_MANIFEST.json']==tested_path.read_bytes(),
            'archived tested manifest differs from the actual tested manifest')
    proof={'schema':'primitive357_proof_inputs_v1','release_tag':TAG,
           'files':[{k:row[k] for k in ('path','sha256','bytes')} for row in tested_rows.values()]}
    require(metadata['PROOF_INPUTS_SHA256.json']==dump(proof),
            'archived proof-input index differs from the exact tested inputs')
    with tempfile.TemporaryDirectory(prefix='primitive357-selection-reference-') as temp:
        reference=Path(temp);(reference/'RELEASE_MANIFEST.json').write_bytes(tested_path.read_bytes())
        try:selection=artifact_selector.select_final_artifacts(replay,reference)
        except RuntimeError as exc:raise ValueError('fresh artifact selection failed: '+str(exc)) from exc
    require(json_bytes(metadata['ARTIFACT_SELECTION.json'])==selection,
            'archived artifact selection differs from the complete fresh output selection')
    selected=unique_records(selection['files'],'path')
    excluded={row['path']:row for row in selection['excluded']}
    require(not (set(selected)&VERIFICATION_METADATA)
            and all(n!='tools' and not n.startswith('tools/') for n in selected),
            'fresh output collides with assembly-owned verification records')
    expected=set(tested_rows)|{'verification/'+n for n in set(selected)|VERIFICATION_METADATA}
    require(set(final_rows)==expected,'final archive additions differ from the exact retained records')
    for name,row in selected.items():
        archived=final_rows['verification/'+name]
        require(all(archived[k]==row[k] for k in ('sha256','bytes')),
                'archived fresh output differs from the actual replay: '+name)
    def bind_file(name,path):
        row=final_rows['verification/'+name]
        require(row['bytes']==path.stat().st_size and row['sha256']==sha256(path),
                'archived external record differs: '+name)
    bind_file('INTEGRATED_REPLAY.log',driver_log)
    bind_file('HOST_ENVIRONMENT.json',host_record)
    bind_file('tools/select_final_artifacts.py',HERE/'select_final_artifacts.py')
    require(sum(line.strip()=='PASS_FRESH_INTEGRATED_REPLAY'
                for line in driver_log.read_text().splitlines())==1,
            'driver log lacks one unique integrated success marker')
    construction=json_bytes(metadata['ASSET_CONSTRUCTION.json'])
    require(construction.get('schema')=='primitive357_verified_asset_construction_v1'
            and construction.get('release_tag')==TAG,'wrong asset construction record')
    require(construction.get('tested_manifest')==result['input_manifest'],
            'asset construction refers to different tested inputs')
    require(construction.get('tested_candidate_archive')==
            {'sha256':sha256(candidate_archive),'bytes':candidate_archive.stat().st_size},
            'asset construction refers to a different candidate archive')
    require(construction.get('scope')==result.get('retained_premises'),
            'asset construction changes the retained-premise boundary')
    mandatory={'REPLAY_RESULT.json','RUNTIME_VERSIONS.json','prior/PRIOR_REPLAY_RESULT.json',
               'sectors/SECTOR_REPLAY_RESULT.json','rank_local/rank_local_results.json',
               'sectors/logs/independent_fano_resolvent_foundation.log'}
    require(mandatory<=set(selected),'required fresh report, runtime or Fano log is missing')
    runtime=read_json(regular_file(replay,'RUNTIME_VERSIONS.json'))
    require(all(isinstance(runtime.get(k),str) and runtime[k].strip()
                for k in ('ordinary_python','sage','pari_gp','pdf_text_extractor')),
            'runtime record omits a required tool, including pdftotext')
    # Every reported actual job log is bound as well as the full selection.
    # An identical historical copy may be referenced through a tested input,
    # but only when the independently recomputed selector establishes equality.
    def bind_job_log(prefix,row,key):
        name=prefix+relative_path(row['log']).as_posix()
        path=regular_file(replay,name)
        require(sha256(path)==row[key],'actual job log changed: '+name)
        if name not in selected:
            old=excluded.get(name,{})
            require(old.get('reason')=='identical_sealed_input_copy'
                    and old.get('sha256')==row[key]
                    and old.get('candidate_path') in tested_rows,
                    'actual job log is not retained or bound to an identical tested input: '+name)
    for row in result['components']:bind_job_log('',row,'sha256')
    for row in prior['records']:bind_job_log('prior/',row,'log_sha256')
    for row in sectors['records']:bind_job_log('sectors/',row,'sha256')
    for row in unique_records(rank['fresh_checks'],'name').values():
        require(type(row.get('returncode')) is int and row['returncode']==0,
                'actual rank job failed')
        bind_job_log('rank_local/',row,'log_sha256')
    fano=unique_records(sectors['records'])['independent_fano_resolvent_foundation']
    require(fano['log']=='logs/independent_fano_resolvent_foundation.log',
            'Fano foundation log has an unexpected identity')
    return {'selected_fresh_files':len(selected),'selected_fresh_bytes':selection['selected_bytes'],
            'artifact_selection_sha256':final_rows['verification/ARTIFACT_SELECTION.json']['sha256'],
            'candidate_archive_sha256':sha256(candidate_archive),
            'all_archived_fresh_outputs_match_actual_replay':True}


def snapshot_manifest(root):
    previous=verifier.ROOT;verifier.ROOT=root
    try:names=sorted(verifier.inventory())
    finally:verifier.ROOT=previous
    return ''.join(sha256(regular_file(root,name))+'  '+name+'\n' for name in names).encode()

def run_check(command,cwd):
    done=subprocess.run(command,cwd=cwd,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
    require(done.returncode==0,'proposal validation failed:\n'+done.stdout)
    return {'command':command,'exit_code':done.returncode,'output':done.stdout.strip()}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for flag in ('control-root','final-replay','tested-manifest','final-archive','final-manifest','paper-pdf','workspace-root','candidate-archive','driver-log','host-record'):
        p.add_argument('--'+flag,type=Path,required=True)
    p.add_argument('--review-output',type=Path,help='optional new JSON review file, outside the control repository')
    p.add_argument('--apply',action='store_true',help='apply validated changes; default only reviews in a temporary copy')
    a=p.parse_args();control=a.control_root.resolve();replay=a.final_replay.resolve();workspace=a.workspace_root.resolve()
    require(control.is_dir() and replay.is_dir() and workspace.is_dir(),'missing input directory')
    previous=verifier.ROOT;verifier.ROOT=control
    try:verifier.inventory()  # Reject symlink directories before copying/writing the temporary proposal.
    finally:verifier.ROOT=previous
    control_before=snapshot_manifest(control)
    old_manifest=sha256(regular_file(control,verifier.MANIFEST))
    tested_path=regular_input(a.tested_manifest);final_path=regular_input(a.final_manifest)
    archive=regular_input(a.final_archive);pdf=regular_input(a.paper_pdf)
    candidate_archive=regular_input(a.candidate_archive)
    driver_log=regular_input(a.driver_log);host_record=regular_input(a.host_record)
    require(archive.name==ARCHIVE_NAME,'unexpected new archive basename')
    require(pdf.suffix.lower()=='.pdf' and pdf.open('rb').read(5)==b'%PDF-','paper input is not a PDF')
    for f in ('verify_repository.py','verify_assets.py','verification_common.py','test_verifiers.py',
              'promote_release.py','test_promotion.py','select_final_artifacts.py'):
        require(sha256(regular_file(control,'scripts/'+f))==sha256(HERE/f),'control verifier is not synchronized: '+f)
    current_assets=asset_index(control);byid=unique_records(current_assets)
    require(HISTORICAL<=set(byid) and set(byid)<=HISTORICAL|{PRIMARY,PAPER},'unexpected historical asset identity set')
    historical={key:copy.deepcopy(byid[key]) for key in HISTORICAL}
    status=read_json(regular_file(control,'audit/status.json'))
    require(status.get('release_tag')==TAG and status.get('release_state') in ('pending_fresh_replay','verified'),'wrong target release status')
    tested=read_json(tested_path);final=read_json(final_path)
    tested_rows=manifest_rows(tested);final_rows=manifest_rows(final)
    require(tested.get('release_tag')==final.get('release_tag')==TAG,'tested/final manifest tag mismatch')
    for name,row in tested_rows.items():
        require(name in final_rows and all(final_rows[name][k]==row[k] for k in ('path','sha256','bytes')),'tested input changed or missing: '+name)
    pdfrow=final_rows.get('paper/manuscript.pdf')
    require(pdfrow is not None and pdfrow['sha256']==sha256(pdf) and pdfrow['bytes']==pdf.stat().st_size,'separate PDF differs from the tested manuscript')
    require(tested_rows.get('paper/manuscript.pdf')==pdfrow,'paper PDF was not part of the tested inputs')
    for name in ('paper/manuscript.tex','paper/rank-proof.tex','paper/manuscript.pdf'):
        path=regular_file(control,name)
        require(name in tested_rows and sha256(path)==tested_rows[name]['sha256']
                and path.stat().st_size==tested_rows[name]['bytes'],'control manuscript differs from the tested paper: '+name)
    checked_zip(candidate_archive,tested_path,tested_rows)
    contract,metadata=checked_zip(archive,final_path,final_rows,records=True)
    require('audit/work/integration_prior/REQUIRED_PRIOR_EVIDENCE.json' in tested_rows,
            'prior required-job contract was not a tested input')
    result_path=regular_file(replay,'REPLAY_RESULT.json');result=read_json(result_path)
    require(result.get('schema')=='primitive357_integrated_replay_v1' and result.get('status')=='PASS_FRESH_INTEGRATED_REPLAY','actual integrated replay did not pass')
    require(result.get('input_manifest')=={'files':len(tested_rows),'manifest_sha256':sha256(tested_path)},'actual replay manifest differs')
    prior=read_json(regular_file(replay,'prior/PRIOR_REPLAY_RESULT.json'))
    require(prior.get('status')=='PASS_SELECTED_PRIOR_GROUPS' and prior.get('groups')==verifier.PRIOR_GROUPS,'actual prior groups incomplete')
    expected_jobs={name for group in verifier.PRIOR_GROUPS for name in contract['required_job_ids_by_group'][group]}
    jobs=unique_records(prior['records'])
    require(set(jobs)==expected_jobs and prior.get('required_full_prior_job_count')==len(expected_jobs),'actual prior job coverage incomplete')
    require(prior.get('fresh_replay') is True and prior.get('all_required_prior_jobs_passed') is True,'actual prior run was not fresh and complete')
    require(all(row.get('success') is True and type(row.get('exit_code')) is int and row['exit_code']==0 for row in jobs.values()),'actual prior job failed')
    sectors=read_json(regular_file(replay,'sectors/SECTOR_REPLAY_RESULT.json'))
    sector_rows=unique_records(sectors['records'])
    require(sectors.get('status')=='PASS_FRESH_TEN_SECTORS_AND_INTERFACES' and list(sector_rows)==SECTOR_IDS,'actual sector coverage incomplete')
    require(all(type(row.get('exit_code')) is int and row['exit_code']==0 for row in sector_rows.values()),'actual sector job failed')
    rank=read_json(regular_file(replay,'rank_local/rank_local_results.json'))
    require(rank.get('status')=='PASS_FRESH_RANK_LOCAL_COMPONENT' and rank['conclusions'].get('equals_B_plus_literal_c') is True,'actual rank join failed')
    require(result['rank_conclusions']==rank['conclusions'],'integrated/local rank conclusions disagree')
    record_join=checked_record_join(replay,tested_path,tested_rows,final_rows,metadata,
        candidate_archive,driver_log,host_record,result,prior,sectors,rank)
    proposed={RDIR+'REPLAY_RESULT.json':result_path.read_bytes(),RDIR+'TESTED_RELEASE_MANIFEST.json':tested_path.read_bytes(),RDIR+'FINAL_RELEASE_MANIFEST.json':final_path.read_bytes()}
    components=unique_records(result['components'])
    require(set(components)=={'prior','rank_local','sectors'},'integrated component coverage')
    for name,row in components.items():
        log=regular_file(replay,row['log']);require(sha256(log)==row['sha256'],'actual component log changed: '+name)
        proposed[RDIR+row['log']]=log.read_bytes()
    proof={'schema':'primitive357_proof_inputs_v1','release_tag':TAG,'files':[{k:row[k] for k in ('path','sha256','bytes')} for row in tested_rows.values()]}
    proposed[RDIR+'PROOF_INPUTS_SHA256.json']=dump(proof)
    assets=copy.deepcopy(current_assets)
    for key,path,role in ((PRIMARY,archive,'integrated verified proof and dependency-closed independent replay'),(PAPER,pdf,'separate compiled manuscript identical to the tested archive PDF')):
        try:source=path.relative_to(workspace).as_posix()
        except ValueError:raise ValueError('asset lies outside --workspace-root: '+str(path))
        item={'id':key,'filename':path.name,'sha256':sha256(path),'bytes':path.stat().st_size,'source_path_from_workspace':source,
              'github_release':status['github_repository']+'/releases/tag/'+TAG,
              'download_url':status['github_repository']+'/releases/download/'+TAG+'/'+quote(path.name),'role':role,'audit_state':'verified_fresh_integrated_replay'}
        if key in byid:
            require(all(byid[key][k]==item[k] for k in ('id','filename','sha256','bytes','source_path_from_workspace')),'refuse to alter an existing release asset identity: '+key)
        else:assets.append(item)
    after=unique_records(assets)
    require(all(after[key]==value for key,value in historical.items()),'historical asset record changed')
    index=read_json(regular_file(control,'evidence/assets.json'));index['assets']=assets
    proposed['evidence/assets.json']=dump(index)
    proposed['evidence/checksums/RELEASE_ASSETS_SHA256.txt']=''.join(f"{x['sha256']}  {x['filename']}\n" for x in assets).encode()
    binding={'schema':'primitive357_replay_binding_v1','release_tag':TAG,'asset_id':PRIMARY,'asset_sha256':after[PRIMARY]['sha256'],'asset_bytes':after[PRIMARY]['bytes']}
    for key,name in [('replay_result','REPLAY_RESULT.json'),('tested_manifest','TESTED_RELEASE_MANIFEST.json'),('proof_inputs','PROOF_INPUTS_SHA256.json'),('final_manifest','FINAL_RELEASE_MANIFEST.json')]:
        path=RDIR+name;binding[key]={'path':path,'sha256':hashlib.sha256(proposed[path]).hexdigest()}
    proposed[RDIR+'REPLAY_BINDING.json']=dump(binding)
    status.update(release_state='verified',proof_complete=True,public_proof_release_authorized=True,
        blocking_gate=None,fresh_replay={'state':'pass','binding':RDIR+'REPLAY_BINDING.json'},
        verification_boundary='The mathematical audit and fresh integrated replay of the exact sealed inputs are complete. Published results and the explicitly identified historical Magma computations remain imported premises; no fresh Magma execution or proof-assistant formalization is claimed. The replay binding records the tested inputs, final archive and unchanged manuscript identities.')
    for gate in status['gates']:
        if gate['id'] in ('fresh_integrated_replay','public_proof_release'):
            gate.update(state='pass',evidence=RDIR+'REPLAY_BINDING.json')
    proposed['audit/status.json']=dump(status)
    # Existing final records are immutable. Repeating an identical promotion is
    # allowed, but a changed record under this release identity is not.
    for name,content in proposed.items():
        if name.startswith(RDIR) and (control/name).exists():
            require(regular_file(control,name).read_bytes()==content,'refuse to overwrite a different sealed audit record: '+name)
    with tempfile.TemporaryDirectory(prefix='primitive357-promotion-') as temp:
        proposal=Path(temp)/'control'
        def ignore(path,names):return ['.git','build'] if Path(path)==control else []
        shutil.copytree(control,proposal,ignore=ignore,symlinks=True)
        for name,content in proposed.items():
            path=proposal/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(content)
        proposed[verifier.MANIFEST]=snapshot_manifest(proposal);(proposal/verifier.MANIFEST).write_bytes(proposed[verifier.MANIFEST])
        checks=[]
        for mode in ([],['-O'],['-OO']):checks.append(run_check([sys.executable,'-B',*mode,str(proposal/'scripts/verify_repository.py')],proposal))
        checks.append(run_check([sys.executable,'-B',str(proposal/'scripts/verify_assets.py'),'--workspace-root',str(workspace),'--asset-id',PRIMARY,'--asset-id',PAPER],proposal))
        plan={'schema':'primitive357_promotion_review_v1','release_tag':TAG,'mode':'APPLY' if a.apply else 'DRY_REVIEW','actual_replay_status':result['status'],'tested_input_count':len(tested_rows),'final_file_count':len(final_rows),'prior_job_count':len(jobs),'sector_job_count':len(sector_rows),'archived_record_join':record_join,'historical_asset_records_preserved':7,'new_assets':[after[PRIMARY],after[PAPER]],'changed_control_files':[{'path':n,'bytes':len(c),'sha256':hashlib.sha256(c).hexdigest()} for n,c in sorted(proposed.items())],'validation':checks,'no_commit_upload_or_publication':True}
        if a.review_output:
            review=a.review_output.absolute();require(control!=review and control not in review.parents,'review output must be outside the control repository')
            require(not review.exists(),'refuse to overwrite review output');review.parent.mkdir(parents=True,exist_ok=True);review.write_bytes(dump(plan))
        print(json.dumps(plan,indent=2))
        if a.apply:
            require(sha256(regular_file(control,verifier.MANIFEST))==old_manifest,'control manifest changed during proposal validation')
            # Compare the full starting file set, including newly copied scripts.
            # Its previous manifest may be stale; this utility regenerates it.
            require(snapshot_manifest(control)==control_before,'control files changed during proposal validation')
            order=[n for n in sorted(proposed) if n not in ('audit/status.json',verifier.MANIFEST)]+['audit/status.json',verifier.MANIFEST]
            for name in order:
                dest=control/name;dest.parent.mkdir(parents=True,exist_ok=True)
                fd,tmp=tempfile.mkstemp(prefix='.promotion-',dir=dest.parent)
                with os.fdopen(fd,'wb') as f:f.write(proposed[name])
                os.replace(tmp,dest)
            run_check([sys.executable,'-B',str(control/'scripts/verify_repository.py')],control)
            print('PASS_APPLIED_VERIFIED_RELEASE_PROMOTION')
        else:print('PASS_DRY_REVIEW_NO_CONTROL_FILES_CHANGED')

if __name__=='__main__':
    try:main()
    except (OSError,ValueError,KeyError,TypeError,zipfile.BadZipFile) as e:
        print('RELEASE_PROMOTION_FAILED: '+str(e),file=sys.stderr);sys.exit(1)
