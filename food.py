import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.position_range = []
        for x in range(-260, 260, 20):
            self.position_range.append(x)
        self.shape("circle")
        self.color("red")
        self.shapesize(0.5, 0.5, 1)
        self.speed(0)
        self.penup()
        self.current_food_pos = [random.choice(self.position_range), random.choice(self.position_range)]
        self.goto(x=self.current_food_pos[0], y=self.current_food_pos[1])

    def spawn_pos(self):
        spawn_food_pos = [random.choice(self.position_range), random.choice(self.position_range)]
        while spawn_food_pos == self.current_food_pos:
            spawn_food_pos = [random.choice(self.position_range), random.choice(self.position_range)]
        self.goto(x=spawn_food_pos[0], y=spawn_food_pos[1])
