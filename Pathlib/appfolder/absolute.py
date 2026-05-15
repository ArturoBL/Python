import sys
from pathlib import Path

# Carpeta externa
ruta_libs = Path("/home/dark/Progra/Pruebas/libpath/libfolder/")

sys.path.append(str(ruta_libs))

from mylib import myfunction

val = myfunction()

print(val)