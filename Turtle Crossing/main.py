import time
from turtle import Screen
from player import Player, STARTING_POSITION, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
car_manager.hideturtle()
car_manager.penup()
car_manager.goto(300, -300)

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "w")
screen.onkeypress(player.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.gameover()
            game_is_on = False

    if player.finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.scoring()


screen.exitonclick()
