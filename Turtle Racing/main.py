from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(500,500)
user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win a race (purple, orange, red, blue)?:")

don = Turtle(shape="turtle")
don.color("purple")

mike = Turtle(shape="turtle")
mike.color("orange")

raph = Turtle(shape="turtle")
raph.color("red")

leo = Turtle(shape="turtle")
leo.color("blue")


turtles = [don, mike, raph, leo]
jump_value = [1,2,3,4,5,10]


for turtle in turtles:
    turtle.penup()


don.goto(x=-230, y=-100)
mike.goto(x=-230, y=-50)
raph.goto(x=-230, y=-0)
leo.goto(x=-230, y=50)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() >230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win {user_bet}" )
            else:
                print(f"You lose {user_bet}, {winning_color} win")

        random_jump = random.choice(jump_value)
        turtle.forward(random_jump)

screen.exitonclick()

