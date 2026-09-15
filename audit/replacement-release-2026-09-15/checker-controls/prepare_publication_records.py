#!/usr/bin/env python3
"""Stage publication bindings from actual saved observations; never publish.

No repository, GitHub, or input file is modified. This offline helper verifies
the supplied download/API evidence and stages records in a new output root.
"""
from pathlib import Path
import argparse, copy, datetime, hashlib, json, os, re, shutil, stat, sys, tempfile
from urllib.parse import quote

N = Path(__file__).resolve().parent
sys.path.insert(0, str(N / 'current_binding'))
sys.path.insert(0, str(N / 'publication_checker'))
from verify_current_distribution import verify_current_distribution
from verify_current_publication import verify_current_publication

REPO = 'https://github.com/bbpcho/primitive-357-proof-audit'
API = 'https://api.github.com/repos/bbpcho/primitive-357-proof-audit'
TAG = 'replay-companion-2026-09-15.2'
BASE = 'audit/replacement-release-2026-09-15'
NAMES = {'companion': 'PRIMITIVE_357_REPLAY_COMPANION_2026-09-15_V2.zip',
         'paper_pdf': 'primitive_357_peter_chocian_submission_2026_09_15_v2.pdf',
         'source_zip': 'PRIMITIVE_357_ARXIV_SOURCE_2026-09-15_V2.zip',
         'replay_guide': 'FINAL_COMPANION_REPLAY_GUIDE.md', 'checksums': 'SHA256SUMS.txt'}
CORE = ('paper_pdf', 'source_zip', 'companion')
OLD = {
    561595084: ('2026-09-13_p5_literal_c_obstruction_dependency_closure_v1.zip',
               149934212, '03f3bfe077372275e570dd2541c033ba9a3c0701c80fecadfe1b575f3991d6eb'),
    561674379: ('2026-09-13_corrected66_predyadic_and_p2_place2_dependency_closure_v1.zip',
               137069860, 'ec90f7ce74fcdebfb3c398a7ac7da8426d590ff9abc0ef115e4824c0e2918248'),
}

def need(ok, message):
    if not ok:
        raise ValueError(message)

def unique_object(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, 'Duplicate JSON key: ' + key)
        result[key] = value
    return result

def path_checked(value, directory=False):
    p = Path(os.path.abspath(value))
    for part in [*reversed(p.parents), p]:
        if part.exists() or part.is_symlink():
            mode = part.lstat().st_mode
            need(not stat.S_ISLNK(mode), 'Symlink path: ' + str(part))
            if part != p:
                need(stat.S_ISDIR(mode), 'Non-directory parent: ' + str(part))
    if directory:
        need(p.is_dir(), 'Missing directory: ' + str(p))
    else:
        need(p.is_file(), 'Missing regular file: ' + str(p))
        need(stat.S_ISREG(p.stat().st_mode), 'Non-regular file: ' + str(p))
    return p

def relative(value):
    need(isinstance(value, str) and value and '\\' not in value and
         all(ord(c) >= 32 for c in value), 'Invalid relative path')
    p = Path(value)
    need(not p.is_absolute() and '..' not in p.parts and p.as_posix() == value and value != '.',
         'Unsafe relative path: ' + value)
    return value

def load(path):
    return json.loads(path_checked(path).read_text(), object_pairs_hook=unique_object)

def sha(path):
    with path_checked(path).open('rb') as handle:
        return hashlib.file_digest(handle, 'sha256').hexdigest()

def identity(path):
    path = path_checked(path)
    return {'bytes': path.stat().st_size, 'sha256': sha(path)}

def checked_identity(row, path):
    need(type(row['bytes']) is int and row['bytes'] >= 0 and
         isinstance(row['sha256'], str) and re.fullmatch('[0-9a-f]{64}', row['sha256']),
         'Malformed file identity')
    need(identity(path) == {k: row[k] for k in ('bytes', 'sha256')}, 'File identity mismatch: ' + str(path))

