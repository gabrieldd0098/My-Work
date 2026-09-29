from turtle import *
import random

screen = Screen()
screen.colormode(255)

directions = [0, 90, 180, 270, 360, 720 -90, -180, -270, -360, -720]
num_sides = 9

def cs():
    #clear the screen and reset pen position
    tammy.clear()
    tammy.penup()
    tammy.goto(0,0) #alternatively use .home()
    tammy.pendown()

def rc():
    # random rgb color tuple
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rc = (r, g, b)
    return rc

def ds(num_sides): #draw shape
    angle = 360 / num_sides
    for _ in range(num_sides):
        tammy.forward(100)
        tammy.right(angle)

def spiro(gap_size):
    for _ in range(int(random.randint(360, 721) // gap_size)):
        tammy.color(rc())
        tammy.circle(random.randint(1, 100))
        tammy.setheading(tammy.heading() + gap_size)

#initial defining
screen.bgcolor(rc())
tammy = Turtle()
tammy.shape("triangle")
tammy.color(rc())
tammy.setheading(90)
tammy.pensize(2)
tammy.width(2)
tammy.speed("fastest")

for _ in range(4): #square
    tammy.forward(100)
    tammy.left(90)

for _ in range(25): #dotted line
    tammy.forward(-5)
    tammy.penup()
    tammy.forward(-5)
    tammy.pendown()

cs()

#trippy
for shape_side_n in range(3, 11):
    tammy.color(rc())
    ds(num_sides = shape_side_n)

cs()

tammy.pensize(3)
#random walk
for _ in range(300):
    tammy.color(rc())
    tammy.forward(random.randint(-30, 30))
    tammy.setheading(random.choice(directions))

cs()

tammy.pensize(1)
spiro(gap_size = random.randint(1, 10))

cs()

#next

screen.exitonclick()
