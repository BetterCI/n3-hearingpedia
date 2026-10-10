from pathlib import Path
import tempfile
import urllib.request
from pypdf import PdfReader
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

url = 'https://people.ee.ethz.ch/~isistaff/courses/ak1/skriptA1-english_2024.pdf'
target = Path(tempfile.gettempdir()) / 'n3-sound-waves-eth-notes.pdf'
if not target.exists():
    with urllib.request.urlopen(url, timeout=30) as response:
        target.write_bytes(response.read())
reader = PdfReader(target)
for i in [0, 91, 92, 98, 99]:
    print(f'\n--- PDF page {i+1} ---\n{reader.pages[i].extract_text()}')
