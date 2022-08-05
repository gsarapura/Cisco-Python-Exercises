# \ does not count:
from tkinter import X


i_am = 'I\'m'
print(len(i_am))

# \n is invisible:
multiline = '''Line #1 
Line #2''' # Line # 1 \n => 8 characters and Line # 2 => 7 characters. 
print(len(multiline))

str1 = 'a'
str2 = 'b'
print(str1+str2)
print(str2+str1)
print(5 * 'a')
print('b' * 4)

# ord() only works with one character.
print(ord('α'))
print(ord(' '))

# chr()
print(chr(97))
print(chr(76))

print(chr(ord('x')) == 'x')
print(ord(chr(120)) == 120)

# Indexing chains:
the_string = 'silly walks'
for ix in range(len(the_string)):
    print(the_string[ix], end='')

# Iterating chains:
the_string = 'piluso goes'
for character in the_string:
    print(character, end='')

# Rebanadas

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

# Operator in and not in:
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)
print("F" not in alphabet)

# Since chains are inmutable:
# del[] (except deleting all the chain), append() or insert() are not allowed