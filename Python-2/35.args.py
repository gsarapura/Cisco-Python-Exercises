# args =>  tuple of arguments given to the exception constuctor. 
# Some built-in exceptions require and arguments. Also your own exceptions may require one.

def print_args(args): #It receives the tuple.
    length = len(args)
    if length == 0:
        print('No arguments.')
    elif length == 1:
        print(args[0])
    else:
        print(str(args))
try: # First case without arguments.
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ' ,end=' : ')
    print_args(e.args)

try: # Second case with one argument.
    raise Exception("mi excepción")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)

try: # Third case with two arguments.
    raise Exception("mi", "excepción")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print_args(e.args)