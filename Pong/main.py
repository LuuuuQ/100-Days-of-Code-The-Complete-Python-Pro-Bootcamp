from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()

paddle_1 = Paddle((-360, 0))
paddle_2 = Paddle((360, 0))
ball = Ball()

screen.listen()
screen.onkeypress(paddle_1.go_up, "w")
screen.onkeypress(paddle_1.go_down, "s")
screen.onkeypress(paddle_2.go_up, "Up")
screen.onkeypress(paddle_2.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    if ball.ycor() > 287 or ball.ycor() < - 280:
        ball.bounce_y()

    if ball.distance(paddle_2) < 50 and ball.xcor() > 340 or ball.distance(paddle_1) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.scoring_r()

    elif ball.xcor() < -390:
        ball.reset_position()
        scoreboard.scoring_l()

screen.exitonclick()
