# Interchange order of the first and the last elements. Keep the middle one.
# 100 elements.

lista = []

for i in range(100):
    lista.append(i+1)

times_done = len(lista)//2
length = len(lista)

for i in range(times_done):
    lista[i], lista[length - 1 - i] = lista[length - 1 - i], lista[i]

print(lista)
