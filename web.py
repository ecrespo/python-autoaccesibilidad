#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Name: web
Description: Modulo que inicia un servidor web
Version:0.1
License: GPLv3
Copyright: Copyright (C) 2009 Proyecto Libre Accesibilidad - Distrito Socialista Tecnologico AIT PDVSA  <moderador@libreaccesibilidad.org>
Author: Ernesto Nadir Crespo Avila
Email: ernesto@libreaccesibilidad.org
"""
#import SimpleHTTPServer
#SimpleHTTPServer.test()
#python -m SimpleHTTPServer

import BaseHTTPServer, SimpleHTTPServer
import sys
print "probando"
httpd = BaseHTTPServer.HTTPServer( ( '', 8000),SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.serve_forever()
    
