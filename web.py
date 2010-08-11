#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Name: web
Description: Modulo que inicia un servidor web
Version:0.1
License: GPLv3
Copyright: Copyright (C) 2009 Proyecto Libre Accesibilidad - Distrito Socialista Tecnologico AIT PDVSA 
Author: Ernesto Nadir Crespo Avila
Email: ecrespo@gmail.com
"""

from twisted.internet import reactor
from twisted.web import static, server

class WebServer:
	def __init__(self,ruta,puerto):
		self.__ruta = ruta
		self.__puerto = puerto
		self.__servicio = static.File(self.__ruta)
		
	
	def run(self):
		reactor.listenTCP(self.__puerto,server.Site(self.__servicio))
		reactor.run()
	def stop(self):
		reactor.stop()

if __name__ == "__main__":
	servidorweb = WebServer('/home/ernesto/googlecode/python-autoaccesibilidad/debian',8080)
	servidorweb.run()
		
		
