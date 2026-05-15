import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

sys.path.append(str(BASE_DIR.parent / "libfolder"))

from mylib import myfunction

val = myfunction()

print(val)