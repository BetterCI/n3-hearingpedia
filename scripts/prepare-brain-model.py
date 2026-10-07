"""Convert Nilearn's fsaverage5 pial surfaces into a compact local display asset.

Input files and upstream license are kept with their source URLs in
public/models/brain/NOTICE.txt. Run with the four downloaded GIFTI files
in artifacts/brain-map/fsaverage5. No Python packages are required.
"""
import base64
import gzip
import json
import struct
import xml.etree.ElementTree as ET
import zlib
from pathlib import Path

root = Path(__file__).resolve().parents[1]
input_dir = root / 'artifacts/brain-map/fsaverage5'

def arrays(path):
    document = ET.fromstring(gzip.decompress(path.read_bytes()))
    result = []
    for array in document.findall('DataArray'):
        assert array.attrib['Encoding'] == 'GZipBase64Binary'
        assert array.attrib['Endian'] == 'LittleEndian'
        binary = zlib.decompress(base64.b64decode(array.findtext('Data')))
        code = 'f' if array.attrib['DataType'] == 'NIFTI_TYPE_FLOAT32' else 'i'
        result.append(list(struct.unpack('<' + str(len(binary) // 4) + code, binary)))
    return result

hemispheres = []
for side in ('left', 'right'):
    points, triangles = arrays(input_dir / f'pial_{side}.gii.gz')
    sulc, = arrays(input_dir / f'sulc_{side}.gii.gz')
    assert len(points) == 10242 * 3 and len(triangles) == 20480 * 3
    assert len(sulc) == 10242
    hemispheres.append({'side': side, 'positions': [round(v * 10) for v in points],
                        'triangles': triangles, 'sulc': [round(v * 100) for v in sulc]})
output = root / 'public/models/brain'
output.mkdir(parents=True, exist_ok=True)
asset = output / 'fsaverage5.json'
asset.write_text(json.dumps({'version': 1, 'positionScale': .1, 'sulcScale': .01,
                            'hemispheres': hemispheres}, separators=(',', ':')), encoding='utf-8')
print(f'{asset.name}: {asset.stat().st_size:,} bytes; 20,484 vertices; 40,960 triangles')
