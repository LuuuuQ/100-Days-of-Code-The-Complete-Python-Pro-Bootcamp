from turtle import Turtle


class Text(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.color("black")

    def texting(self, answer, x, y):
        self.goto(x, y)
        self.write(arg=f"{answer}", align="center", move=False, font=("Courier", 8, "normal"))
