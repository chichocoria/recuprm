# recuprm
Aplicacion para realizar backup de archivos de registración de la herramienta Sitel Cliente.
Se usó Python y se compilo a .exe con pyinstaller.

Autor: Ruben Dario Coria

## Colaboradores
* Damiam Heinze: Instalador NSIS y agregado el acceso directo al common startup de Sitel Cliente y de recuprm para que siempre inicie al encender la PC.
* Lucas Arenas
* Santiago Torriglia

## Descripcion General
La aplicacion busca eliminar los llamados por "Licencia Invalida" cuando el usuario experimenta cortes de luz, mal apagado de la PC o problemas externos.
Tambien busca eliminar los llamados por time-out provocados por que no esta ejecutado Sitel Cliente al inicio de la sesion.

## Funcionamiento
Una vez instalado Sitel PCPOS o Sifos y configuradas las aplicaciones con las licencias respectivas, debemos ejecutar el instalador Installer recuprm.exe.
En la primer ejecucion crea una carpeta llamada 'bkp' dentro del directorio de trabajo configurado en sitel (por defecto c:/estandar) con los archivos:
_sitel.prm
_sitel.prv
_sitel.emp
XXXXXXXX.prm
XXXXXXXX.lic

La app cada 60 segundos verifica que exista el archivo _sitel.prm que es el que desencadena el error, si no lo encuentra copia todo lo que esta en la carpeta bkp en los directorios q correspondan.

ej: "c:/estandar" y "programfiles/ITCSoluciones/SitelCliente"

El instalador crea un acceso directo en el directorio Startup para todos los usuarios de Sitel Cliente, esto elimina tener q aceeder a "Ejecutar" y cargar "Shell:common startup" para recien copiar el acceso directo.

## Instalacion

El camino aun es mas corto.

1-Correr el instalador Installer recuprm.exe

2-Listo!!

recuprm se ejecutara en el inicio de sesion de cualquier usuario y la app va a estar siempre activa y cada 60 segundos verificando cambios.

~~Es un ejecutable deberia copiarse dentro de ITCSoluciones/, para que el sistema corra al inicio es necesario crear una tarea desde el programador de tareas de windows.~~

~~1-Crear tarea basica.~~

~~2-Nombre: recuprm~~

~~3-Desencadenar: al iniciar sesion y que correa para cualquier usuario del sistema.~~

~~4-Accion: Iniciar un programa~~

~~5-Examinar: ruta en donde se encuentra el ejecutable "recuprm.exe"~~

~~6-En la solapa General tildar "ejecutar con los privilegios mas altos"~~

## Limitaciones
La aplicacion Funciona en Windows 7/8/10 y posteriores x86 y x64.
Es necesario como primer paso registrar licencia en Sitel y que se creen los archivos _sitel.prm, _sitel.prv y _sitel.emp asi como los archivos de licencia en la carpeta de instalacion de sitel XXXXXXXX.lic y XXXXXXXX.prm

## Releases

### V1.2
- Se agrega un log con level INFO en donde se puede visualizar fecha y hora del inicio del sistema, backup y recuperacion del mismo ("logs_info_itcs.log").
- Se cambio el nombre del directorio "bkp" a  "backup_itcs"

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

### Compilar el archivo .py

pyinstaller --onefile --windowed nombre_archivo.py
