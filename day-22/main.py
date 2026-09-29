from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("P O N G")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(left_paddle.go_up, key="w")
screen.onkeypress(left_paddle.go_down, key="s")

screen.onkeypress(right_paddle.go_up, key="Up")
screen.onkeypress(right_paddle.go_down, key="Down")

pong_is_on = True
while pong_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280: #touch wall
        ball.bounce_y()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() <
            -320): #touch paddle
        ball.bounce_x()

    if ball.xcor() > 380: #right-sided miss
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380: #left-sided miss
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
