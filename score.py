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
        self.write(arg=f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)

    def record(self):
        self.current_score += 1
        self.clear()
        self.write(arg=f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over!", align=ALIGNMENT, font=FONT)
