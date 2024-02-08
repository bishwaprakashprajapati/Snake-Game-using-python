from turtle import Turtle,Screen
import random


class Food(Turtle):


    def __init__(self):
        super().__init__()
        self.color0 = ["red", "blue", "yellow", "pink"]
        self.shape("circle")
        self.color(random.choice(self.color0))
        self.penup()
        self.shapesize(0.5,0.5)
        self.new_food()


    def new_food(self):
        x_position = random.randint(-280, 280)
        y_position = random.randint(-280, 280)
        self.goto(x_position, y_position)

