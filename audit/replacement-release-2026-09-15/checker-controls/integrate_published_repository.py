#!/usr/bin/env python3
"""Stage, then optionally install, observed postpublication repository records.

Default mode stages a reviewable overlay outside R. --apply is deliberately
separate. No tracked-manifest regeneration, commit, tag change or push occurs.
"""
from pathlib import Path
import argparse, copy, hashlib, json, os, shutil, stat, sys, tempfile

N = Path(__file__).resolve().parent
R_DEFAULT = N.parent / 'pre_submission_revision_2026_09_15/repository'
sys.path.insert(0, str(N));sys.path.insert(0, str(N / 'outer_tools'))
import prepare_publication_records as prep
from companion_common import verify_distribution
from verify_current_publication import verify_current_publication

BASE = prep.BASE
PFX = 'records/completed-replay/'
DOCS = ('README.md', 'NOTICE.md', 'docs/PROOF_STATUS.md', 'docs/EVIDENCE.md',
        'docs/GITHUB_SETUP.md', 'docs/RELEASE_PROCESS.md',
        'release/PROGRAMS_AND_CERTIFICATES.md', 'release/VERIFIED_RELEASE_2026-09-14.md')
HISTORICAL_READMES = (
    'audit/dahmen-removal-2026-09-15/README.md',
    'audit/first-submission-2026-09-15/README.md',
    'audit/reviewer-corrections-2026-09-15/README.md',
    'audit/pre-submission-2026-09-15/README.md',
    'audit/ai-disclosure-2026-09-15/README.md',
)
ASSET_IDS = {'companion': 'PRIMITIVE_357_REPLAY_COMPANION_2026_09_15_V2',
             'paper_pdf': 'PRIMITIVE_357_PETER_CHOCIAN_SUBMISSION_2026_09_15_V2',
             'source_zip': 'PRIMITIVE_357_ARXIV_SOURCE_2026_09_15_V2'}
OLD_INDEX_IDS = {561595084: 'P5_LITERAL_C_OBSTRUCTION_DEPENDENCY_CLOSURE_V1',
                 561674379: 'CORRECTED66_PREDYADIC_AND_P2_PLACE2_DEPENDENCY_CLOSURE_V1'}
need, load, identity, encoded = prep.need, prep.load, prep.identity, prep.encoded

def file_bytes(path):
    return prep.path_checked(path).read_bytes()

def identical(path, row):
    prep.checked_identity(row, path)

def relative_to_workspace(path):
    return prep.relative(prep.path_checked(path).relative_to(N.parent.parent).as_posix())

def safe_target(root, name):
    target=root/prep.relative(name)
    for path in [*reversed(target.parents),target]:
        if not path.is_relative_to(root):continue
        need(not path.is_symlink(),'Symlink in planned target: '+str(path))
        if path.exists():
            mode=path.lstat().st_mode
            need(stat.S_ISREG(mode) if path==target else stat.S_ISDIR(mode),'Non-regular planned target: '+str(path))
    return target

def compact_mirror(root, merged):
    """Copy only records required by the current checker, never R/.git."""
    for name in ('paper', 'release', BASE):
        source = prep.path_checked(root / name, directory=True)
        prep.copy_tree_checked(source, merged / name)

