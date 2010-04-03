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
from string import splitfields
import pyttsx
import threading

def ServidorWeb():
    getstatusoutput("python -m SimpleHTTPServer &")

class Accesibilidad():
    def __init__(self):
        self.engine = pttsx.init()
        self.engine.setProperty('voice', "spanish-latin-american")
        self.apt = aptitude.Aptitude()
        
    def instalar_paquetes(self):
        print "sincronizando repositorio"
        self.engine.say("sincronizando repositorio")
        self.engine.runAndWait()

        sincronizar.actualizar
        print "instalando paquetes accesibles"
        self.engine.say("instalando paquetes accesibles")
        self.engine.runAndWait()
        self.apt.main("accessibility-es speech-dispatcher")
        
        while 1:
            self.engine.say("Escriba el idioma que desea usar en el lector de pantalla Ingles o Español")
            self.engine.runAndWait()
            idioma = raw_input("Escriba el idioma que desea usar en el lector de pantalla:[Ingles/Español]:")
            if idioma == "Ingles":
                lang = "english"
                break
            elif idioma =="Español":
                lang = "spanish"
                break
            else:
                print "Error colocando el idioma"
                self.engine.say("Error colocando el idioma")
                self.engine.runAndWait()
                continue
        config.conf_escritorio("lang")
        self.__fin_web()
        print "Finalizando autoaccesibilidad"
        self.engine.say("Finalizando autoaccesibilidad")
        self.engine.runAndWait()
        sys.exit(0)
        
    def __fin_web(self):
        r = getstatusoutput("ps -aux | grep python | grep web.py")
        if r[0] == 0:
            s = splitfields(r[1]," ")
            t = getstatusoutput("kill -9 %s" %s[12])
            if t[0] <> 0:
                print "no se pudo apagar el servidor web local"
            else:
                print "se apago el servidor web"
        
        
    
    
    
if __name__ == "__main__":
    accesibilidad = Accesibilidad()
    accesibilidad.instalar_paquetes()
    
    
        
    
    
