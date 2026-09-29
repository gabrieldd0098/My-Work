from turtle import Turtle
import random

possible_colors = ["red", "orange", "yellow", "green", "blue", "violet", "brown", "purple"]
possible_shapes = ["square", "circle"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color_shape_size()
        self.refresh()

    def color_shape_size(self):
        self.color(random.choice(possible_colors))
        self.shape(random.choice(possible_shapes))
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def refresh(self):
        self.color_shape_size()
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
