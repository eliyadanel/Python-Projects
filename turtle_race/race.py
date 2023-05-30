from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? pick a color: ')

timmy = Turtle()
tommy = Turtle()
tammy = Turtle()
tony = Turtle()
tilly = Turtle()
terry = Turtle()
tory = Turtle()

color_list = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
turtle_list = [timmy, tommy, tammy, tony, tilly, terry, tory]
location = [-230, -180]

for (color, item) in zip(color_list, turtle_list):
    item.color(color)
    item.shape("turtle")
    item.penup()
    item.goto(location[0], location[1])
    location[1] += 60

race_on = False

if user_bet:
    race_on = True

while race_on:
    for item in turtle_list:
        random_distance = random.randint(0, 10)
        item.forward(random_distance)
        if item.xcor() > 230.00:
            race_on = False
            winning_color = item.pencolor()
            if winning_color == user_bet:
                print(f"Your {user_bet} turtle won the race!")
            else:
                print(f"The turtle you bet on lost, {winning_color} turtle won. Try again next time.")

screen.exitonclick()
