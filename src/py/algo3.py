import random


chosen_number = int(input("Enter a number: "))
random_number = random.randrange(10**(100-1), 10**100)
print(chosen_number/random_number)