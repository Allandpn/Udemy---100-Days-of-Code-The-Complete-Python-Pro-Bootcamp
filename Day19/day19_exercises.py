from turtle import Turtle, Screen

t = Turtle()

screen = Screen()

screen.setup(width=500, height=400)


screen.listen()

def t_forward():
    t.forward(5)

def t_backward():
    t.backward(5)


def t_c_clockwise():
    t.left(5)


def t_clockwise():
    t.right(5)


def t_clear():
    t.clear()
    t.up()
    t.home()
    t.down()



screen.onkeypress(fun=t_forward, key="w")
screen.onkeypress(fun=t_backward, key="s")
screen.onkeypress(fun=t_c_clockwise, key="a")
screen.onkeypress(fun=t_clockwise, key="d")
screen.onkeypress(fun=t_clear, key="c")




screen.mainloop()
# screen.exitonclick()

