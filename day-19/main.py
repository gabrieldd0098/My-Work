import turtle as tan

tan.Turtle()
tan.Screen()

def move_forwards():
    tan.forward(10)

def move_backwards():
    tan.backward(10)

def turn_left():
    tan.left(90)

def turn_right():
    tan.right(90)

tan.listen()
tan.onkeypress(key="w", fun=move_forwards)
tan.onkeypress(key="s", fun=move_backwards)
tan.onkeypress(key="a", fun=turn_left)
tan.onkeypress(key="d", fun=turn_right)
tan.exitonclick()
