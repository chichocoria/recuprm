import os.path
import os
import shutil
import glob

if os.path.exists('C:/Program Files (x86)'):
## Valida si el SO es de 64Bit  
    if os.path.exists('C:/estandar/bkp/'):
        print('La carpeta bkp existe y el sistema operatico es de 64bits.')
        ##Valida si existe el archivo prm que es el que desencadena el problema, si exite no hace nada, si no existe realiza el backup
        ##en la carpeta bkp
        if os.path.exists('C:/estandar/_sitel.prm'):
            print('El archivo existe.')
        else:
            files_sitel = glob.iglob(os.path.join('C:/estandar/bkp/', "_site*"))
            for file in files_sitel:
                if os.path.isfile(file):
                    shutil.copy2(file, 'C:/estandar/')
            fileslic = glob.iglob(os.path.join(
                'C:/estandar/bkp/', "*.lic"))
            for file in fileslic:
                if os.path.isfile(file):
                    shutil.copy2(file, 'C:/Program Files (x86)/ITC Soluciones/Sitel Cliente/')
            filesprm = glob.iglob(os.path.join(
                'C:/estandar/bkp/', "*.prm"))
            for file in filesprm:
                if os.path.isfile(file):
                    shutil.copy2(file, 'C:/Program Files (x86)/ITC Soluciones/Sitel Cliente/')
                print('El archivo no existe.')
    else:
        if os.path.exists('C:/estandar/_sitel.prm') and os.path.exists('C:/estandar/_sitel.prv') and os.path.exists('C:/estandar/_sitel.emp'):
            os.mkdir('C:/estandar/bkp/')

        files_sitel = glob.iglob(os.path.join('C:/estandar/', "_site*"))
        for file in files_sitel:
            if os.path.isfile(file):
                shutil.copy2(file, 'C:/estandar/bkp/')
        fileslic = glob.iglob(os.path.join(
            'C:/Program Files (x86)/ITC Soluciones/Sitel Cliente/', "*.lic"))
        for file in fileslic:
            if os.path.isfile(file):
                shutil.copy2(file, 'C:/estandar/bkp/')
        filesprm = glob.iglob(os.path.join(
            'C:/Program Files (x86)/ITC Soluciones/Sitel Cliente/', "*.prm"))
        for file in filesprm:
            if os.path.isfile(file):
                shutil.copy2(file, 'C:/estandar/bkp/')
                print('Se creo la carpeta bkp con los archivos de registracion.')

else:
    #El sistema operativo es de 32bits 
    if os.path.exists('C:/estandar/bkp/'):
        print('La carpeta bkp existe y el sistema operatico es de 64bits.')
        ##Valida si existe el archivo prm que es el que desencadena el problema, si exite no hace nada, si no existe realiza el backup
        ##en la carpeta bkp
        if os.path.exists('C:/estandar/_sitel.prm'):
            print('El archivo existe.')
        else:
            files_sitel = glob.iglob(os.path.join('C:/estandar/bkp/', "_site*"))
            for file in files_sitel:
                if os.path.isfile(file):
                    shutil.copy2(file, 'C:/estandar/')
            fileslic = glob.iglob(os.path.join(
                'C:/estandar/bkp/', "*.lic"))
            for file in fileslic:
                if os.path.isfile(file):
                    shutil.copy2(file, 'C:/Program Files/ITC Soluciones/Sitel Cliente/')
            filesprm = glob.iglob(os.path.join(
                'C:/estandar/bkp/', "*.prm"))
            for file in filesprm:
                if os.path.isfile(file):
                    shutil.copy2(file, 'C:/Program Files/ITC Soluciones/Sitel Cliente/')
                print('El archivo no existe.')
    else:
        os.mkdir('C:/estandar/bkp/')

        files_sitel = glob.iglob(os.path.join('C:/estandar/', "_site*"))
        for file in files_sitel:
            if os.path.isfile(file):
                shutil.copy2(file, 'C:/estandar/bkp/')
        fileslic = glob.iglob(os.path.join(
            'C:/Program Files/ITC Soluciones/Sitel Cliente/', "*.lic"))
        for file in fileslic:
            if os.path.isfile(file):
                shutil.copy2(file, 'C:/estandar/bkp/')
        filesprm = glob.iglob(os.path.join(
            'C:/Program Files/ITC Soluciones/Sitel Cliente/', "*.prm"))
        for file in filesprm:
            if os.path.isfile(file):
                shutil.copy2(file, 'C:/estandar/bkp/')
                print('Se creo la carpeta bkp con los archivos de registracion.')