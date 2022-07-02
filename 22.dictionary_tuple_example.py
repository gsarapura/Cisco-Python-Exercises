# Necesitas un programa para calcular los promedios de tus alumnos.
# El programa pide el nombre del alumno seguido de su calificación.
# Los nombres son ingresados en cualquier orden.
# El ingresar un nombre vacío finaliza el ingreso de los datos (nota 1: ingresar una puntuación vacía generará la excepción ValueError, 
# pero no te preocupes por eso ahora, verás cómo manejar tales casos cuando hablemos de excepciones en el segundo parte de la serie del curso).
# Una lista con todos los nombre y el promedio de cada alumno debe ser mostrada al final.

school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
        break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

print(school_class)       

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)

