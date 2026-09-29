import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "magenta"]
STARTING_MOVE_DISTANCE = random.randint(1, 5)
MOVE_INCREMENT = random.randint(5, 15)

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.spd = STARTING_MOVE_DISTANCE

    def create_cars(self):
        r_chance = random.randint(1, 10) #or 6
        if r_chance == 1:
            n_car = Turtle("square")
            n_car.shapesize(stretch_wid=1, stretch_len=2)
            n_car.penup()
            n_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            n_car.goto(300, random_y)
            self.all_cars.append(n_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def speed_up(self):
        self.spd += MOVE_INCREMENT
