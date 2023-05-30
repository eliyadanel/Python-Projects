from turtle import Turtle

SHAPE = 'circle'
COLOR = 'white'


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed_num = 0.1
        self.speed(self.speed_num)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.speed_num *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.speed_num = 0.1
        self.bounce_x()
