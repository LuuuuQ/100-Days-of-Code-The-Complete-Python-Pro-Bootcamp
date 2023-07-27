from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 300


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("black")
        self.speed("fastest")
        self.penup()
        self.go_to_start()
        self.seth(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.backward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


