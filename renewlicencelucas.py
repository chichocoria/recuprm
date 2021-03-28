import os.path
import os
import shutil
import glob
import _winreg
import sched, time

while True:        

    #Busca en el registro de Windows el directorio de Puleo de Sitel Cliente.
    with _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, "SOFTWARE\\VB and VBA Program Settings\\Sitel32\\Puleo") as key:
        value = _winreg.QueryValueEx(key,'Directorio')
    ##variable que contiene el directorio de trabajo, el resultado es una array pero solo traigo el valor 0.
    dirtrabajo=(value[0])
    print (dirtrabajo)
    ##variable que contiene el directorio del backup
    bkp= r'/bkp'
    dirbackup = dirtrabajo + bkp
    ##variables que contiene el path hasta el archivo _sitel.*
    archivoprm= dirtrabajo + '\\_sitel.prm'
    archivoprv= dirtrabajo + '\\_sitel.prv'
    archivoemp= dirtrabajo + '\\_sitel.emp'
    print (dirbackup)

    if os.path.exists('C:/Program Files (x86)'):
    ## Valida si el SO es de 64Bit  
        if os.path.exists(dirbackup):
            print('La carpeta bkp existe y el sistema operatico es de 64bits.')
            ##Valida si existe el archivo prm que es el que desencadena el problema, si exite no hace nada, si no existe realiza el backup en la carpeta bkp
            if os.path.exists(archivoprm):
                print('El archivo existe.')
            else:
                files_sitel = glob.iglob(os.path.join(dirbackup, "_site*"))
                for file in files_sitel:
                    if os.path.isfile(file):
                        shutil.copy2(file, dirtrabajo)
                fileslic = glob.iglob(os.path.join(dirbackup, "*.lic"))
                for file in fileslic:
                    if os.path.isfile(file):
                        shutil.copy2(file, 'C:/Program Files (x86)/ITC Soluciones/Sitel Cliente/')
                filesprm = glob.iglob(os.path.join(dirbackup, "*.prm"))
                for file in filesprm:
                    if os.path.isfile(file):
                        shutil.copy2(file, 'C:/Program Files (x86)/ITC Soluciones/Sitel Cliente/')
                        print('El archivo prm se borro inesperadamente, se realizo el backup OK.')
        else:
            ##Si existen los archivos _sitel prm prv y emp en el directorio de trabajo, crea la carpeta bkp
            if os.path.exists(archivoprm) and os.path.exists(archivoprv) and os.path.exists(archivoemp):
                os.mkdir(dirbackup)
            files_sitel = glob.iglob(os.path.join(dirtrabajo, "_site*"))
            for file in files_sitel:
                if os.path.isfile(file):
                    shutil.copy2(file, dirbackup)
            fileslic = glob.iglob(os.path.join(
                'C:/Program Files (x86)/ITC Soluciones/Sitel Cliente/', "*.lic"))
            for file in fileslic:
                if os.path.isfile(file):
                    shutil.copy2(file, dirbackup)
            filesprm = glob.iglob(os.path.join(
                'C:/Program Files (x86)/ITC Soluciones/Sitel Cliente/', "*.prm"))
            for file in filesprm:
                if os.path.isfile(file):
                    shutil.copy2(file, dirbackup)
                    print('Se creo la carpeta bkp con los archivos de registracion.')

    else:
        #El sistema operativo es de 32bits 
        if os.path.exists(dirbackup):
            print('La carpeta bkp existe y el sistema operatico es de 32bits.')
            ##Valida si existe el archivo prm que es el que desencadena el problema, si exite no hace nada, si no existe realiza el backup
            ##en la carpeta bkp
            if os.path.exists(archivoprm):
                print('El archivo existe.')
            else:
                files_sitel = glob.iglob(os.path.join(dirbackup, "_site*"))
                for file in files_sitel:
                    if os.path.isfile(file):
                        shutil.copy2(file, dirtrabajo)
                fileslic = glob.iglob(os.path.join(
                    dirbackup, "*.lic"))
                for file in fileslic:
                    if os.path.isfile(file):
                        shutil.copy2(file, 'C:/Program Files/ITC Soluciones/Sitel Cliente/')
                filesprm = glob.iglob(os.path.join(
                    dirbackup, "*.prm"))
                for file in filesprm:
                    if os.path.isfile(file):
                        shutil.copy2(file, 'C:/Program Files/ITC Soluciones/Sitel Cliente/')
                        print('El archivo prm se borro inesperadamente, se realizo el backup OK.')
        else:
            os.mkdir(dirbackup)

            files_sitel = glob.iglob(os.path.join(dirtrabajo, "_site*"))
            for file in files_sitel:
                if os.path.isfile(file):
                    shutil.copy2(file, dirbackup)
            fileslic = glob.iglob(os.path.join(
                'C:/Program Files/ITC Soluciones/Sitel Cliente/', "*.lic"))
            for file in fileslic:
                if os.path.isfile(file):
                    shutil.copy2(file, dirbackup)
            filesprm = glob.iglob(os.path.join(
                'C:/Program Files/ITC Soluciones/Sitel Cliente/', "*.prm"))
            for file in filesprm:
                if os.path.isfile(file):
                    shutil.copy2(file, dirbackup)
                    print('Se creo la carpeta bkp con los archivos de registracion.')

    #Arriba la busqueda de la carpeta bkp copia todos los archivos con extension prm, por eso abajo se borra el _sitel.prm de ese directorio al finalizar el programa.
    if os.path.exists ('C:/Program Files (x86)/ITC Soluciones/Sitel Cliente/_sitel.prm'):
        os.remove('C:/Program Files (x86)/ITC Soluciones/Sitel Cliente/_sitel.prm')
    ##Corre cada 60 segundos el programa.
    time.sleep(60)
