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
import BaseHTTPServer, SimpleHTTPServer
import sys

def Inicio():
    apt = aptitude.Aptitude()
    print "Actualiza el repositorio local con respecto al repositorio principal"
    sincronizar.actualizar()
    print "Inicia el servidor web"
    try:
        httpd = BaseHTTPServer.HTTPServer( ( '', 80),SimpleHTTPServer.SimpleHTTPRequestHandler)
        httpd.serve_forever()
        print "Instala aplicaciones necesarias para darle accesibilidad al escritorio"
        apt.main("aqualung audacity")
        print "Configuración de los escritorios de los usuarios"
        config.conf_escritorio()
        sys.exit()
    except KeyboardInterrupt:
        pass
    else:
        sys.exit()
        
    
    
    
if __name__ == "__main__":
    Inicio()
    
    
