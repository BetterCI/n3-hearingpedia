"""Verify sources for the requested animal-model overview, without rerunning discovery."""
from pathlib import Path
import concurrent.futures
import json
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

OUT = Path(__file__).resolve().parents[1] / 'docs/research/comparative-hearing-2026-10-10'
DOIS = ['10.1007/s10162-016-0589-1', 'MED:39442868',
        'PMC:PMC6881193', '10.1016/0378-5955(90)90030-S',
        '10.1038/35008083', '10.1038/nature03867',
        '10.1371/journal.pgen.1000020', '10.1073/pnas.94.26.14837']

def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Hearingpedia evidence verification'}), timeout=25) as response:
        return response.read()

def one(doi):
    query = ('EXT_ID:39442868 AND SRC:MED' if doi.startswith('MED:') else
             'PMC6881193' if doi.startswith('PMC:') else 'DOI:"' + doi + '"')
    url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + urllib.parse.urlencode({'query': query, 'format': 'json', 'resultType': 'core'})
    result = json.loads(fetch(url))['resultList']['result']
    if not result:
        return {'requested_doi': doi, 'error': 'No DOI match'}
    row = result[0]
    row.update(requested_doi=row.get('doi', doi), metadata_source=url)
    if row.get('pmcid'):
        try:
            raw = fetch('https://www.ebi.ac.uk/europepmc/webservices/rest/' + row['pmcid'] + '/fullTextXML')
            (OUT / (row['pmcid'] + '-models.xml')).write_bytes(raw)
            doc = ET.fromstring(raw)
            text = [{'text': ''.join(p.itertext()).strip()} for p in doc.findall('.//body//p')]
            (OUT / (row['pmcid'] + '-models-text.json')).write_text(json.dumps(text, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
            row['models_fulltext_access'] = 'retrieved'
        except Exception as error:
            row['models_fulltext_access'] = str(error)
    return row

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    rows = list(pool.map(one, DOIS))
(OUT / 'animal-models-metadata.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for row in rows:
    print(row['requested_doi'], row.get('id'), row.get('title', row.get('error')), row.get('models_fulltext_access', 'abstract'))
