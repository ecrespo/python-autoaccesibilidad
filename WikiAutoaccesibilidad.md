# Introducción #

Este programa permitirá la instalación de aplicaciones accesibles en equipos con Debian ya instalados sin necesidad de tener una conexión a internet o un mirror en la red; es útil para laboratorios y centros de navegación.

Para los usuarios se tendrá 2 paquetes de Debian (metapaquete accesibilidad, accesibilidad-gnome-conf-spanish y accesibilidad-gnome-conf-english) que facilitará la instalación de sus equipos.

# Detalles #

La aplicación tendrá las siguientes características:
  * Desarrollado en python
  * Modular
  * Usará el módulo gksu de python para la instalación de paquetes de Debian, modificación del sources.list  y ejecutar un servidor web escrito en python.
  * Se agrega los directorios de configuración y un módulo para copiar las configuraciones a todos los usuarios.
  * Se incorpora un repositorio pequeño de debian que tendrá el metapaquete accesibilidad y las dependencias necesarias para así no necesitar un mirror de debian (un disco duro o conexión a internet).
  * Por los momentos sólo funcionará con Debian Squeeze y Sid, ya que el metapaquete accesibilidad funciona para esas dos versiones de Debian (problemas de dependencias y existencia de paquetes en Lenny), en un futuro se sacará una versión para lenny.
  * Tendrá la posibilidad de actualizar el repositorio de paquetes local para así no depender de versiones de paquetes y que se cambie la aplicación debido a esos cambios.
  * Todos los usuarios del equipo tendrán configurados el lector de pantalla incluyendo el usuario root.
  * El usuario puede decidir si el lector de pantalla hablará en Inglés o Español.
  * Los invidentes pueden utilizar el programa ya que el mismo tendrá accesibilidad (en desarrollo).

Los módulos que se necesitan son:
  * web.py : Inicia un servidor web.
  * privilegios.py : Facilita la ejecución de comandos como root pidiendo la clave de root.
  * users.py : Devuelve los usuarios que existen en el computador.
  * sincronizar.py : Módulo para sincronizar el repositorio local con el repositorio en www.crespo.info.ve/debian.
  * apt.py : Realiza cambios en el repositorio que usa el equipo e instala aplicaciones.
  * autoaccesibilidad.py : Programa principal que realiza la instalación de aplicaciones accesibles en un equipo utilizando un mirror y servidor web local.
  * config.py: La herramienta instala y configura el lector de pantalla orca y el lector por consola yasr.Se usará el módulo gconf de python.
  * reproducir.py: Programa que permite reproducir archivos ogg y mp3.

Contendrá 2 directorios:
  * conf: En este directorio se tendrá toda la configuración de la sesión del Escritorio Gnome, la configuración del lector de pantalla orca y cualquier otra configuración de la sesión del usuario.
  * debian: En este directorio se tendrá un repositorio local de paquetes de Debian que son necesarios para que un computador sea accesible.


Mirror principal:
Se tiene un mirror de Debian con los paquetes de accesibilidad en www.crespo.info.ve/accesibilidad. Para usarlo se agrega la siguiente línea en /etc/apt/sources.list .
deb http://www.crespo.info.ve/accesibilidad sid/squeeze main

Se creo un servidor rsync de sólo lectura para que los equipos actualicen la lista de paquetes de su repositorio local.