# To work with "Archivo Zip Módulos_y_Paquetes"

from sys import path 
# it was needed to '//':
path.append('/home/gustavs/repo/Cisco-Python-Exercises/Python-2/Archivo_ZIP_Módulos_y_Paquetes')
# Check Path:
#for name in path:
    #print(name)

# extra is a packet
import extra.iota # Pylance gives error, but just add it to its path. Vscode tells you to add it.
print(extra.iota.FunI())

#Other alternative:
#from extra.iota import FunI

#print(FunI())