#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Name: ejecutar-root
Description: Modulo que permite la ejecución de comandos como root
Version:0.1
License: GPLv3
Copyright: Copyright (C) 2009 Proyecto Libre Accesibilidad - Distrito Socialista Tecnologico AIT PDVSA  <moderador@libreaccesibilidad.org>
Author: Ernesto Nadir Crespo Avila
Email: ecrespo@debianvenezuela.org
"""



import gksu2 as gksu
import gobject
import getpass

def ask_pass_func(context, prompt):
    try:
        return getpass.getpass("Enter root password: ")
    except KeyboardInterrupt:
        print
        err = gobject.GError("keyboard interrupt")
        err.code = gksu.ERROR_CANCELED
        err.domain = "libgksu"
        raise err

def ejecutar(comando):
    ctx = gksu.Context()
    ctx.set_command(comando)
    gksu.su_full(ctx, ask_pass=ask_pass_func)
