FONT = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)

    def mark_level(self):
        self.level += 1
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=FONT)
