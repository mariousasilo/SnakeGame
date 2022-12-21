from snake import Snake
from food import Food
from score import Score
from screen import Screen_setup

my_screen = Screen_setup()
snake = Snake()
food = Food()
score = Score()
my_screen.screen_controls(snake)

game_on = True
while game_on:
    snake.move()
    my_screen.screen.update()

    if snake.head.distance(food) <= 1:
        food.spawn_pos()
        snake.add_segment()
        score.record()

    snake_x = int(snake.head.xcor())
    snake_y = int(snake.head.ycor())
    if snake_x >= 300 or snake_x <= -300 or snake_y >= 300 or snake_y <= -300:
        score.reset()
        snake.reset()

    for body in snake.segment[1:]:
        if snake.head.distance(body) < 10:
            score.reset()
            snake.reset()

my_screen.screen.exitonclick()
