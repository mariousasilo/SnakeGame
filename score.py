from turtle import Turtle

FONT = ("Arial", 20, "normal")
ALIGNMENT = "center"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed(0)
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.current_score = 0
        with open(file="high_score.txt") as file:
            self.high_score = int(file.read())
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(arg=f"Score: {self.current_score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def record(self):
        self.current_score += 1
        self.print_score()

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        with open(file="high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.current_score = 0
        self.print_score()
