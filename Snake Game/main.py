from turtle import *
import time
from snake import Snake
from food import *
from scoreboard import *
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake game!')
screen.tracer(0)
snake = Snake()
scoreboard = ScoreBoard()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while_loop = True
while while_loop:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect Collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score += 1
        scoreboard.score_show()
        snake.extend()
        snake.speed(0)

    # Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segments in snake.all_snakes[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()

