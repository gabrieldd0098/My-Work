import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("CROSSY ROAD")
screen.tracer(0)
screen.bgcolor("black")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, key= "space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars: #getting run over
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_crossed(): #reach finish line
        player.send_back()
        car_manager.speed_up()
        scoreboard.increase_level()

screen.exitonclick()
