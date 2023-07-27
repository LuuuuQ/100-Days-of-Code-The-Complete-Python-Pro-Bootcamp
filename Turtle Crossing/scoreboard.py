from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("black")
        self.goto(-200, 240)
        self.write(arg=f"Level: {self.score}", move=False, align="center", font=("Courier", 20, "normal"))

    def scoring(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Level: {self.score}", move=False, align="center", font=("Courier", 20, "normal"))

    def gameover(self):
        self.goto(-85, 0)
        self.write(arg="GAME OVER", move=False, font=("Courier", 25, "normal"))
