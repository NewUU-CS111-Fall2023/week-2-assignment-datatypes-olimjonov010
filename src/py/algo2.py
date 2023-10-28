import random
chosen_number = random.randint(1,100)
number = int(input("Choose a nnumber: "))

while chosen_number != number:
    if number < chosen_number:
        print("too low")
        number = int(input("Choose a nnumber: "))

    if number > chosen_number:
        print("to high")
        number = int(input("Choose a nnumber: "))

print("Correct")