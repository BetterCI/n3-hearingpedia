from pathlib import Path
import runpy
for name in ("example-1.py", "example-2.py", "example-3.py"):
    print(name)
    runpy.run_path(str(Path(__file__).with_name(name)), run_name="__main__")
