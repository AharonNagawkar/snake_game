from turtle import Turtle
from os import system

HIGH_SCORE_FILE = 'high_score.txt'

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.pull_high_score()
        self.color("yellow")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} | High Score: {self.high_score} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        with open(HIGH_SCORE_FILE, 'w') as file:
            file.write(str(self.high_score))

    def add_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.clear()
        self.update_scoreboard()

    def pull_high_score(self):
        try:
            with open(HIGH_SCORE_FILE, 'r+') as file:
                score = file.read()
                self.high_score = int(score)

        except FileNotFoundError:
            with open(HIGH_SCORE_FILE, 'w') as file:
                file.write(str(self.high_score))
