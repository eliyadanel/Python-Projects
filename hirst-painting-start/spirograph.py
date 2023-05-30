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


def spirograph(gap_size):
    tim.speed("fastest")
    # tim.tracer(False)
    for i in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)


spirograph(5)

screen = t.Screen()
screen.exitonclick()
screen.tracer(8, 25)
