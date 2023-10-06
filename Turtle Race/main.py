import turtle
from turtle import *
import random
screen = Screen()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make the bet", prompt="Which turtle win win the race")
y_positions = (-70, -40, -10, 20, 50, 80)
is_race_one = False
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_one = True
while is_race_one:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_one = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} is the winner!")
            else:
                print(f"You have lost! The {winning_color} is the winner")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

print(all_turtle)


screen.exitonclick()