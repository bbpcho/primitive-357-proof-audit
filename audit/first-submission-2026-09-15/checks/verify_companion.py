"""Check the included component bytes; not a mathematical replay."""
from pathlib import Path
import hashlib,json
A=Path(__file__).resolve().parents[1]
manifest=json.loads((A/'COMPONENT_MANIFEST.json').read_text())
for item in manifest['files']:
    p=A/item['path']
    assert p.is_file(),item['path']
    assert p.stat().st_size==item['bytes'],item['path']
    h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(8*1024*1024),b''):h.update(block)
    assert h.hexdigest()==item['sha256'],item['path']
print(json.dumps({'files_verified':len(manifest['files']),'status':'PASS','scope':'File identity only; no mathematical replay.'},indent=2))
