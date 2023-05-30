from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 14, 'normal')
MOVE = False
COLOR = 'white'
POSITION = (0, 270)
FILE = "current_highscore.txt"
with open(FILE) as file:
    HIGH_SCORE = int(file.read())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HIGH_SCORE
        self.hideturtle()
        self.penup()
        self.color(COLOR)
        self.goto(POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score}    High-Score: {self.high_score}', align=ALIGNMENT, move=MOVE, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("current_highscore.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