def bound(root, name):
    name = relative(name)
    return {'path': name, **identity(root / name)}

def encoded(value):
    return (json.dumps(value, indent=2) + '\n').encode()

def timestamp(value):
    need(isinstance(value, str), 'Timestamp type')
    result = datetime.datetime.fromisoformat(value.replace('Z', '+00:00'))
    need(result.tzinfo is not None and result.utcoffset() is not None, 'Timestamp lacks timezone')
    return result

def indexed(rows, key):
    need(isinstance(rows, list), 'Expected record list')
    result = {}
    for row in rows:
        need(isinstance(row, dict) and key in row and row[key] not in result, 'Missing or duplicate ' + key)
        result[row[key]] = row
    return result

def positive_id(value, label):
    need(type(value) is int and value > 0, 'Invalid ' + label)

def url(name, tag=TAG):
    return REPO + '/releases/download/' + quote(tag, safe='') + '/' + quote(name, safe='')

def validate_observation(observation, download_root):
    o = observation
    need(o.get('schema') == 'primitive357_full_public_download_observation_v1' and
         o.get('status') == 'PASS_PUBLIC_DOWNLOADS_AND_IDENTITIES', 'Successful actual download observation required')
    need(not o.get('_example_only', False), 'Example is not an observation')
    need(o['repository'] == REPO and o['release_tag'] == TAG and o['draft'] is False and
         o['repository_visibility'] == 'public' and o['unauthenticated_request'] is True,
         'Wrong or nonpublic observed release')
    positive_id(o['release_id'], 'release ID')
    need(timestamp(o['published_utc']) <= timestamp(o['checked_utc']), 'Downloads precede publication')
    api_rows = o['api_records']
    need(isinstance(api_rows, dict) and set(api_rows) in
         ({'REPOSITORY_API.json', 'RELEASE_API.json', 'TAG_REF_API.json'},
          {'REPOSITORY_API.json', 'RELEASE_API.json', 'TAG_REF_API.json', 'ANNOTATED_TAG_API.json'}),
         'Incomplete API observation records')
    apis = {}
    for name, row in api_rows.items():
        checked_identity(row, download_root / name)
        apis[name] = load(download_root / name)
    repo, release = apis['REPOSITORY_API.json'], apis['RELEASE_API.json']
    need(repo['private'] is False and repo['full_name'] == 'bbpcho/primitive-357-proof-audit', 'Repository API mismatch')
    positive_id(release['id'], 'API release ID')
    need(release['id'] == o['release_id'] and release['tag_name'] == TAG and release['draft'] is False and
         release['published_at'] == o['published_utc'], 'Release API mismatch')
    assets = indexed(release['assets'], 'name')
    asset_ids = set()
    for row in assets.values():
        positive_id(row['id'], 'API asset ID')
        need(row['id'] not in asset_ids, 'Duplicate API asset ID')
        asset_ids.add(row['id'])
    need(apis['TAG_REF_API.json']['ref'] == 'refs/tags/' + TAG, 'Wrong tag reference')
    obj = apis['TAG_REF_API.json']['object']
    if obj['type'] == 'tag':
        need('ANNOTATED_TAG_API.json' in apis and
             obj['url'] == API + '/git/tags/' + obj['sha'] and
             apis['ANNOTATED_TAG_API.json']['sha'] == obj['sha'], 'Annotated tag record missing or mismatched')
        obj = apis['ANNOTATED_TAG_API.json']['object']
    else:
        need('ANNOTATED_TAG_API.json' not in apis, 'Unexpected annotated tag record')
    need(obj['type'] == 'commit' and isinstance(obj['sha'], str) and
         re.fullmatch('[0-9a-f]{40}', obj['sha']) and obj['sha'] == o['tag_commit'], 'Tag commit observation mismatch')
    downloads = indexed(o['downloads'], 'role')
    need(set(downloads) == set(NAMES), 'Observation must contain exactly five asset roles')
    seen = set()
    for role, name in NAMES.items():
        row, api = downloads[role], assets[name]
        positive_id(row['asset_id'], 'download asset ID')
        need(row['asset_id'] not in seen, 'Duplicate downloaded asset ID')
        seen.add(row['asset_id'])
        need(row['name'] == name and row['url'] == url(name) and
             type(row['http_status']) is int and row['http_status'] == 200, 'Wrong downloaded asset: ' + role)
        checked_identity(row, download_root / name)
        need(row['asset_id'] == api['id'] and api['state'] == 'uploaded' and
             type(api['size']) is int and api['size'] == row['bytes'] and
             api['browser_download_url'] == row['url'] and
             api.get('digest') in (None, 'sha256:' + row['sha256']), 'API/download identity mismatch: ' + role)
    return downloads

