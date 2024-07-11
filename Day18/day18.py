import colorgram
from turtle import Turtle, Screen
import random


t = Turtle()
t.hideturtle()
t.speed("fastest")
screen = Screen()
screen.colormode(255)
colors = colorgram.extract('img.png', 10)


def align_turtle(n):
    t.up()
    t.setheading(225)
    t.forward(n * 30)
    t.setheading(0)
    t.down()


def print_color():
    color = random.choice(colors).rgb
    t.down()
    t.dot(20, color)
    t.up()



def next_line(pos_init):
    pos = t.pos()
    t.sety(pos[1] + 40)
    print(pos)
    if not pos[0] == pos_init:
        t.setheading(180)
    else:
        t.setheading(0)


def damien_hirst(n):
    align_turtle(n)
    pos_init = t.pos()
    for i in range(n):
        for j in range(n):
            print_color()
            t.forward(40)
        print_color()
        next_line(pos_init[0])





damien_hirst(15)


screen.exitonclick()