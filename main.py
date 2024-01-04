from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake = Snake()
food = Food()
score_ = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score_.increase_score()
        score_.type_()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or \
            snake.segments[0].ycor() < -280:
        score_.reset_scoreboard()
        snake.reset_snake()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            score_.hit_your_tail()
            score_.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
