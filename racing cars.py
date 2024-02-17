from random import uniform
import time


class Car:
    final_distance = 80
    race_time = 0

    def __init__(self, name, driver):
        self.name = name
        self.driver = driver
        self.speed = 0
        self.position = 0

    def update_position(self):
        self.position = self.speed * Car.race_time

    def update_time(self, race_time):
        Car.race_time = race_time

    def __str__(self):
        return f"{int(self.position)*'-'}{self.name}"


class BMW(Car):
    def __init__(self, name, driver, model, max_speed):
        super().__init__(name, driver)
        self.model = model
        self.speed = max_speed * 1.1 * (self.model/2020)


class Benz(Car):
    def __init__(self, name, driver, max_speed):
        super().__init__(name, driver)
        self.speed = max_speed * uniform(0.8, 1.2)


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


cars = [BMW('first bmw', Driver('mammad', 18), 2010, 200),
        Benz('first benz', Driver('ali', 25), 200),
        Benz('second benz', Driver('arsalan', 80), 200)]

winner_car = ''
race_time = 0
end_race = False
while not end_race:
    for car in cars:
        car.update_position()
        print(car)
        if car.position >= Car.final_distance:
            winner_car = car
            end_race = True
            break

    cars[0].update_time(race_time)
    time.sleep(2)
    race_time += 0.1

print(f"winner car is {winner_car.name}")