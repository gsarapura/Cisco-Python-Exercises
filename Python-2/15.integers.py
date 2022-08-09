def read_int(prompt, min, max):
    """Checks whether the prompted integer is within the range specified.
    Args:
        prompt: The integer to check.
        min (int): The minimum level.
        max (int): The maximum level.
    """
    try:
        prompt = input(prompt)
        assert int(prompt) >= min and int(prompt) <= max
        print("Yes, it is within the range specified.")
    except AssertionError:
        print("Error: prompt is not within the range specified.")
    except ValueError:
        print("Error: invalid prompt.")
    
v = read_int("Enter an integer value betwee -10 and 10: ", -10, 10)

