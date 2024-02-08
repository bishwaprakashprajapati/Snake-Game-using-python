from turtle import Turtle, Screen
import time
import random

from food import Food
from score_board import Score

up = 90
down = 270
right = 0
left = 180

food =Food()
score = Score()


def move_up():
    if snake_head.heading() != down:
        snake_head.setheading(up)


def move_down():
    if snake_head.heading() != up:
        snake_head.setheading(down)


def move_right():
    if snake_head.heading() != left:
        snake_head.setheading(right)


def move_left():
    if snake_head.heading() != right:
        snake_head.setheading(left)



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)



starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

def snake():
    for position in starting_positions:
        add_segment(position)

def add_segment(position):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

def extend():
    # Get the position of the last segment to extend from there
    last_segment = segments[-1]
    position = last_segment.position()
    add_segment(position)

snake()
is_game_on = True
snake_head = segments[0]

while is_game_on:
    screen.update()
    time.sleep(0.2)

    if snake_head.distance(food)<15:
        food.new_food()
        score.increase_score()
        extend()

    if snake_head.xcor() > 280 or snake_head.xcor() <-280 or snake_head.ycor()>280 or snake_head.ycor()<-280:
        is_game_on = False
        score.game_over()

    for segment in segments:
        if segment == snake_head:
            pass
        elif snake_head.distance(segment)<10:
            is_game_on = False
            score.game_over()

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    snake_head.forward(20)

    screen.listen()
    screen.onkey(key="Up", fun=move_up)
    screen.onkey(key="Right", fun=move_right)
    screen.onkey(key="Down", fun=move_down)
    screen.onkey(key="Left", fun=move_left)


screen.exitonclick()
