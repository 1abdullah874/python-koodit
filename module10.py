from module9 import cars

import random


class Elevator:
    def __init__(self,top_floor, bottom_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = self.bottom_floor

    def go_to_floor(self, floor):
        if floor > self.top_floor or floor < self.bottom_floor:
            print("You have entered an invalid floor")
            return
        while floor > self.current_floor:
            self.floor_up()
        while floor < self.current_floor:
            self.floor_down()


    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"You are on {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"You are on {self.current_floor}")

el = Elevator(9,0)
el.go_to_floor(9)
el.go_to_floor(3)


class Building():
    def __init__(self,top_floor, bottom_floor, floor_num):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.no_of_floor= floor_num
        self.ele = []
        for i in range(floor_num):

            self.ele.append(Elevator(self.top_floor, self.bottom_floor))

    def run_elevator(self, el, destination_floor):
        if 0 <= el < self.no_of_floor:

            self.ele[el].go_to_floor(destination_floor)
            print(f"you are on {el} and your floor is {self.ele[el].current_floor}")
        else:
            print("You have entered an invalid floor")


    def fire_alarm(self):
        for i in self.ele:
            i.go_to_floor(self.bottom_floor)
        print("All of the elevators have been moved to bottom floor")

z = Building(9,3,5)
z.run_elevator(3,5)
z.fire_alarm()


class Race:
    def _init_(self, name, distance_km, cars):
        self.name = name
        self.distance_km = distance_km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change  = random.randint(-10,10)
            car.accelerate(speed_change)
            car.drive(1)

    def print_info(self):
        for car in self.cars:
            print(f"{car.Registration_number}: Speed = {car.current_speed}km/h"
              f"Distance = {car.distance_km}km")

    def race_fin(self):
        return
        any(car.travelled_distance >= self.distance_km for car in self.cars)

cars = [cars(f"ABD-{i+1}", random.radint(100, 200)) for i in range(10)]
race = Race("Barcelona Grand Prix")
hours_passed = 0
while not race.race_fin():
        race.hour_passes()
        hours_passed += 1
if hours_passed % 10 == 0:
    print(f"After {hours_passed} hours passed these are the stats {race.print_info()}")


race.print_info()
print(f"Barcelona Grand Prix finished after {hours_passed} hours")

