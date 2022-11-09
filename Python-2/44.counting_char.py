from os import strerror

print("Using while:")
try:
    counter = 0
    stream = open('/home/gustavs/file.txt', "rt")
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\nNumber of characters:", counter)
except IOError as e:
    print("E/S error:", strerror(e.errno))

print("\nUsing read() (be careful it requires a lot of memory, so in case of bigger archives, it can cause damage to your system)")
try:
    counter = 0
    stream = open('/home/gustavs/file.txt', "rt")
    content = stream.read()
    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    print("\nNumber of characters:", counter)
except IOError as e:
    print("E/S error:", strerr(e.errno))

from os import strerror

print("\nUsing readline()")
try:
    character_counter = line_counter = 0
    stream = open('/home/gustavs/file.txt', 'rt')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nNumber of characters:", character_counter)
    print("Number of lines:      ", line_counter)
except IOError as e:
    print("E/S error:", strerror(e.errno))

print("\nUsing readlines()")
from os import strerror

try:
    character_counter = line_counter = 0
    stream = open('/home/gustavs/file.txt', 'rt')
    lines = stream.readlines(20)
    while len(lines) != 0:
        for line in lines:
            line_counter += 1
            for char in line:
                print(char, end='')
                character_counter += 1
        lines = stream.readlines(10)
    stream.close()
    print("\nNumber of characters:", character_counter)
    print("Number of lines:      ", line_counter)
except IOError as e:
    print("E/S error:", strerror(e.errno))

print("\nUsing open")
try:
	character_counter = line_counter = 0
	for line in open('/home/gustavs/file.txt', 'rt'):
		line_counter += 1
		for char in line:
			print(char, end='')
			character_counter += 1
	print("\nNumber of characters: ", character_counter)
	print("Number of lines:     ", line_counter)
except IOError as e:
	print("E/S error:", strerror(e.errno))
