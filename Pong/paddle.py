from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.seth(90)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)

