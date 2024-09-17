"""""
Exercise 1

import random
rolls = int	(
		 input("How many dice would you like to roll? "))
total_sum = 1
for roll
in range(rolls):
	roll = random.randint(1, 6)
		total_sum += roll
		print(f "the sum of rolling {rolls} dice is {total_sum}")


exercise 2


numbers =[]
while True:
		user_number = input("Enter any number (or press enter to quit): ")
		if user_number== "":
				break
numbers.sort(reverse = True)
top_five =[]

for i in range(min(5, len(numbers))):
	top_five.append(numbers[i])
print(f"the top five numbers are {top_five}")


exercise 3

def isprime(number):
	if number <= 1:
		return False
	for i in range(2, int(number**0.5) + 1):
		if number % i == 0:
			return False
	return True
num = int(input("Enter a number: "))
if isprime(num):
	print(f"{num} is a prime number")
else:
	print(f"{num} is not a prime number")



exercise 4


cities = []
for i in range(5):
	city  = input(f"Enter a city{i + 1}: ")
	cities.append(city)
print(cities)
for city in cities:
	print(city)

	"""

