# Demostración del método capitalize():
print('aBcD'.capitalize())
print('alPHsa sOns todEs'.capitalize())

# Demostración del método center():
print('[' + 'alpha'.center(10) + ']')
# Variant:
print('[' + 'gamma'.center(20, '*') + ']')

# Demostración del método endswith():
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")

# Demostración del método find():
print("Eta".find("ta"))
print("Eta".find("mma"))

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)

# Variant:
print('kappa'.find('a', 1, 4))
# -1 since a is on index 1.
print('kappa'.find('a', 2, 4))

# Demostración del método the isalnum():
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

t = 'Six lambdas'
print(t.isalnum()) # False due to space.
t = 'ΑβΓδ'
print(t.isalnum())
t = '20E1'
print(t.isalnum())

# Ejemplo 1: Demostración del método isapha():
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Ejemplo 2: Demostración del método isdigit():
print('2018'.isdigit())
print("Year2019".isdigit())

# Ejemplo 1: Demostración del método islower():
print("Moooo".islower())
print('moooo'.islower())

# Ejemplo 2: Demostración del método isspace(:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Ejemplo 3: Demostración del método isupper():
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# Demonstrating the join() method:
print("/".join(["omicron", "pi", "rho"]))

# Demostración del método lower():
print("SiGmA=60".lower())

# Demostración del método the lstrip():
print("[" + " tau ".lstrip() + "]")
# Variant:
print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".lstrip(".org"))

# Demostración del método replace():
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

# Demostración del método rfind():
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

# Demostración del método rstrip():
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

# Demostración del método split():
print("phi       chi\npsi".split())

# Demostración del método startswith():
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

# Demostración del método strip():
print("[" + "   aleph   ".strip() + "]")

# Demostración del método swapcase():
print("Yo sé que no sé nada.".swapcase())

print()

# Demostración del método title():
print("Yo sé que no sé nada. Part 1.".title())

print()

# Demostración del método upper():
print("Yo sé que no sé nada. Part 2.".upper())