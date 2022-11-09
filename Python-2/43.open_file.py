import errno

try:
    s = open("/home/gustavs/file.txt", "rt")
    # Processing.
    print(s.read())
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("Archive does not exist.")
    elif exc.errno == errno.EMFILE:
        print("Too many open archives.")
    else:
        print("Number error is:", exc.errno)