def validate_withdrawal(w, download_check_time):
    need(w.get('schema') == 'primitive357_old_asset_withdrawal_observation_v1' and
         w.get('status') == 'PASS_WITHDRAWN_PUBLIC_ENDPOINTS', 'Completed withdrawal observation required')
    need(not w.get('_example_only', False), 'Example is not withdrawal evidence')
    need(w['repository'] == REPO and w['replacement_release_tag'] == TAG and
         w['unauthenticated_request'] is True, 'Withdrawal scope mismatch')
    need(timestamp(w['checked_utc']) >= timestamp(download_check_time), 'Withdrawal observation precedes completed replacement download checks')
    rows = indexed(w['assets'], 'asset_id')
    need(set(rows) == set(OLD), 'Withdrawal must cover exactly the two old assets')
    for asset_id, (name, size, digest) in OLD.items():
        row = rows[asset_id]
        positive_id(asset_id, 'withdrawn asset ID')
        need(row['name'] == name and type(row['bytes']) is int and row['bytes'] == size and
             row['sha256'] == digest, 'Withdrawn historical identity mismatch')
        need(row['api_url'] == API + '/releases/assets/' + str(asset_id) and
             row['download_url'] == url(name, 'audit-2026-09-13.1'), 'Wrong withdrawal endpoint')
        for key in ('api_http_status', 'download_http_status'):
            need(type(row[key]) is int and row[key] == 404, 'Withdrawal endpoint is not observed HTTP 404')

def copy_tree_checked(source, destination):
    for directory, dirs, files in os.walk(source, followlinks=False):
        relative_dir = Path(directory).relative_to(source)
        folded = [n.casefold() for n in dirs + files]
        need(len(folded) == len(set(folded)), 'Case-fold collision in overlay')
        target = destination / relative_dir
        target.mkdir(parents=True, exist_ok=True)
        for name in dirs:
            path_checked(Path(directory) / name, directory=True)
        for name in files:
            shutil.copyfile(path_checked(Path(directory) / name), target / name)

