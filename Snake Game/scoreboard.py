from turtle import *


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-10, 275)
        self.score = 0
        with open("data.txt", "r") as highest_score:
            self.high_score = int(highest_score.read())
        self.score_show()

    def score_show(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ('Arial', 15, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as new_highest_score:
                new_highest_score.write(str(self.score))
                self.high_score = self.score
        self.score = 0
        self.score_show()
