from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(-50, 250)
        self.color("white")
        self.write(arg=f"Score: {self.score}", move=False, font=("Courier", 18, "normal"))

    def scoring(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, font=("Courier", 18, "normal"))


    def gameover(self):
        self.goto(-60, 0)
        self.write(arg="GAME OVER", move=False, font=("Courier", 18, "normal"))
