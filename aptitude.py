#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Name: apt
Description: Modulo que maneja todo sobre repositorios
Version:0.1
License: GPLv3
Copyright: Copyright (C) 2009 Proyecto Libre Accesibilidad - Distrito Socialista Tecnologico AIT PDVSA  <moderador@libreaccesibilidad.org>
Author: Ernesto Nadir Crespo Avila
Email: ernesto@libreaccesibilidad.org
"""

from commands import getstatusoutput
from types import *
import string
import privilegios

import pdb

class Aptitude:
	
	def __init__(self):
		self.__url = "deb http://127.0.0.1:8000/debian"
		self.__versiones = ("testing","squeeze","sid","unstable")

		
	def __change_config(self):
		print "pasando por aca"
		privilegios.ejecutar("cp /etc/apt/sources.list /etc/apt/sources.list.bak")
		self.__version = self.__search_debian_version()
		if self.__version <> "":
			mirror = self.__url + " " + self.__version + " main"
		else:
			return -1
		privilegios.ejecutar(" echo %s > /etc/apt/sources.list" %mirror)
		return 0
	
	def __sources_orig(self):
		privilegios.ejecutar("cp /etc/apt/sources.list.bak /etc/apt/sources.list")
        
	def __search_debian_version(self):
		lista = []
		lineas = open("/etc/apt/sources.list").readlines()
		for i in range(len(lineas)):
			if string.find(lineas[i][:-1],"deb http://") <> -1 :
				lista.append(string.splitfields(lineas[i][:-1]," "))
		for i in range(len(lista)):
			if lista[i][2] in self.__versiones:
				self.__version = lista[i][2]
			else:
				self.__version = ""
		return self.__version
    
                
        
        
	def __update(self):
		privilegios.ejecutar("aptitude update")


	def __install(self,paquetes):
		if type(paquetes) is StringType:
			if string.find(paquetes,",") <> -1:
				print "La lista de paquetes no esta separada por espacios"
			else:
       				r = privilegios.ejecutar("aptitude install %s" %paquetes)
				print r
		else:
			print "Error, no es una lista de paquetes separadas por espacio"
	
	
		
	def main(self,paquetes):
		if self.__change_config()  == 0:
			self.__update()
			self.__install(paquetes)
			self.__sources_orig()
			print "Fin de instalacion de paquetes"
		else:
			print "Problemas con el archivo sources.list"
        




if __name__ == "__main__":
	aptitude = Aptitude()
        aptitude.main("conspy git-doc")
