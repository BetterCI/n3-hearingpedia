"""Read selected public PDF sections; downloaded copies stay in the system temporary directory."""
from pathlib import Path
import tempfile
import urllib.request
import sys
from pypdf import PdfReader

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
materials = [
 ('gavioso', 'https://iris.inrim.it/retrieve/3fb286b8-b616-4d85-9c76-d08d22e41af2/Gavioso_et.pdf', [20, 30, 31, 32, 33]),
 ('allen', 'https://jontalle.web.engr.illinois.edu/Public/AllenBerkley97.pdf', [0, 1]),
]
for name, url, indices in materials:
    target = Path(tempfile.gettempdir()) / f'n3-sound-waves-{name}.pdf'
    try:
        if not target.exists():
            with urllib.request.urlopen(url, timeout=30) as response:
                target.write_bytes(response.read())
        reader = PdfReader(target)
        for i in indices:
            print(f'\n--- {name}: PDF page {i+1} ---\n{reader.pages[i].extract_text()}')
    except Exception as e:
        print(f'{name}: retrieval failed: {e}')
