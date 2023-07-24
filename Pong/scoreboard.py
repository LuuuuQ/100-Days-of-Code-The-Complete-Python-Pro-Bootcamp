from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.write(arg=f"{self.score_l}     {self.score_r}", move=False, align="center", font=("Courier", 50, "normal"))

    def scoring_l(self):
        self.score_r += 1
        self.clear()
        self.write(arg=f"{self.score_l}     {self.score_r}", move=False, align="center", font=("Courier", 50, "normal"))

    def scoring_r(self):
        self.score_l += 1
        self.clear()
        self.write(arg=f"{self.score_l}     {self.score_r}", move=False, align="center", font=("Courier", 50, "normal"))

