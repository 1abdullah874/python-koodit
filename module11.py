from module9 import Car
"""class Publication:
    def __init__(self, pub_type, name):
        self.type = pub_type
        self.name = name

    def print_information(self):
        print(f"{self.type} - {self.name}")

class Magzine(Publication):
    def __init__(self, name, cheif):
        super().__init__("magzine", name)
        self.cheif = cheif

    def print_information(self):
        super().print_information()
        print(f"editor: {self.cheif}")
class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__("book", name)
        self.page_count = page_count
        self.author = author

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}")
        print(f"page_count: {self.page_count}")


publication = Publication("book", "Ugly Love")
publication.print_information()


magzine = Magzine("Aku Ankka", "Aki hyyppä")
magzine.print_information()

book = Book("Compartment No. 6", "Rosa Liksom", "192")
book.print_information()

pub_list = (publication, magzine, book)
for item in pub_list:
    item.print_information()"""


class Electric(Car):
    def _init_(self, regi_num, max_speed, capacity):
        super()._init_(regi_num, max_speed)
        self.capacity = capacity

    def print_drive(self):
        print(f"Distance by electric car: {self.travelled_distance} km")


class Gasoline(Car):
    def _init_(self, regi_num, max_speed, litres):
        super()._init_(regi_num, max_speed)
        self.litres = litres

    def print_drive(self):
        print(f"Distance by Gasoline Car: {self.travelled_distance} km")


electric = Electric("ABD-102", 180, 52.5, travelled_distance=0)
gasoline = Gasoline("ABD-101", 165, 32.3, travelled_distance=0)

electric.accelerate(99)
electric.drive(4)
electric.print_drive()

gasoline.accelerate(99)
gasoline.drive(5)
gasoline.print_drive()