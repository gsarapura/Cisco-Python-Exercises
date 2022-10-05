# Run time error.

def division(n):
    try: # This block will test the expected error to occur.
        n = 1 / n
    except ZeroDivisionError: # Here you can handle the error.
        print("Divison failed.")
        n = None
    else: # Executed only if there's no exception.
        print("Everything went well.")
    finally: # Executed regardless of anything.
        print("Time to say goodbye.")
        return n


print(division(2))
print(division(0))