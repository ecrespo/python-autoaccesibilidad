#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Name: Users
Description: Modulo que captura los usuarios que existen en un equipo
Version:0.1
License: GPLv3
Copyright: Copyright (C) 2009  Ernesto Nadir Crespo Avila <ecrespo@debianvenezuela.org>
Author: Ernesto Nadir Crespo Avila
Email: ecrespo@debianvenezuela.org
"""

from pwd import getpwall 
from commands import getstatusoutput
from string import splitfields

def get_users():
    list = getpwall()
    users_pwd = []
    users = []
    result =  getstatusoutput("ls /home")
    directories = splitfields(result[1],"\n")
    for i in range(len(list)):
        if list[i][2] >= 1000:
            users_pwd.append(list[i][0])
    for i in range(len(users_pwd)):
        if users_pwd[i] in directories:
            users.append(users_pwd[i])
    return users
            

if __name__ == "__main__":
    get_users()
    
    