from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__() #inherits
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.send_back()
        self.setheading(90) #north

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def send_back(self):
        self.goto(STARTING_POSITION)

    def is_crossed(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
