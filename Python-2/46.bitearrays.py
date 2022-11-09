from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    binary_file = open('file.bin', 'wb')
    binary_file.write(data)
    binary_file.close()
except IOError as e:
    print("E/S error:", strerror(e.errno))

for b in data:
    print(hex(b))

