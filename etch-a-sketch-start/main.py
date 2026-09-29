from turtle import Turtle, Screen
#Etch-A-Sketch project

EAS = Turtle()
screen = Screen()

def move_forwards():
    EAS.forward(10)

def move_backwards():
    EAS.backward(10)

def turn_left():
    EAS.left(10)

def turn_right():
    EAS.right(10)

def clear_reset():
    EAS.clear()
    EAS.reset()

screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="c", fun=clear_reset)

screen.exitonclick()
