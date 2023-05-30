from turtle import Turtle
import random

FOOD_SHAPE = 'turtle'


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("pink")
        self.speed("fastest")
        # Random x and y positions are generated from the scope that is within the screens boundaries:
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
        self.refresh()

    # The refresh method generates a new position for the food to go to and is used whenever the snake's head collides with the existing food.
    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)

