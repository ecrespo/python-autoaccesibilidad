#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Name: sincronizar
Description: Modulo que sincroniza el sistema de archivos del repositorio local con el mirror www.crespo.info.ve/debian/
Version:0.1
License: GPLv3
Copyright: Copyright (C) 2009 Proyecto Libre Accesibilidad - Distrito Socialista Tecnologico AIT PDVSA  <moderador@libreaccesibilidad.org>
Author: Ernesto Nadir Crespo Avila
Email: ernesto@libreaccesibilidad.org
"""
import pdb
import privilegios

def actualizar():
    privilegios.ejecutar("rsync -avz rsync://nevado.crespo.info.ve/accesibilidad debian/")


if __name__ == "__main__":
    actualizar()