def stage_and_validate(a):
    root = prep.path_checked(a.root, directory=True)
    records = prep.path_checked(a.publication_records, directory=True)
    out = Path(os.path.abspath(a.output))
    need(not out.exists() and not out.is_symlink(), 'Staging destination must be new')
    prep.path_checked(out.parent, directory=True)
    need(not out.is_relative_to(root) and not root.is_relative_to(out), 'Stage must be outside the repository')
    need(not out.is_relative_to(records) and not records.is_relative_to(out), 'Stage and publication records must be disjoint')

    final, paper, extraction = (load(N / name) for name in
        ('FINAL_ARCHIVE_IDENTITY.json', 'FINAL_PAPER_BUILD.json', 'FINAL_EXTRACTION_EQUIVALENCE.json'))
    need(final['status'] == 'PASS_FINAL_APPEND_ONLY_COMPANION' and final['release_tag'] == prep.TAG and
         final['name'] == prep.NAMES['companion'], 'Final companion is not sealed for this release')
    archive = prep.path_checked(N / 'final' / final['name']);identical(archive, final)
    need(paper['status'] == 'PASS_PAPER_BUILD_AND_CLEAN_SOURCE_REBUILD' and
         paper['visual_review'] == 'PASS_VISUAL_REVIEW' and paper['companion'] == final and
         paper['arxiv_submitted'] is False, 'Paper build or visual review incomplete')
    need(extraction['status'] == 'PASS_FRESH_FINAL_EXTRACTION_AND_EXACT_INPUT_EQUIVALENCE' and
         extraction['archive'] == final, 'Final extraction not bound to this archive')
    extracted = N / 'final_extraction/distribution' / final['name'].removesuffix('.zip')
    verified_distribution = verify_distribution(extracted)[0]
    need(verified_distribution['distribution_manifest_sha256'] == final['final_public_manifest_sha256'] and
         verified_distribution['logical_manifest_sha256'] == final['logical_manifest_sha256'], 'Fresh final extraction identities changed')
    need(prep.sha(N / 'FINAL_EXTRACTED_PUBLIC_CONTENTS_SCAN.json') == extraction['public_scan_sha256'] and
         load(N / 'FINAL_EXTRACTED_PUBLIC_CONTENTS_SCAN.json')['status'] == 'PASS_PUBLIC_CONTENTS_SCAN', 'Final public scan binding failed')

    observation, withdrawal = (load(N / name) for name in
        ('FULL_PUBLIC_DOWNLOAD_OBSERVATION.json', 'OLD_ASSET_WITHDRAWAL_OBSERVATION.json'))
    observed = prep.validate_observation(observation, N / 'public_downloads')
    prep.validate_withdrawal(withdrawal, observation['checked_utc'])
    prepared_commit = load(N / 'PREPARED_REPOSITORY_COMMIT.json')
    need(prepared_commit['commit'] == observation['tag_commit'], 'Release tag does not identify the prepared commit')
    receipt = load(records / 'PUBLICATION_RECORD_PREPARATION.json')
    need(receipt['status'] == 'PASS_STAGED_PUBLICATION_RECORDS' and
         receipt['publication_check']['status'] == 'PASS_CURRENT_PUBLICATION_OFFLINE_BINDING' and
         receipt['repository_modified'] is False and receipt['github_modified'] is False,
         'Publication record preparation did not pass')
    actual_inputs = {'final_archive_identity': identity(N / 'FINAL_ARCHIVE_IDENTITY.json'),
        'paper_build': identity(N / 'FINAL_PAPER_BUILD.json'),
        'public_download_observation': identity(N / 'FULL_PUBLIC_DOWNLOAD_OBSERVATION.json'),
        'withdrawal_observation': identity(N / 'OLD_ASSET_WITHDRAWAL_OBSERVATION.json')}
    need(receipt['input_identities'] == actual_inputs, 'Prepared records identify different observations/builds')
    prospective = load(records / 'PROSPECTIVE_STATUS.json')
    need(prospective['current_publication'] == receipt['record_rows'] == load(records / 'PROSPECTIVE_CURRENT_PUBLICATION.json'),
         'Prospective publication object mismatch')
    need(prospective['arxiv_submission_ready'] is False and prospective['arxiv_submission_made'] is False and
         prospective['arxiv_submission_holds'] == ['Requested Dahmen reply pending'], 'Unsupported submission state')
    before_status = load(root / 'audit/status.json');original_status = load(N / 'STATUS_BEFORE_REPLACEMENT.json')
    for folder,name in [('current_binding','verify_current_distribution.py'),
                        ('current_binding','current_replay_coverage.py'),
                        ('publication_checker','verify_current_publication.py')]:
        need(prep.sha(root/'scripts'/name)==prep.sha(N/folder/name),'Installed checker differs from reviewed implementation: '+name)
    preserve = load(N / 'repo_docs/STATUS_INTEGRATION_PLAN.json')['preserve_historical_status_fields']
    for key in preserve:
        need(before_status[key] == original_status[key] == prospective[key], 'Historical status field changed: ' + key)
    need(before_status['current_publication'] == {'state': 'pending'}, 'Repository must be the prepared pending snapshot')
    need((root / BASE / 'PREPUBLICATION_PREPARATION.json').is_file(), 'Phase-A preparation is not installed')
    for name, digest in paper['paper'].items():
        need(name in ('manuscript.tex', 'rank-proof.tex', 'manuscript.pdf') and
             prep.sha(root / 'paper' / name) == prep.sha(N / 'final_paper' / name) == digest,
             'Installed paper differs from final build')
    identical(root / 'release' / paper['source_bundle']['filename'], paper['source_bundle'])

    changes = {}
    def add(name, data):
        name = prep.relative(name)
        need(name not in changes, 'Duplicate planned target: ' + name)
        changes[name] = data
    def add_file(source, name):add(name, file_bytes(source))
    for role in ('paper_revision', 'publication', 'public_access'):
        row = prospective['current_publication'][role]
        need(row['path'] == BASE + '/' + {'paper_revision':'PAPER_REVISION.json',
             'publication':'PUBLICATION.json','public_access':'PUBLIC_ACCESS_CHECK.json'}[role], 'Unexpected publication record target')
        identical(records / row['path'], row);add_file(records / row['path'], row['path'])
    revision = load(records / BASE / 'PAPER_REVISION.json')
    need(revision['preparation_input_identities'] == actual_inputs, 'Revision provenance differs from actual inputs')
    for name in ('FULL_PUBLIC_DOWNLOAD_OBSERVATION.json', 'OLD_ASSET_WITHDRAWAL_OBSERVATION.json',
                 'PREPARED_REPOSITORY_COMMIT.json', 'FINAL_ARCHIVE_IDENTITY.json',
                 'FINAL_EXTRACTION_EQUIVALENCE.json', 'FINAL_EXTRACTED_PUBLIC_CONTENTS_SCAN.json',
                 'FINAL_PAPER_BUILD.json', 'FINAL_PDF_VISUAL_REVIEW.json', 'RELEASE_ASSET_SET.json',
                 'PRE_WITHDRAWAL_LOCAL_PRESERVATION.json', 'PRE_WITHDRAWAL_RELEASE13.json'):
        add_file(N / name, BASE + '/' + name)
    add_file(records / 'PUBLICATION_RECORD_PREPARATION.json', BASE + '/PUBLICATION_RECORD_PREPARATION.json')
    for name, row in observation['api_records'].items():
        identical(N / 'public_downloads' / name, row)
        add_file(N / 'public_downloads' / name, BASE + '/public-observations/' + name)

    source_index = load(N / 'repo_docs/POSTPUBLICATION_SOURCE_INDEX.json')
    expected_sources = {'repo_docs/' + name: name for name in DOCS}
    expected_sources['repo_docs/FINAL_COMPANION_REPLAY_GUIDE.md'] = 'release/FINAL_COMPANION_REPLAY_GUIDE.md'
    source_rows = prep.indexed(source_index['files'], 'path')
    need(set(source_rows) == set(expected_sources), 'Reviewed document allowlist mismatch')
    for source, target in expected_sources.items():
        row = source_rows[source]
        need(row['destination'] == target, 'Reviewed document destination mismatch')
        identical(N / source, row);add_file(N / source, target)
    guide = N / 'repo_docs/FINAL_COMPANION_REPLAY_GUIDE.md'
    identical(guide, observed['replay_guide'])
    need(prep.sha(guide) == prep.sha(extracted / PFX / 'FINAL_COMPANION_REPLAY_GUIDE.md'), 'Guide differs from final companion')

    supplemental = [
        'supplemental/adapted-readers/supplemental_clean2/attempt2/SUPPLEMENTAL_RESULTS.json',
        'supplemental/adapted-readers/supplemental_clean2/attempt3/SUPPLEMENTAL_RESULTS.json',
        'supplemental/v5/SUPPLEMENTAL_V5_FINAL_RESULT.json',
        'supplemental/v5/COMPLETED_RECORD_REVIEW.json',
        'supplemental/v5/TOTAL_COUNT_ERRATUM.md',
        'sector-review/SECTOR_REVIEW.md',
    ]
    for name in supplemental:add_file(extracted / PFX / name, BASE + '/' + name)
    supplemental_results = [load(extracted / PFX / name) for name in supplemental[:2]]
    for name,result in zip(supplemental[:2],supplemental_results):
        for row in result['records']:
            log_name=(Path(name).parent/prep.relative(row['log'])).as_posix()
            log_path=extracted/PFX/log_name
            need(prep.sha(log_path)==row['log_sha256'],'Supplemental reader log identity mismatch')
            add_file(log_path,BASE+'/'+log_name)
    readers = [row for result in supplemental_results for row in result['records']]
    need({row['id'] for row in readers} == {'v2','v3','v4','v6'} and len(readers) == 4 and
         all(row['status']=='PASS_FRESH_LEAF_REPLAY' and row['exit_code']==0 and row['timed_out'] is False and
             row['diagnostics_detected'] is False and row['marker_count']==1 for row in readers), 'Supplemental reader checks incomplete')
    v5 = load(extracted / PFX / supplemental[2])
    need(v5['status']=='PASS_V5_EXACT_SUPPORT_COMPARISONS_WITH_TOTAL_LABEL_CORRECTION' and
         v5['exit_code']==0 and v5['exact_set_matches']==8 and v5['missing_rows']==v5['extra_rows']==0 and
         v5['independently_counted_support_rows']==237182 and v5['raw_reported_support_rows']==236182 and
         sum(v5['per_table_support_rows'].values())==237182, 'V5 supplement or erratum mismatch')
    for key in ('raw_run','raw_log','count_review'):
        row=v5[key];name='supplemental/v5/'+prep.relative(row['path']);source=extracted/PFX/name
        identical(source,row)
        if BASE+'/'+name in changes:need(changes[BASE+'/'+name]==file_bytes(source),'Duplicate V5 record mismatch')
        else:add_file(source,BASE+'/'+name)

    status = copy.deepcopy(prospective)
    status.update(as_of=observation['checked_utc'][:10], github_visibility='public',
        current_candidate='Current first-submission manuscript and published replacement companion with a fresh complete isolated replay',
        verification_boundary='The current replacement has a bound fresh isolated 13-sector/interface, 65-prior-job, 16-rank-local-check replay with five fresh input joins. The main irreducible-sector mode is DEEP_REPLAY=0; five default adapted-reader checks passed separately. V5 has eight exact support-table equalities totaling 237182 rows; the historical aggregate 236182 is corrected by an explicit erratum. Seven earlier Magma executions and four controls are carried records, not jobs rerun by this suite. Cited mathematical results and software remain premises. No proof-assistant formalization or external human peer review is claimed.',
        computational_baseline_note='The legacy top-level release_tag, release_asset_id, release_state, fresh_replay and original gates retain the unchanged 14 September historical binding. The current replacement and its later public observations are authenticated by current_distribution and current_publication. The release tag identifies the preparation snapshot; postpublication records are a main-branch follow-up.',
        current_release_publication_verification=BASE+'/PUBLICATION_VERIFICATION.json',
        arxiv_submission_ready=False, arxiv_submission_made=False,
        arxiv_submission_holds=['Requested Dahmen reply pending'])
    status['current_distribution'].update(acquisition_required=True,
        public_inputs_scope='Public companion plus the pinned externally acquired/private inputs; required licensed retained material is bundled.',
        withdrawal_record=BASE+'/OLD_ASSET_WITHDRAWAL_OBSERVATION.json')
    status['release_tag_snapshot']={'tag':prep.TAG,'commit':observation['tag_commit'],
        'scope':'Prepared source snapshot A; the current main-branch records describe later publication/download/withdrawal observations B.'}
    for key in preserve:need(status[key] == original_status[key], 'Historical status changed during integration')

    old_index = load(root / 'evidence/assets.json');index = copy.deepcopy(old_index)
    assets = prep.indexed(index['assets'], 'id')
    withdrawal_rows = prep.indexed(withdrawal['assets'], 'asset_id')
    for github_id, index_id in OLD_INDEX_IDS.items():
        row, observed_old = assets[index_id], withdrawal_rows[github_id]
        need(all(row[k] == observed_old[{'filename':'name'}.get(k,k)] for k in ('filename','bytes','sha256')), 'Old indexed asset identity changed')
        need(row['download_url'] == observed_old['download_url'], 'Old indexed download URL changed')
        row['withdrawn_download_url'] = row.pop('download_url')
        row.update(availability='withdrawn_'+withdrawal['checked_utc'][:10].replace('-','_'),
            withdrawn_utc=withdrawal['checked_utc'], github_asset_id=github_id,
            withdrawal_reason='Full Bruin-Poonen-Stoll paper included without an established downstream redistribution grant',
            withdrawal_record=BASE+'/OLD_ASSET_WITHDRAWAL_OBSERVATION.json', superseded_by=prep.TAG,
            audit_state_scope='Historical packaging/audit status retained; current adopted replay is recorded separately.')
    assets['PRIMITIVE_357_VERIFIED_RELEASE_2026_09_14_V1']['superseded_by'] = prep.TAG
    workspace_sources = {'companion':archive, 'paper_pdf':N.parent.parent/'output/pdf'/paper['pdf']['filename'],
                         'source_zip':N.parent.parent/'output'/paper['source_bundle']['filename']}
    for role in ('companion','paper_pdf','source_zip'):
        observed_row = observed[role];identical(workspace_sources[role], observed_row)
        need(ASSET_IDS[role] not in assets and observed_row['name'] not in {r['filename'] for r in index['assets']}, 'New asset already indexed')
        index['assets'].append({'id':ASSET_IDS[role],'filename':observed_row['name'],
            'sha256':observed_row['sha256'],'bytes':observed_row['bytes'],
            'source_path_from_workspace':relative_to_workspace(workspace_sources[role]),
            'github_release':prep.REPO+'/releases/tag/'+prep.TAG,'github_release_id':observation['release_id'],
            'github_asset_id':observed_row['asset_id'],'download_url':observed_row['url'],
            'role':{'companion':'Current replacement computational companion with bound fresh replay',
                    'paper_pdf':'Current first-submission paper bound to the replacement companion',
                    'source_zip':'Current two-file arXiv source package with byte-identical clean PDF rebuild'}[role],
            'current_role':role,'audit_state':'verified_current_replacement_publication',
            'availability':'public_download_verified','publication_record':BASE+'/PUBLICATION.json'})
    for previous in old_index['assets']:
        current = next(r for r in index['assets'] if r['id']==previous['id'])
        for key in ('id','filename','bytes','sha256','source_path_from_workspace','role','audit_state'):
            need(current[key]==previous[key], 'Historical asset record rewritten: '+key)
    add('evidence/assets.json',encoded(index))
    add('evidence/checksums/RELEASE_ASSETS_SHA256.txt',''.join(f"{r['sha256']}  {r['filename']}\n" for r in index['assets']).encode())

    date = observation['checked_utc'][:10]
    for name in HISTORICAL_READMES:
        text = file_bytes(root/name).decode()
        banner = f'> **Later update ({date}):** this is the historical event record. The [current replacement audit](../replacement-release-2026-09-15/README.md) records the published replacement, completed public-download checks and later p=5/rank withdrawals. The original event text below is retained unchanged.\n\n'
        need(not text.startswith(banner), 'Historical banner already installed')
        add(name,(banner+text).encode())
    decision=file_bytes(root/'docs/DECISION_LOG.md').decode()
    heading='## '+date+' — Publish the externally acquired-input replacement'
    need(heading not in decision, 'Publication decision already recorded')
    decision+='\n'+heading+'\n\nThe replacement `'+prep.TAG+'` was published and its five public assets were downloaded without authentication and checked against the sealed identities. The p=5 and rank downloads containing the BPS paper were withdrawn afterward, with both old API and download endpoints observed as HTTP 404. Their original byte identities remain in the ledger.\n\nThe main 13/65/16/5 replay and five separate default-reader checks retain distinct scope. The V5 reporting aggregate is corrected to 237,182 without changing the eight exact support tables. Seven prior Magma executions and the cited mathematical/software premises remain explicit. The release tag identifies prepared snapshot A; these observed postpublication records belong to the main-branch follow-up B. No arXiv submission has been made; Dahmen\'s requested reply remains the hold.\n'
    add('docs/DECISION_LOG.md',decision.encode())
    audit=f'''# Published replacement — {date}

The replacement [{prep.TAG}]({prep.REPO}/releases/tag/{prep.TAG}) is public. [PUBLICATION.json](PUBLICATION.json) and [PUBLIC_ACCESS_CHECK.json](PUBLIC_ACCESS_CHECK.json) bind the three main assets to actual unauthenticated downloads; [the full observation](FULL_PUBLIC_DOWNLOAD_OBSERVATION.json) also records the guide and checksums. The old p=5/rank assets were withdrawn afterward: [both API/download endpoint checks](OLD_ASSET_WITHDRAWAL_OBSERVATION.json) returned HTTP 404. Original asset identities remain preserved.

[BINDING.json](BINDING.json) authenticates the complete fresh isolated replay: **13 sector/interface records, 65 prior jobs and 16 rank-local checks**, with the latter joined to five freshly generated inputs. [The final extraction check](FINAL_EXTRACTION_EQUIVALENCE.json) found exactly the same replay inputs after extracting the sealed ZIP. The main irreducible-sector mode is `DEEP_REPLAY=0`; optional V15/V7 `--full` searches are not claimed.

Five default adapted readers passed separately, as documented by [V4/V6](supplemental/adapted-readers/supplemental_clean2/attempt2/SUPPLEMENTAL_RESULTS.json), [V2/V3](supplemental/adapted-readers/supplemental_clean2/attempt3/SUPPLEMENTAL_RESULTS.json) and the [corrected V5 result](supplemental/v5/SUPPLEMENTAL_V5_FINAL_RESULT.json). V5's eight exact support tables total **237,182 rows**; the historical 236,182 aggregate is a reporting error. The [erratum](supplemental/v5/TOTAL_COUNT_ERRATUM.md) preserves the raw source/log labels and explains the downstream metadata assertions; all eight exact generated-set comparisons passed.

[PAPER_REVISION.json](PAPER_REVISION.json) binds the current paper, its two-file source ZIP and this companion. [The build record](FINAL_PAPER_BUILD.json) and [visual review](FINAL_PDF_VISUAL_REVIEW.json) describe the clean byte-identical source rebuild and layout checks. Use the [complete replay guide](../../release/FINAL_COMPANION_REPLAY_GUIDE.md) for authenticated external acquisition and the actual runtime/isolation requirements.

The release tag names prepared source snapshot A, commit `{observation['tag_commit']}`. Its [prepublication record](PREPUBLICATION_PREPARATION.json) correctly says publication was pending then. These later observed publication/download/withdrawal records form the main-branch follow-up B; they do not alter the tag or imply that its earlier snapshot contained future observations.

Seven previous official Magma executions and four negative controls remain carried evidence; this suite did not execute Magma. Cited mathematics and software algorithms remain premises. No proof-assistant formalization or independent human peer review is claimed. **No arXiv submission has been made; Dahmen's requested reply is the remaining submission hold.**
'''
    add(BASE+'/README.md',audit.encode())

    if a.include_checker_controls:
        def add_checker_file(source, relative_target):
            target=prep.relative(BASE+'/checker-controls/'+relative_target)
            data=file_bytes(source)
            if target in changes:
                need(changes[target] == data, 'Conflicting checker-control target: '+target)
            else:
                add(target,data)
        for index_path, source_prefix in [
            ('publication_checker/ARTIFACT_INDEX.json','publication_checker'),
            ('current_binding/MANIFEST.json','current_binding'),
            ('publication_checker/PREPARATION_ARTIFACT_INDEX.json',''),
        ]:
            control_index=load(N/index_path)
            add_checker_file(N/index_path,index_path)
            for row in control_index['files']:
                relative_source='/'.join(part for part in (source_prefix,prep.relative(row['path'])) if part)
                source=N/relative_source;identical(source,row)
                add_checker_file(source,relative_source)
        for name in ('prepare_publication_records.py','integrate_published_repository.py'):
            add_checker_file(N/name,name)

    with tempfile.TemporaryDirectory(prefix='postpublication-review-',dir=out.parent) as temp:
        merged=Path(temp)/'root';compact_mirror(root,merged)
        for name,data in changes.items():
            target=merged/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
        check=verify_current_publication(merged,status,archive)
        need(check['status']=='PASS_CURRENT_PUBLICATION_OFFLINE_BINDING','Postpublication checker failed')
        add(BASE+'/PUBLICATION_VERIFICATION.json',encoded(check))
        add('audit/status.json',encoded(status))
        # No repository verifier runs here: its tracked snapshot must be
        # regenerated by the parent after this deliberately separate install.
        out.mkdir()
        for name,data in changes.items():
            target=out/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
    expected_before={name:identity(safe_target(root,name)) if safe_target(root,name).exists() else None for name in changes}
    plan={'schema':'primitive357_postpublication_repository_install_v1','status':'PASS_VALIDATED_INSTALL_PLAN',
        'mode':'APPLY' if a.apply else 'STAGED_ONLY','repository':str(root),'tag_snapshot_commit':observation['tag_commit'],
        'release_tag':prep.TAG,'release_id':observation['release_id'],'publication_check':check,
        'baseline_status_fields_preserved':preserve,'new_asset_ids':ASSET_IDS,
        'files':[{'path':name,**identity(out/name),'previous':expected_before[name]} for name in sorted(changes)],
        'tracked_manifest_regenerated':False,'commit_created':False,'github_mutated':False,'arxiv_submitted':False}
    (N/'POSTPUBLICATION_INTEGRATION_PLAN.json').write_bytes(encoded(plan))
    return root,out,changes,expected_before,plan

