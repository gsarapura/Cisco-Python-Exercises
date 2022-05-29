# If income is not greater than 85.528 pesos, tax will be equal to 18% of income minus 556 pesos and 2 cents.
# if income is greater than 85.528 pesos, tax will be equal to 14.839 pesos and 2 cents, plus 32% of the surplus over 85.528.
# Note: remember that if tax equals 0, it just means that they don't have to pay taxes.

income = float(input("Type your income:"))

if income > 85528:
    tax = 14839.2 + (income - 85528) * .32
else:
    tax = income * .18 - 556.2


if tax >= 0:
    tax = round(tax, 0)
    print("Your tax is:", tax, "pesos")
else:
    print("Lucky you, no taxes")
