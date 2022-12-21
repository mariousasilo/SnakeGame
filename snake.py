import time
from turtle import Turtle

TIME = 0.1
STARTING_SEGMENT = 3
TRAVEL_DISTANCE = 20
SHAPE = "square"
COLOR = "white"


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for x in range(STARTING_SEGMENT):
            x_axis = -20 * x
            self.segment.append(Turtle(SHAPE))
            self.segment[x].color(COLOR)
            self.segment[x].penup()
            self.segment[x].goto(x=x_axis, y=0)

    def move(self):
        time.sleep(TIME)
        for x in range(1, len(self.segment)):
            self.segment[-x].goto(self.segment[-x - 1].pos())
        self.head.fd(TRAVEL_DISTANCE)

    def add_segment(self):
        last_segment_pos = self.segment[len(self.segment) - 1].pos()
        self.segment.append(Turtle("square"))
        total_segment = len(self.segment)
        self.segment[total_segment - 1].color("white")
        self.segment[total_segment - 1].penup()
        self.segment[total_segment - 1].goto(last_segment_pos)

    def reset(self):
        for x in self.segment:
            x.goto(x=1000, y=1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def up_direction(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down_direction(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def east_direction(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def west_direction(self):
        if self.head.heading() != 0:
            self.head.seth(180)
