#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Name: pyconfig
Description: Programa que permite modificar la configuracion de gnome por medio del modulo gconf de python
Version:0.1
License: GPLv3
Copyright: Copyright (C) 2009  Distrito Socialista Tecnologico AIT PDVSA Mérida
Author: Ernesto Nadir Crespo Avila
Email: ernesto@libreaccesibilidad.org
"""

import gconf


class Conf:
    def __init__(self):
        self.gconfClient = gconf.client_get_default()
        self.aplicaciones = ("orca", "gnome-terminal","oowriter","iceweasel","nautilus","ooimpress","pidgin","oocalc","gedit","gnome-calculator")
        self.comando = "/apps/metacity/keybinding_commands/command_"
        self.asignacion_teclado = "/apps/metacity/global_keybindings/run_command_"
        self.teclas = {"orca":"<Super>o","gnome-terminal":"<Super>t","oowriter":"<Super>w","iceweasel":"<Super>n","nautilus":"<Super>h","ooimpress":"<Super>i","pidgin":"<Super>p","oocalc":"<Super>x","gedit":"<Super>e","gnome-calculator":"<Super>c"}

        
    def modificar(self):
        cont = 1
        for aplicacion in self.aplicaciones:
            ruta1 =  "%s%s" %(self.comando,cont)
            ruta2 = "%s%s"  %(self.asignacion_teclado,cont)
            self.gconfClient.set_string(ruta1, "%s" %aplicacion)
            self.gconfClient.set_string(ruta2, "%s" %self.teclas[aplicacion])
            cont = cont +1
    
    def listar(self):
        cont = 1
        for aplicacion in self.aplicaciones:
            ruta1 =  "%s%s" %(self.comando,cont)
            ruta2 = "%s%s"  %(self.asignacion_teclado,cont)
            print self.gconfClient.get_string(ruta1),self.gconfClient.get_string(ruta2)
            cont = cont +1


if __name__ == "__main__":
    import sys
    config = Conf()
    if len(sys.argv) == 1 :
        print "pyconfig-orca options " 
        print "option : --help    : Print this help"
        print "option : --list    : List gconf for gnome-orca"
        print "option : --change  : Change gconf for gnome-orca"
    elif len(sys.argv) == 2:
        if sys.argv[1] == "--list" :
            config.listar()
        elif sys.argv[1] == "--change":
            config.modificar()
        elif sys.argv[1] == "--help" :
            print "pyconfig-orca options "
            print "option : --help    : Print this help"
            print "option : --list    : List gconf  for gnome-orca"
            print "option : --change  : Change gconf for gnome-orca"
        else:
            print "pyconfig-orca options "
            print "option : --help    : Print this help"
            print "option : --list    : List gconf  for gnome-orca"
            print "option : --change  : Change gconf for gnome-orca"
    else:
        print "pyconfig-orca options " 
        print "option : --help    : Print this help"
        print "option : --list    : List gconf for gnome-orca"
        print "option : --change  : Change gconf for gnome-orca"
        


    
    