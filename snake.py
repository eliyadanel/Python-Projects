from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # The starting location of the 1st three turtle squares that the snake is composed of.
MOVE_DISTANCE = 20  # Each time the snake moves it takes 20 steps (pixels).
UP = 90  # The directions in which the snake can move.
DOWN = 270
LEFT = 180
RIGHT = 0
SHAPE = 'square'
COLOR = 'white'


class Snake(Turtle):
    def __init__(self):
        super(Snake, self).__init__()
        self.segments = []  # The body of the snake
        self.create_snake()  # This method will be run whenever the Snake class is called upon to create the initial snake body.
        self.head = self.segments[0]  # The head of the snake, that the rest of the body follows.

    def create_snake(self):
        # The first 3 snake blocks are created.
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # The snake is created and sent to its correct location on the screen.
        new_segment = Turtle(SHAPE)
        new_segment.color(COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # The snake moves from last square to first by placing each square on the square before it and finally letting the head move forwards to the direction in which it is heading.
        for seg_num in range(len(self.segments) - 1, 0, -1):  # start, stop, step
            self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())
            # Makes current seg go to the position of previous seg.
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # The following methods are what defines the change of the snake's heading (see keystroke listener in main file)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
