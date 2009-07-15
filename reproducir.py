#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Name: reproducir
Description: Programa principal que permite instalar aplicaciones accesibles de un repositorio local
Version:0.1
License: GPLv3
Copyright: Copyright (C) 2009 Proyecto Libre Accesibilidad - Distrito Socialista Tecnologico AIT PDVSA  <moderador@libreaccesibilidad.org>
Author: Ernesto Nadir Crespo Avila
Email: ernesto@libreaccesibilidad.org"""


import pygst
pygst.require("0.10")
import sys, gst, gobject
gobject.threads_init()


def main(args):
    if len(args) != 2:
        print "Uso: "+args[0]+" <fichero.ogg>"
        return -1
    pipestr = 'filesrc location=' + args[1] + ' ! oggdemux ! vorbisdec !'+'audioconvert ! alsasink '
    try:
        pipeline = gst.parse_launch(pipestr)
    except gobject.GError, e:
        print "No es posible crear la tuberia,", str(e)
        return -1
    def eventos(bus, msg):
        t = msg.type
        if t == gst.MESSAGE_EOS:
            loop.quit()
        elif t == gst.MESSAGE_ERROR:
            e, d = msg.parse_error()
            print "ERROR:", e
            loop.quit()
        return True
    pipeline.get_bus().add_watch(eventos)
    pipeline.set_state(gst.STATE_PLAYING)
    loop = gobject.MainLoop()
    try:
        loop.run()
    except KeyboardInterrupt: # Por si se pulsa Ctrl+C
        pass
    pipeline.set_state(gst.STATE_NULL)
    return 0
if __name__ == "__main__":
    sys.exit(main(sys.argv))

