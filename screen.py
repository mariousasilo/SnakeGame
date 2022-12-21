from turtle import Screen
HEIGHT = 600
WIDTH = 600
SCREEN_COLOR = "black"
WINDOW_TITLE = "Snake Game"


class Screen_setup:

    def __init__(self):
        self.screen = Screen()
        self.screen.listen()
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.bgcolor(SCREEN_COLOR)
        self.screen.title(WINDOW_TITLE)
        self.screen.tracer(0)

    def screen_controls(self, function):
        self.screen.onkey(key="w", fun=function.up_direction)
        self.screen.onkey(key="s", fun=function.down_direction)
        self.screen.onkey(key="a", fun=function.west_direction)
        self.screen.onkey(key="d", fun=function.east_direction)
