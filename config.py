#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Name: config
Description: Modulo que permite copiar la configuracion a las cuentas de los usuarios en el equipo
Version:0.1
License: GPLv3
Copyright: Copyright (C) 2009  Ernesto Nadir Crespo Avila <moderador@libreaccesibilidad.org>
Author: Ernesto Nadir Crespo Avila
Email: ernesto@libreaccesibilidad.org
"""


import pdb
import users
import privilegios
from commands import getstatusoutput

def conf_escritorio(idioma):
    archivos_home = "{config,gconf,gconfd,gnome,gnome2,gnome2_private,orca}"
    archetc = "{speech-dispatcher,yasr}"
    if idioma == "english":
        archivos_configuracion = "./conf/home/es/."
        archivos_etc = "./conf/etc/en/"
    else:
        archivos_configuracion = "./conf/home/es/."
        archivos_etc = "./conf/etc/es/"
    teclas = {"orca":"<Super>o","gnome-terminal":"<Super>t","oowriter":"<Super>w","iceweasel":"<Super>n","nautilus":"<Super>h","ooimpress":"<Super>i","pidgin":"<Super>p"}
    cont = 1
    comandos = ("gconftool-2 --set --type string /apps/metacity/keybinding_commands/command_",
                "gconftool-2 --set --type string /apps/metacity/global_keybindings/run_command_" )
    aplicaciones = ("orca","gnome-terminal","oowriter","iceweasel","nautilus","ooimpress","pidgin")
    r = getstatusoutput("echo $USER")
    usuarios = users.get_users()
    print "Copiando los archivos de configuración a /etc/skel"
    r = getstatusoutput("mpg123 voces/05.mp3")
    privilegios.ejecutar("cp -R  %s /etc/skel/.%s" %(archivos_configuracion,archivos_home))
    print "Copiando los archivos de configuración a /etc/"
    r = getstatusoutput("mpg123 voces/05.mp3")
    privilegios.ejecutar("cp -R %s%s /etc/"  %(archivos_etc,archetc))
    usuarios.append("root")
    for usuario in usuarios:
        if usuario == "root":
            home = "/root"
        else:
            home = "/home/%s" %usuario
        r = getstatusoutput("mpg123 voces/03.mp3")
        print "Configurando el lector de pantalla al usuario: %s" %usuario
        privilegios.ejecutar("cp -R %s%s  %s" %(archivos_configuracion,archivos_home,home))
        privilegios.ejecutar("chown -R %s.%s %s/.%s" %(usuario,usuario,home,archivos_home))
        for aplicacion in aplicaciones:
            print "Configurando la aplicación: %s" %aplicacion
            r = getstatusoutput("mpg123 voces/04.mp3")
            r = getstatusoutput("sudo -u %s %s%s \"%s\"  " %(usuario,comandos[0],cont,aplicacion))
            s = getstatusoutput("sudo -u %s %s%s \"%s\"" %(usuario,comandos[1],cont,teclas[aplicacion]))
            if r[0] <> 0 or s[0] <> 0:
                print "Error al cambiar los accesos rápidos de  %s" %aplicacion
                r = getstatusoutput("mpg123 voces/07.mp3")
            cont = cont + 1
        
if __name__ == "__main__":
    conf_escritorio("español")
    
