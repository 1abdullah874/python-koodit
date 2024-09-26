"""""
exercise 1
import random

def roll_dice():
    return random.randint(1, 6)
def main():
    roll = 0
    while roll != 6:
        roll = roll_dice()
        print(roll)
if __name__ == '__main__':
    main()

exercise 2

import random
def roll_dice(sides):
    return random.randint(1, sides)
def main():
    sides = int(input("How many sides do you want? "))
    roll = 0
    while roll != sides:
        roll = roll_dice(sides)
        print(roll)
if __name__ == '__main__':
    main()

exercise 3

def gallons_liters(gallons):
    return gallons * 3.78541
def main():
    while True:
        gallons = float(input("How many gallons do you want?(negative value to quit the program): "))

        if gallons < 0:
            break
        liters = gallons_liters(gallons)
        print(liters)
    print("Conversion done")

if __name__ == '__main__':
    main()

exercise 4


def sumoflist(numbers):
    return sum(numbers)

def main():
    my_list = [1, 2, 3, 4, 5]
    result = sumoflist(my_list)
    print(result)
if __name__ == '__main__':
    main()



exercise 5


def remove_uneven_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
def main():
    originallist = [1, 2, 3, 4, 5]
    filteredlist = remove_uneven_numbers(originallist)
    print(f"original list: {originallist}")
    print(f"filtered list: {filteredlist}")
if __name__ == '__main__':
    main()


exercise 6

import math


def unitprice(diameter, price):
    radius = diameter / 2
    area = math.pi * (radius ** 2) / 1_000_000
    return price / area
def main():
    diameter = float(input("How many diameter do you want of your pizza in cm? "))
    price1 = float(input("enter the price of the first pizza in euros: "))

    diameter2 = float(input("enter the diameter of the second pizza in euros: "))
    price2 = float(input("enter the price of the second pizza in euros: "))

    unit_price1 = unitprice(diameter, price1)
    unit_price2 = unitprice(diameter2, price2)

    if unit_price1 < unit_price2:
        print(
            f"The first pizza provides better value for money with a unit price of {unit_price1:.2f} euros per square meter.")
    elif unit_price2 < unit_price1:
        print(
            f"The second pizza provides better value for money with a unit price of {unit_price2:.2f} euros per square meter.")
    else:
        print(f"Both pizzas have the same unit price of {unit_price1:.2f} euros per square meter.")

if __name__ == '__main__':
    main()
    """
