from turtle import Turtle, Screen
import random


race_on = False
screen = Screen()
screen.setup(width=500, height=400)
choice = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: :")
t_colors = ["red", "purple", "blue", "green", "yellow", "orange", "violet"]
t_flock = []

pos_y = -100
for _ in range(0, 7):
    t = Turtle(shape="turtle")
    t.color(t_colors[_])
    t_flock.append(t)
    t.up()
    t.goto(-240, pos_y)
    t.down()
    pos_y += 40


if choice:
    race_on = True


while race_on:
    rand_distance = random.randint(2, 8)
    rand_t = random.choice(t_flock)
    rand_t.up()
    rand_t.forward(rand_distance)
    if rand_t.xcor() > 220:
        t_color = rand_t.pencolor()
        if choice == t_color:
            screen.textinput(f"{t_color} wins! Your bet was right. :)", "")
        else:
            screen.textinput(f"{t_color} Wins! Your bet was wrong. :(", "")
        race_on = False



screen.mainloop()


