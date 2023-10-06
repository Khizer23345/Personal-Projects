from turtle import *

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.all_snakes = []
        self.create_snake()
        self.head = self.all_snakes[0]

    def add_segment(self, position):
        snakes = Turtle("square")
        snakes.color("white")
        snakes.penup()
        snakes.goto(position)
        self.all_snakes.append(snakes)

    def reset(self):
        for snake in self.all_snakes:
            snake.goto(1000, 1000)
        self.all_snakes.clear()
        self.create_snake()
        self.head = self.all_snakes[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def extend(self):
        # Add a new segment to the snake
        self.add_segment(self.all_snakes[-1].position())

    def move(self):
        for snakes in range(len(self.all_snakes)-1, 0, -1):
            new_x = self.all_snakes[snakes - 1].xcor()
            new_y = self.all_snakes[snakes - 1].ycor()
            self.all_snakes[snakes].goto(new_x, new_y)
        self.all_snakes[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
