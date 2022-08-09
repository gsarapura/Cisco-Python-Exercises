def read_int(min, max, prompt):
    """It prints whether the prompted integer is within the range specified.
    It asks the user to prompt again in case of AssertionError and ValueError.

    Args:
        prompt: The integer to check.
        min (int): The minimum level.
        max (int): The maximum level.
    """
    try:
        min = int(input(min))
        max = int(input(max))
        assert min <= max, 'Min must be less or equal than max'
        prompt = int(input(prompt))
        assert prompt >= min and prompt <= max
        print("Yes, it is within the range specified.")
    except AssertionError:
        print("Error: prompt is not within the range specified.")
        # Is this recursiveness allowed?
        read_int("Enter minimum level: ", "Enter maximum level: ", "Enter an integer value between minimum and maximum levels: ")
    except ValueError:
        print("Error: invalid prompt.")
        # Is this recursiveness allowed?
        read_int("Enter minimum level: ", "Enter maximum level: ", "Enter an integer value between minimum and maximum levels: ")

read_int("Enter minimum level: ", "Enter maximum level: ", "Enter an integer value between minimum and maximum levels: ")