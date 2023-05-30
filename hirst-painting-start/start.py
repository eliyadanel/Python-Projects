import turtle as t
import random

t.colormode(255)
tim = t.Turtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_rgb = (r, g, b)
    return rand_rgb


def shape_drawer():
    directions = [0, 90, 180, 270]  # east, north, west, south
    tim.speed(9)  # speed fast
    while True:
        tim.pensize(10)  # thickness of pen
        chosen_direction = random.choice(directions)  # select random direction from directions list
        tim.color(random_color())  # the random chosen color is used for the next pen stroke
        tim.right(chosen_direction)  # the random chosen direction is where turtle turns next
        tim.forward(20)  # after each turn, turtle moves forward 20 steps


shape_drawer()

screen = t.Screen()
screen.exitonclick()
