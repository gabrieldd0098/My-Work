from turtle import Turtle, Screen
import random

is_racing = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="BET! BET! BET!", prompt="Which color shall win? red, orange, yellow, green, blue, "
                                                           "black, or purple? ")
r_colors = ["red", "orange", "yellow", "green", "blue", "black", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80, 110]
all_racers = []

for t_index in range(0, 7):
    racer = Turtle(shape="turtle")
    racer.color(r_colors[t_index])
    racer.penup()
    racer.goto(x=-230, y=y_pos[t_index])
    all_racers.append(racer)
    racer.pendown()

if user_bet:
    is_racing = True

while is_racing:
    for turt in all_racers:
        if turt.xcor() > 230:
            is_racing = False
            win_color = turt.pencolor()
            if win_color == user_bet:
                print(f"YOU'VE WON! {win_color} color racer wins!")
            else:
                print(f"YOU'VE LOST! You chose {user_bet} but {win_color} color racer wins!")

        rnd_dist = random.randint(0, 10)
        turt.forward(rnd_dist)

screen.exitonclick()
