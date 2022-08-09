def read_int(prompt, min, max):
    """It prints whether the prompted integer is within the range specified.
    It asks the user to prompt again in case of AssertionError and ValueError.
    
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
        # Is this recursiveness allowed?
        read_int("Enter an integer value between -10 and 10: ", -10, 10)
    except ValueError:
        print("Error: invalid prompt.")
        # Is this recursiveness allowed?
        read_int("Enter an integer value between -10 and 10: ", -10, 10)

read_int("Enter an integer value between -10 and 10: ", -10, 10)