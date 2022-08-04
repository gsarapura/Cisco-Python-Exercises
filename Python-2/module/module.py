#! /usr/bin/python3.10 => ./main.py on terminal. Remeber to chmod 764 main.py

"""Ejemplo de módulo"""

__counter = 0 # times this module has been called

def sum1(the_list):
    global __counter
    __counter += 1
    the_sum = 0
    for element in the_list:
        the_sum += element
    return the_sum

def prod1(the_list):
    global __counter
    __counter += 1
    prod = 1
    for element in the_list:
        prod *= element
    return prod
    
print(__name__)
if __name__ == "__main__": # to be interpreted only in module.py / "module" to be interpreted in main.py
    print("Estoy en un módulo. Puedo hacer unas cuentas.")
    my_list = [i+1 for i in range(5)]
    print(sum1(my_list) == 15)
    print(prod1(my_list) == 120)