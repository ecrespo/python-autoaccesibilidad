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
import su


class apt:
	def __init__(self):
		self.__url = "deb http://127.0.0.1/debian"
        self.__versiones = ("testing","squeeze","sid","unstable")
		
	def __change_config(self):
		su.ejecutar("cp /etc/apt/sources.list /etc/apt/sources.list.bak")
        version = self.__search_debian_version()
        if version <> "":
            mirror = self.__url + " " + version + " main"
        else:
            return -1
        su.ejecutar(" echo %s > /etc/apt/sources.list" %mirror) 
        return 0
        
    def __sources_orig(self):
        su.ejecutar("cp /etc/apt/sources.list.bak /etc/apt/sources.list")
        
    
    def __search_debian_version(self):
        lista = []
        lineas = open("/etc/apt/sources.list").readlines()
        for i in range(len(lineas)):
            if string.find(lineas[i][:-1],"deb http://") <> -1 :
                lista.append(string.splitfields(lineas[i][:-1]," "))
        for i in range(len(lista)):
            if lista[i][2] in versiones:
                version = lista[i][2]
            else:
                version = ""
        return version
    
                
        
        
	def __update(self):
		su.ejecutar("aptitude update")


	def __install(self,paquetes):
		if type(paquetes) is StringType:
			if string.find(paquetes,",") <> -1:
				print "La lista de paquetes no esta separada por espacios"
			else:
       				r = su.ejecutar("aptitude install %s" %paquetes)
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
	aptitude = apt
	apt.main("accesibilidad")
