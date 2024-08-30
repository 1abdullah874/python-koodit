"""""
Module 3
Exercise 1
Sizelimit = 42
Zanderslength = float(input("Enter the length of the zander: "))
if Zanderslength >= Sizelimit:
    print("You can keep the fish")
else:
    print("Put the fish back into the lake")
    howshort= Sizelimit - Zanderslength
    print(f"the fish was {howshort} short of 42 cm")




Exercise 2
CabinClass = input("Enter your class of cruise cabin(LUX, A, B, C):")
if CabinClass == "lUX":
    print("Upper-deck cabin with a balcony.")
elif CabinClass == "A":
    print("Above the car deck, equipped with a window.")
elif CabinClass == "B":
    print("Windowless cabin above the car deck.")
elif CabinClass == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class")



Exercise 3
Gender = input("Enter your gender(Male, Female):")
HB_level = int(input("Enter you hemoglobin level:"))
if Gender == "Male" and 134 <= HB_level <= 150:
    print("normal hemoglobin level")
else:
    print("Your hemoglobin level is higher than your normal hemoglobin level")
    if Gender == "Female" and 117 <= HB_level <= 134:
        print("normal hemoglobin level")
    else:
        print("Your hemoglobin level is lower than your normal hemoglobin level")

Exercise 4
Year = input("Enter your year for checking if it is leap year: ")
if Year % 4 == 0:
    print("the year is leap year")
elif Year % 100 == 0 and Year % 400 != 0:
    print("the year is leap year")
else: print("the year is not leap year")
"""
