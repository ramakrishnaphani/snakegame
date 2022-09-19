from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(random.randint(-270, 270), random.randint(-270, 270))

    def set_new_pos(self):
        self.random_y = random.randint(-270, 270)
        self.random_x = random.randint(-270, 270)
        self.position = (self.random_x, self.random_y)

    def refresh(self):
        self.set_new_pos()
