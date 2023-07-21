from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()


def move_forward():
    tim.forward(20)

def move_back():
    tim.back(20)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def screen_clear():
    tim.reset()


screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="Down", fun=move_back)

screen.onkey(key="c", fun=screen_clear)

screen.exitonclick()