import random

num = random.randint(1, 6)

def fact(num):
    if num == 0 or num == 1:   # base case
        return 1
    return num * fact(num - 1)

print(f"Random number: {num}")
print(f"Factorial: {fact(num)}")
