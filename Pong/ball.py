from turtle import Turtle, Screen
import random

random_starts = [2, 3, -2, -3]
random_num_1 = random.choice(random_starts)
random_num_2 = random.choice(random_starts)


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.speed("slowest")
        self.penup()

        self.x_move = random_num_1
        self.y_move = random_num_2
        # self.angle = random.randint(1, 360)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1.1


    def reset_position(self):
        random_num_1 = random.choice(random_starts)
        random_num_2 = random.choice(random_starts)
        self.goto(0, 0)
        self.x_move = random_num_1
        self.y_move = random_num_2
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
