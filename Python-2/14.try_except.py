first_number = int(input("Ingresa el primer numero: "))
second_number = int(input("Ingresa el segundo numero: "))

try:
    print(first_number / second_number)
except:
    print("Esta operación no puede ser realizada.")

print("FIN.")

# Betterment:
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salió mal...")

print("FIN.")

# General or specific errors:
try:
    y = 1 / 0
except BaseException: # Most general BaseException => ArithmeticError => ZeroDivisionError.
    print("Uuupsss...")

print("FIN.")

# Raise (simulate exceptions):
def bad_fun(n):
    raise ZeroDivisionError


try:
    bad_fun(0)
except ArithmeticError:
    print("¿Que pasó? ¿Un error?")

print("FIN.")

# Raise inside except => twice
def bad_fun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise


try:
    bad_fun(0)
except ArithmeticError:
    print("¡Ya veo!")
# ZeroDivisionError is executed twice. First, here, then inside bad_fun() due to Raise.
print("FIN.")

# Assert:
import math

x = float(input("Ingresa un número: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)