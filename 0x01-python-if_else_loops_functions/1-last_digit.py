#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
sign = 1 if number >= 0 else -1
print("Last digit of", number, "is", end=" ")
if last_digit > 5:
    print(sign * last_digit, "and is greater than 5")
elif last_digit == 0:
    print(last_digit, "and is 0")
else:
    print(sign * last_digit, "and is less than 6 and not 0")
