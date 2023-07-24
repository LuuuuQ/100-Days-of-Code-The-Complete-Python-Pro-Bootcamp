from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Down", fun=snake.down)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.scoring()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.gameover()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()

screen.exitonclick()
