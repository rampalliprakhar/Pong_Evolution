from turtle import Turtle
import random

class PowerUp(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.goto(random.randint(-200, 200), random.randint(-200, 200))
        self.showturtle()

    def reset_position(self):
        """Move power-up to a new random position."""
        self.goto(random.randint(-200, 200), random.randint(-200, 200))