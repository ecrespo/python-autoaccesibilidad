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

def conf_escritorio():
    teclas = {"orca":"<Super>o","gnome-terminal":"<Super>t","oowriter":"<Super>w","iceweasel":"<Super>n","nautilus":"<Super>h","ooimpress":"<Super>i","pidgin":"<Super>p"}
    cont = 1
    comandos = ("gconftool-2 --set --type string /apps/metacity/keybinding_commands/command_",
                "gconftool-2 --set --type string /apps/metacity/global_keybindings/run_command_" )
    aplicaciones = ("orca","gnome-terminal","oowriter","iceweasel","nautilus","ooimpress","pidgin")
    r = getstatusoutput("echo $USER")
    privilegios.AgregarUsuarioSudo(r[1])
    usuarios = users.get_users()
    privilegios.ejecutar("cp -R ./conf/.* /etc/skel/")
    for usuario in usuarios:
        privilegios.ejecutar("cp -R ./conf/.*  /home/%s/" %usuario)
        privilegios.ejecutar("chown -R %s.%s /home/%s/.*" %(usuario,usuario,usuario))
        for aplicacion in aplicaciones:
            r = getstatusoutput("sudo -u %s %s%s \"%s\"  " %(usuario,comandos[0],cont,aplicacion))
            s = getstatusoutput("sudo -u %s %s%s \"%s\"" %(usuario,comandos[1],cont,teclas[aplicacion]))
            if r[0] <> 0 or s[0]: print "Error al cambiar los accesos rápidos de  %s" %aplicacion
            cont = cont + 1
        
if __name__ == "__main__":
    conf_escritorio()
    
