#!/bin/python

import sys
import os

args = sys.argv[1:] # Almacenamos en un array los argumentos de la terminal.

for arg in args:
	if arg == "-h" or arg == "--h" or arg == "-help" or arg == "--help":
		print("Método de uso:\n" + sys.argv[0] + " {directorio con las imágenes} {hash a comparar} {contraseña de stegosuite}")
		exit()

fotos=os.popen("ls " + args[0]).read().split() # Almacenamos en un array todas las imagenes del archivo dado.

# Compara los hashes de cada foto con el hash dado por el terminal.
for i in range(len(fotos)):
	if args[1]==os.popen("(md5sum \"" + args[0] + "/" + fotos[i] + "\" | awk \'{print $1}\')").read().strip("\n"):
		os.system("stegosuite extract " + args[0] + "/" + fotos[i] + " -k \"" + args[2] + "\"")
