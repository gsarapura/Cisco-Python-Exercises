def mysplit(string):
    """Split a string into a list of strings.
    Space determines the end of the elements.

    Arg: 
    string
    Returns: 
    list of strings
    """
    split_list = []
    char_collector = ''
    # Iterating string:
    for char in string:
        if not char.isspace():
            char_collector += char # Collect characters.
        elif char_collector != '': # When char is not alpha check whether char_collector is empty.
            split_list.append(char_collector)
            char_collector = ''
    # Append missing characters
    if char_collector != '':
        split_list.append(char_collector)
    return split_list
    
print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))