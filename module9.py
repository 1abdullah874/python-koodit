import random


class Car:
    def __init__(self, Registration_number, max_speed, current_speed, travelled_distance):
        self.Registration_number = Registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, number_of_hours):
        self.travelled_distance += self.current_speed * number_of_hours

cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    car = Car(f"ABC-{i}", max_speed, current_speed="", travelled_distance="")
    cars.append(car)

race_hours = 10
for hour in range(race_hours):
    print(f" ---hour {hour + 1}---  ")
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        print(f"Reg number: {car.Registration_number}: || Current speed: {car.current_speed}km/h || travelled distance: {car.travelled_distance}")
print("\n - Final Results -")
for car in cars:
    print(f"{car.Registration_number} | Max speed: {car.max_speed}km/h |final distance: {car.travelled_distance}")

car = Car(Registration_number= "ABC-123", max_speed= 142,current_speed="", travelled_distance=0)
print(f"Registration number : {car.Registration_number}")
print(f"Maximum speed: {car.max_speed}")
print(f"Current speed: {car.current_speed}")
print(f"Travelled distance : {car.travelled_distance}")


car.accelerate(change_of_speed = 30)
print(f"Current speed after +30km/h : {car.current_speed} km/h")
car.accelerate(change_of_speed = 70)
print(f"Current speed after +70km/h : {car.current_speed} km/h")
car.accelerate(change_of_speed = 50)
print(f"Current speed after +50km/h : {car.current_speed} km/h")
car.accelerate(change_of_speed = -200)
print(f"Current speed after -200km/h Emergency break : {car.current_speed} km/h")

car.drive(1.5)
print(f"Travlled distance after 1.5 hours of driving at {car.current_speed} speed: {car.travelled_distance} km")



