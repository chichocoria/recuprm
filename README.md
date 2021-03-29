# recuprm
Sistema para realizar backup de archivos de registración de la herramienta Sitel Cliente.

## Limitaciones
La aplicacion Funciona en Windows 7 y posteriores x86 y x64.
Es necesario como primer paso registrar licencia en Sitel y que se creen los archivos _sitel.prm, _sitel.prv y _sitel.emp asi como los archivos de licencia en la carpeta de instalacion de sitel XXXXXXXX.lic y XXXXXXXX.prm

## Compilacion
Para compilar el archivo se utilizo.
 * Windows 7 32bits SP1
 * Python 2.7.18
 * pyinstaller 2.1
 * pywin32

Para compilar se cambio el nombre de la libreria "winreg". En Python 3.9 el nombre de la libreria es winreg pero en Python 2.7 la libreria es _winreg

### Correr en consola

pip install pyinstaller==2.1

pip install pypiwin32

### Compilar el archico .py

pyinstaller --onefile --windowed nombre_archivo.py



