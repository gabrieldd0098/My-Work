###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import turtle
import colorgram
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

color_list = rgb_colors #use this list
shape_list = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']

screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor(random.choice(color_list))

#Faux Damien Hirst
faux_d = turtle.Turtle()
faux_d.speed('fastest')
faux_d.penup()
faux_d.hideturtle()
faux_d.setheading(225)
faux_d.forward(300)
faux_d.setheading(0)
num_stamps = 100

for stamp_count in range(1, num_stamps + 1):
    faux_d.shape(random.choice(shape_list))
    faux_d.color(random.choice(color_list))
    # faux_d.dot(random.randint(1, 20), random.choice(rgb_colors))
    faux_d.stamp()
    faux_d.forward(50)

    if stamp_count % 10 == 0:
        faux_d.setheading(90)
        faux_d.forward(50)
        faux_d.setheading(180)
        faux_d.forward(500)
        faux_d.setheading(0)

screen.exitonclick()
