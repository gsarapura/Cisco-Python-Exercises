# A natural number is prime if it is greater then 1 and has no divisors other than 1 and itself.
# Find the prime number:
# Expected output: 2 3 5 7 11 13 17 19

def is_prime(num):
    # With this code, 2 return False.
    # for i in range(2, num):
    #     if num % i == 0:
    #         return False
    #     else:
    #         return True
    divisor = 2
    while divisor < num: # Check for improvement with square root => x0.5
        if num % divisor == 0:
            return False
        divisor += 1
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()