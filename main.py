from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
# Defining screen settings:
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
# Defining the class objects:
scoreboard = Scoreboard()
snake = Snake()
food = Food()
# The screen object listens to keystrokes so the user can control the snake with keyboard:
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
# While variable game_on is True, the game goes on:
game_on = True
while game_on:
    # The screen works in the update method, and sleeps between updates so the snake 'animation' doesn't lag.
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food. If occurs: increase score + grow snake:
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # Detect collision with wall. If occurs: calculate highscore + start new game
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_high_score()
        snake.reset_snake()
    # Detect collision with tail. If occurs: calculate highscore + start new game
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset_high_score()
            snake.reset_snake()
screen.exitonclick()
