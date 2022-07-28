secret_number = 777

# It is  very simple program, but I think it is interesting to know the """ for strings
print(
    """ 
+==================================+
| Welcome to my game, muggle!      |
| Type in an integer number        |
| and guess what number I have     |
| chosen for you.                  |
| So,                              |
| what's the secret number?        |
+==================================+
""")

number = int(input("Guess the secret number... if you can... "))
while number != 777:
    print("Ha, ha! You are stuck in my loop!")
    number = float(input("C'mon, try again... "))
print("Well done, muggle! You are free... for now")
