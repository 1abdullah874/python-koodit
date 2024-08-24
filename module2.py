name = input("Enter your name: ")
print("Hello," + name + "!")

import math
radius = float(input(f"Enter your radius of the circle: "))
print("the area of the circle is:", math.pi * radius * radius)

Length = float(input("Enter your length: "))
Width = float(input("Enter your width: "))
area = Length * Width
perimeter = 2 * (Length + Width)
print("The perimeter of the circle is:", perimeter)
print("The area of the circle is:", area)

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))
Sum= num1 + num2 + num3
average =Sum//3
product = num1 * num2 * num3
print("The average number of the circle is:", average)
print("The product number of the circle is:", product)
print("The sum number of the circle is:", Sum)

talents = float(input("Enter your number of talents: "))
lots = float(input("Enter your number of lots: "))
pounds = float(input("Enter your number of pounds: "))

Lots1 = pounds * 32
lots2 = pounds * 32
pounds1 = talents * 20

grams1 = lots * 13.3
grams2 = lots2 * 13.3
grams3 = lots * 13.3
totalkilo = grams1 + grams2 + grams3
grams = totalkilo % 1000
kilograms = int((totalkilo - grams)/ 1000)
print("Weight in modern unit is", kilograms,f"kg and{grams: .2f} g")