def prepare(a):
    root = path_checked(a.repo_overlay, directory=True)
    downloads_root = path_checked(a.download_root, directory=True)
    archive = path_checked(a.companion_archive)
    out = Path(os.path.abspath(a.output))
    need(not out.exists() and not out.is_symlink(), 'Output root must be new')
    need(not out.is_relative_to(root) and not root.is_relative_to(out), 'Output and overlay must be disjoint')
    path_checked(out.parent, directory=True)
    for p in [downloads_root, archive, Path(a.final_identity), Path(a.paper_build), Path(a.observation), Path(a.withdrawal_record)]:
        need(not p.absolute().is_relative_to(out), 'Output may not contain an input')
    final, paper, observation, withdrawal = map(load, (a.final_identity, a.paper_build, a.observation, a.withdrawal_record))
    need(final.get('schema') == 'primitive357_final_archive_identity_v1' and
         final['status'] == 'PASS_FINAL_APPEND_ONLY_COMPANION' and final['name'] == NAMES['companion'] and
         final['release_tag'] == TAG, 'Wrong final companion')
    checked_identity(final, archive)
    need(paper.get('schema') == 'primitive357_final_paper_build_v1' and
         paper['status'] == 'PASS_PAPER_BUILD_AND_CLEAN_SOURCE_REBUILD' and paper['companion'] == final and
         paper['clean_source_rebuild'] == 'PASS_BYTE_IDENTICAL_PDF' and
         paper['visual_review'] == 'PASS_VISUAL_REVIEW' and
         paper['undefined_references'] is False and paper['overfull_boxes'] is False and
         paper['arxiv_submitted'] is False and paper['submission_holds'] == ['Requested Dahmen reply pending'],
         'Final paper build does not match the sealed companion or submission state')
    observed = validate_observation(observation, downloads_root)
    validate_withdrawal(withdrawal, observation['checked_utc'])
    binding_path = relative(a.binding_path)
    binding = load(root / binding_path)
    need(binding['release_tag'] == TAG and binding['asset'] ==
         {'name': final['name'], 'bytes': final['bytes'], 'sha256': final['sha256'], 'url': url(final['name'])},
         'Final companion differs from current binding')
    status_path = root / 'audit/status.json'
    status = load(status_path) if status_path.exists() else {'github_repository': REPO}
    need(status['github_repository'] == REPO, 'Overlay repository mismatch')
    for key in ('arxiv_submitted', 'arxiv_submission_made', 'arxiv_submission_ready'):
        need(key not in status or status[key] is False, 'Overlay makes unsupported arXiv claim')
    status = copy.deepcopy(status)
    status['current_distribution'] = {'state': 'verified_externalized_replay',
        'public_complete_replay_inputs_available': True, 'replacement_complete_companion_published': True,
        'original_mathematical_replay_status_unchanged': True, 'binding': bound(root, binding_path)}
    distribution_check = verify_current_distribution(root, status, archive)
    need(distribution_check['status'] == 'PASS_CURRENT_DISTRIBUTION_ARCHIVE_AND_RECORD_BINDING', 'Companion archive binding failed')
    canonical = {name: bound(root, 'paper/' + name) for name in ('manuscript.tex', 'rank-proof.tex', 'manuscript.pdf')}
    need(set(paper['paper']) == set(canonical) and all(paper['paper'][name] == row['sha256'] for name, row in canonical.items()),
         'Canonical paper differs from actual build')
    source_path = 'release/' + NAMES['source_zip']
    source = bound(root, source_path)
    for role, build_row, local_row in [('paper_pdf', paper['pdf'], canonical['manuscript.pdf']),
                                       ('source_zip', paper['source_bundle'], source)]:
        need(build_row['filename'] == NAMES[role] and
             all(build_row[k] == local_row[k] == observed[role][k] for k in ('bytes', 'sha256')),
             'Build/local/download identity mismatch: ' + role)
    need(all(observed['companion'][k] == final[k] for k in ('bytes', 'sha256')), 'Downloaded companion differs')
    members = [{'path': name, 'repository_path': 'paper/' + name,
                **{k: canonical[name][k] for k in ('bytes', 'sha256')}} for name in sorted(('manuscript.tex', 'rank-proof.tex'))]
    built_members = indexed(paper['source_members'], 'name')
    need(set(built_members) == {'manuscript.tex', 'rank-proof.tex'} and
         all(built_members[row['path']]['sha256'] == row['sha256'] for row in members), 'Built source-member identity mismatch')
    assets = {role: {k: observed[role][k] for k in ('name', 'bytes', 'sha256', 'url')} for role in CORE}
    submission = {'arxiv_submission_made': False, 'arxiv_submission_ready': False,
                  'dahmen_reply_pending': True, 'holds': ['Requested Dahmen reply pending']}
    provenance = {name: identity(path) for name, path in
                  [('final_archive_identity', a.final_identity), ('paper_build', a.paper_build),
                   ('public_download_observation', a.observation), ('withdrawal_observation', a.withdrawal_record)]}
    revision = {'schema': 'primitive357_current_paper_revision_v1', 'release_tag': TAG,
                'companion_binding': status['current_distribution']['binding'], 'paper_files': canonical,
                'source_bundle': {'archive': source, 'members': members}, 'assets': assets,
                'submission': submission, 'preparation_input_identities': provenance}
    revision_bytes = encoded(revision)
    publication = {'schema': 'primitive357_current_publication_v1', 'repository': REPO,
        'release_tag': TAG, 'release_id': observation['release_id'], 'draft': False,
        'paper_revision_sha256': hashlib.sha256(revision_bytes).hexdigest(), 'arxiv_submission_made': False,
        'published_utc': observation['published_utc'], 'tag_commit': observation['tag_commit'],
        'assets': [dict(assets[role], role=role, asset_id=observed[role]['asset_id']) for role in CORE]}
    access = {'schema': 'primitive357_current_public_access_v1', 'repository': REPO,
        'release_tag': TAG, 'release_id': observation['release_id'], 'draft': False,
        'checked_utc': observation['checked_utc'], 'unauthenticated_request': True, 'repository_visibility': 'public',
        'downloads': [dict(assets[role], role=role, asset_id=observed[role]['asset_id'], http_status=observed[role]['http_status']) for role in CORE]}
    with tempfile.TemporaryDirectory(prefix='publication-staging-', dir=out.parent) as temp:
        staged = Path(temp) / 'records'
        staged.mkdir()
        current = {'state': 'published'}
        for role, name, data in [('paper_revision', 'PAPER_REVISION.json', revision_bytes),
                                 ('publication', 'PUBLICATION.json', encoded(publication)),
                                 ('public_access', 'PUBLIC_ACCESS_CHECK.json', encoded(access))]:
            name = BASE + '/' + name
            target = staged / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            current[role] = bound(staged, name)
        status.update(current_publication=current, current_paper_revision=current['paper_revision']['path'],
                      current_paper_publication=current['publication']['path'], public_access_check=current['public_access']['path'],
                      arxiv_submission_ready=False, arxiv_submission_made=False,
                      arxiv_submission_holds=submission['holds'])
        merged = Path(temp) / 'overlay'
        copy_tree_checked(root, merged)
        for role in ('paper_revision', 'publication', 'public_access'):
            name = current[role]['path'];target = merged / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(staged / name, target)
        check = verify_current_publication(merged, status, archive)
        need(check['status'] == 'PASS_CURRENT_PUBLICATION_OFFLINE_BINDING', 'Publication checker did not pass')
        (staged / 'PROSPECTIVE_STATUS.json').write_bytes(encoded(status))
        (staged / 'PROSPECTIVE_CURRENT_PUBLICATION.json').write_bytes(encoded(current))
        result = {'schema': 'primitive357_publication_record_preparation_v1',
            'status': 'PASS_STAGED_PUBLICATION_RECORDS', 'publication_check': check,
            'input_identities': provenance, 'verified_download_roles': list(NAMES), 'publication_roles': list(CORE),
            'withdrawal_asset_ids': sorted(OLD), 'record_rows': current,
            'network_requests_made': False, 'repository_modified': False, 'github_modified': False,
            'arxiv_submission_made': False, 'arxiv_submission_ready': False,
            'boundary': 'Offline authentication of supplied actual observations and local bytes; no new live observations are manufactured.'}
        (staged / 'PUBLICATION_RECORD_PREPARATION.json').write_bytes(encoded(result))
        need(not out.exists() and not out.is_symlink(), 'Output appeared during validation')
        staged.rename(out)
    return result

def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('repo-overlay', 'download-root', 'companion-archive', 'final-identity',
                 'paper-build', 'observation', 'withdrawal-record', 'output'):
        p.add_argument('--' + name, type=Path, required=True)
    p.add_argument('--binding-path', default=BASE + '/BINDING.json')
    args = p.parse_args()
    print(json.dumps(prepare(args), indent=2))

if __name__ == '__main__':
    main()
