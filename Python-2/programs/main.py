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

# To the end of the tree:
import extra.good.best.sigma as sigma # Using alias makes life easier.
from extra.good.best.tau import FunT

print(sigma.FunS())
print(FunT())

# Working with zip files:
path.append('/home/gustavs/repo/Cisco-Python-Exercises/Python-2/Archivo_ZIP_Módulos_y_Paquetes/Extrapack_ZIP_file.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI
from extra.good.beta import FunB

print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())