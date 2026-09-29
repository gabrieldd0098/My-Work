from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.lvl = 0
        self.penup()
        self.goto(-280,250) #250 or 200
        self.color("white")
        self.upd()

    def upd(self):
        self.clear()
        self.write(arg=f"🐢 LEVEL: {self.lvl}", move=False, align="left", font=FONT)

    def increase_level(self):
        self.lvl += 1
        self.upd()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="🙁 YOU GOT RUN OVER 😭", move=False, align="center", font=FONT)
