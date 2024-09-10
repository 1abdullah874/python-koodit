""""
Module 4

Exercise 1:

i = 1
while i < 1001:
    if i % 3 == 0:
        print(i)
    i += 1

Exercise 2:

inches = float(input("Enter inches: "))
while inches > 0:
    centimeters = inches * 2.54
    print((centimeters))
else:
print("You entered a negative number")

Exercise 3:

largest = None
smallest = None

while True:
    usernumber = input("Enter a number or press enter to quit: ")

    if usernumber == "":
        break
    number = float(usernumber)
        if smallest is None or number<smallest:
            smallest = number
        if largest  is None or number>largest:
            largest = number

    except ValueError:
         print("Invalid input")

if smallest is not None and largest is not None:
    print(f"the smallest number is {smallest}")
    print(f"the largest number is {largest}")
else:
    print("You entered a invalid number")


Exercise 4:

import random

guess_number = random.randint(1, 10)

guessed_correct = False
print("Welcome to the game!")
print("I am thinking of a number between 1 and 10.")
while not guessed_correct:
    user_guess = int(input("Enter a number between 1 and 10: "))
    if user_guess < guess_number:
        print("Your guess is too low.")
    elif user_guess > guess_number:
        print("Your guess is too high.")
    else:
        print("You guessed correctly.")
        guessed_correct = True
        print("You win!")
        break

Exercise 5

username = "python"
password = "rules"
tries = 1
username = input("Enter your Username: ")
password = input("Enter your Password: ")
while tries < 5:
    if username == "python" and password == "rules":
        print("Welcome")
        break
    else:
        print("Invalid, Please try again")
        tries += 1
    username = input("Enter your Username: ")
    password = input("Enter your Password: ")
else:
    print("Access denied")

Exercise 6

import random

def estimated_pi(num):
    insidecircle = 0

    for i in range(num):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            insidecircle += 1

    piapprox = 4 * insidecircle/num
    return piapprox

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    piapprox = estimated_pi(num)
    print(f"approximation of pi after {num} is {piapprox}")
"""
