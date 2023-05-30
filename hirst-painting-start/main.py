# import colorgram
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
"""The color list is created from the colorgram package with the commented out code."""
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)


def dot_painting(c_l):
    for dot in range(1, 11):
        chosen_color = random.choice(c_l)
        tim.dot(20, chosen_color)
        tim.penup()
        tim.forward(50)


def new_line():
    position_list = [tim.pos()[0], tim.pos()[1]]
    # print(position_list)
    position_list[1] += 50
    tim.penup()
    tim.goto(position_list[0], position_list[1])
    tim.right(180)
    tim.forward(50)


tim.penup()
tim.goto(-250, -100)

for i in range(10):
    dot_painting(color_list)
    new_line()

screen = t.Screen()
screen.exitonclick()
