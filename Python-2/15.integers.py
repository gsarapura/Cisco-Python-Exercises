def read_int(prompt, min, max):
    """Checks whether the prompt integer is within the range specified.
    Args:
        prompt: The integer to check.
        min (int): The minimum level.
        max (int): The maximum level.
    Returns:
        bool: True if the prompt integer is within the range specified.
    """
    try:
        assert int(prompt) >= min and int(prompt) <= max
        return True
    except AssertionError:
        print("Error: prompt is not within the range specified.")
    except ValueError:
        print("Error: invalid prompt.")
    
v = read_int(1, -10, 10)

if v:
    print("Yes, it is within the range specified.")
else:
    print("No, it is within the range specified.")
