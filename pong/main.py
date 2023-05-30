from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# Screen setup:
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)  # Tracer is turned off so no unnecessary animations will be seen
# Defining the left + right paddle objects from the 'paddles' class:
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# creating ball object from 'Ball' class:
ball = Ball()
ball.move()
# creating the scoreboard object from the 'Scoreboard' class:
scoreboard = Scoreboard()
# The screen listens to specific keystrokes and moves the objects accordingly:
screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)
# A while loop that keeps the game going and updates the screen (since the tracer is off).
game_on = True
while game_on:
    time.sleep(ball.speed_num)
    screen.update()
    ball.move()  # The ball moves constantly
    if ball.ycor() > 280 or ball.ycor() < -280:  # If the ball hits the maximum height of the screen it bounces back
        ball.bounce_y()
    if (ball.distance(r_paddle) <= 50 and ball.xcor() >= 320) or (ball.distance(l_paddle) <= 50 and ball.xcor() <= -320):  # If the ball hits one of the paddles it bounces in the opposite direction.
        ball.bounce_x()
    if ball.xcor() > 380:  # If the ball hits the right side of the screen, the right paddle missed, which meant left side gets a point (and vice versa).
        scoreboard.l_point()
        ball.reset_position()
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
