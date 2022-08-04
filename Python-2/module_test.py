"""Module in another folder"""

def resta(n1, n2):
    return n1 - n2

# Avoid execute this module as a regular script. 
import sys

if __name__ == "__main__":
    print("¡No hagas eso!")
    sys.exit()