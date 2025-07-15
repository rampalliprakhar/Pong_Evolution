from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position, is_ai=False):
        super().__init__()
        # Check if this paddle is AI-controlled
        self.is_ai = is_ai  
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        """Move paddle up within bounds."""
        if self.ycor() < 250:  
            self.goto(self.xcor(), self.ycor() + 25)

    def move_down(self):
        """Move paddle down within bounds."""
        if self.ycor() > -240:  
            self.goto(self.xcor(), self.ycor() - 25)  

    def move_ai(self, ball):
        """AI moves the paddle towards the ball's y position."""
        if self.ycor() < ball.ycor() and self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 15)  
        elif self.ycor() > ball.ycor() and self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 15)  