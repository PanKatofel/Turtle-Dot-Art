from turtle import Turtle, Screen
from random import choice
import colorgram

# Pick a picture from which the colors will be selected
colors = colorgram.extract("example.jpg", 6)
bob = Turtle()
bob.penup()
bob.hideturtle()
bob.speed(0)

screen = Screen()
screen.colormode(255)


def get_random_color(colors):
    color = choice(colors).rgb
    return (color.r, color.g, color.b)


dot_size = 20
offset_x = dot_size * 2
offset_y = dot_size * 2
step = dot_size * 2

x = (screen.window_width() // -2) + offset_x
y = (screen.window_height() // -2) + offset_y
bob.setpos(x, y)

while bob.pos()[1] < (screen.window_height() // 2):
    while bob.pos()[0] < (screen.window_width() // 2):
        bob.pencolor(get_random_color(colors))
        bob.dot(dot_size)
        bob.forward(step)
    y += offset_y
    bob.teleport(x, y)

screen.exitonclick()