def apply_plan(root,out,changes,previous):
    """Install only validated planned paths, rolling back on a write error."""
    for name,old in previous.items():
        target=safe_target(root,name)
        need((not target.exists() and not target.is_symlink()) if old is None else identity(target)==old,
             'Repository changed after preflight: '+name)
    backups={name:file_bytes(root/name) if old is not None else None for name,old in previous.items()}
    installed=[]
    try:
        # Status last: no partially installed records may acquire final status.
        order=sorted(n for n in changes if n!='audit/status.json')+['audit/status.json']
        for name in order:
            target=safe_target(root,name);target.parent.mkdir(parents=True,exist_ok=True)
            fd,temp=tempfile.mkstemp(prefix='.publication-',dir=target.parent)
            try:
                with os.fdopen(fd,'wb') as handle:handle.write(changes[name])
                os.replace(temp,target);installed.append(name)
            finally:
                if os.path.exists(temp):os.unlink(temp)
    except BaseException:
        for name in reversed(installed):
            target=root/name;old=backups[name]
            if old is None:target.unlink()
            else:target.write_bytes(old)
        raise

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,default=R_DEFAULT)
    p.add_argument('--publication-records',type=Path,default=N/'publication_records')
    p.add_argument('--output',type=Path,default=N/'postpublication_repository_overlay')
    p.add_argument('--apply',action='store_true')
    p.add_argument('--include-checker-controls',action='store_true')
    a=p.parse_args();root,out,changes,previous,plan=stage_and_validate(a)
    if a.apply:
        apply_plan(root,out,changes,previous)
        plan['status']='PASS_POSTPUBLICATION_RECORDS_INSTALLED'
        (N/'POSTPUBLICATION_INTEGRATION_PLAN.json').write_bytes(encoded(plan))
    print(json.dumps(plan,indent=2))

if __name__=='__main__':main()
