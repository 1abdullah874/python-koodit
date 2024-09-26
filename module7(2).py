"""""
Module 7


Exercise 1

def season(month):
    seasons = ("Winter", "Spring", "Summer", "Autumn")

    if month in (12, 1, 2):
       return seasons[0]
    elif month in (3, 4, 5):
        return seasons[2]
    elif month in (6, 7, 8):
        return seasons[2]
    else:
        return seasons[3]

month = int(input("Enter a month: "))
season = season(month)
print(season)

Exercise 2

def name():
    names = set()

    while True:
        name = input("Enter a name (or press enter to quit): ")
        if name == "":
            break

        if name in names:
            print("Name already in use")

        else:
            print("New name in set")
            names.add(name)

        print("\nList of names: ", names)

name()


Exercise 3


airports = {
    "EFHK" : "helsinki-vantaa airport"
}

while True:
    airport_code = str(input("Enter a airport name you would like to get (or press enter to quit): "))
    if airport_code == "":
        break
    elif airport_code in airports:
        print(airports[airport_code])
    elif airport_code not in airports:
        code = str(input("Enter a valid ICAD code: "))
        airports[code] = airport_code
    else:
        print("Invalid airport code")

print(airports)

"""