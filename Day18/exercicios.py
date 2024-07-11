#
from turtle import Turtle, Screen
import random

screen = Screen()

t = Turtle()
t.width(1)
t.speed("fastest")


# t.begin_fill()
# while True:
#     t.forward(200)
#     t.left(90)
#     if abs(t.pos()) < 1:
#         t.end_fill()
#         break

# while True:
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()
#     t.left(10)
#     if abs(t.pos()) < 1:
#         break

screen.colormode(255)

# for n in range(3, 11):
#     t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     for _ in range(n):
#         t.forward(100)
#         t.right(360/n)




#
# def random_walk(n):
#     t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     direct = random.choice([0, 90, 180, 270])
#     t.forward(n)
#     t.setheading(direct)
#
#
# while True:
#     random_walk(25)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_circle(gap):
    for _ in range(int(360/gap)):
        t.color(random_color())
        t.circle(150)
        t.right(gap)

draw_circle(8)



screen.exitonclick()