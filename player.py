STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(position)
        self.setheading(90)

    def move(self):
        self.new_y = self.ycor() + 10
        self.goto(self.xcor(), self.new_y)
