#!/usr/bin/env python

# -*- coding: utf-8 -*-
#
"""Copyright (C) DST-Merida AIT-PDVSA- Accesibilidad para tod@s

 this program is free software: you can redistribute it and/or modify it
 under the terms of the GNU General Public License as published by the
 Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 this program is distributed in the hope that it will be useful, but
 WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 See the GNU General Public License for more details.

 You should have received a copy of the GNU General Public License along
 with this program.  If not, see <http://www.gnu.org/licenses/>.


Team developer:
Ernesto Crespo
julio Hernandez
Niriana Blasco
Jorge Ortega
Joel Gomez
Johan Trujillo

Module to Audio player 

"""


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

