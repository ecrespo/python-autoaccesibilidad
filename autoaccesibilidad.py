#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Name: autoaccesibilidad
Description: Programa principal que permite instalar aplicaciones accesibles de un repositorio local
Version:0.1
License: GPLv3
Copyright: Copyright (C) 2009 Proyecto Libre Accesibilidad - Distrito Socialista Tecnologico AIT PDVSA  <moderador@libreaccesibilidad.org>
Author: Ernesto Nadir Crespo Avila
Email: ernesto@libreaccesibilidad.org
"""
import pdb
import config
import aptitude
import privilegios
import users 
import sincronizar
from commands import getstatusoutput
import sys
import getpass
import time    

def Inicio():
    try:
        apt = aptitude.Aptitude()
        sincronizar.actualizar()
        getstatusoutput("sudo python -m SimpleHTTPServer")
        print "Ejecutando el servidor web"
        apt.main("accessibility-es speech-dispatcher")
        while 1:
            #r = getstatusoutput("./reproducir.py btreathe.ogg")
            idioma = raw_input("Escriba el idioma que desea usar en el lector de pantalla:[Ingles/Español]:")
            if idioma == "Ingles":
                lang = "english"
                break
            elif idioma =="Español":
                lang = "spanish"
                break
            else:
                print "Error colocando el idioma"
                #r = getstatusoutput("./reproducir.py btreathe.ogg")
                continue
        config.conf_escritorio("lang")
        #sys.exit()
    except KeyboardInterrupt:
        pass
    else:
        sys.exit()
        
    
    
    
if __name__ == "__main__":
    Inicio()
    
    
