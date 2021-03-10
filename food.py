from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):   # CREATE THE FOOD.
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.setheading(60)
        self.speed("fastest")
        self.refresh()

    def refresh(self):  # REFRESH THE FOOD LOCATION WHEN HIT.
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
