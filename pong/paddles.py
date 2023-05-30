from turtle import Turtle

SHAPE = 'square'
COLOR = 'white'


class Paddle(Turtle):
    def __init__(self, first_location):
        super().__init__()
        self.penup()
        self.shape(SHAPE)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(COLOR)
        self.goto(first_location)

    def up(self):
        self.goto(self.xcor(), (self.ycor() + 20))

    def down(self):
        self.goto(self.xcor(), (self.ycor() - 20))
