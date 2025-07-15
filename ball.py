from turtle import Turtle
import random

# Maximum speed for the ball
MAX_SPEED = 0.01

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        """Move the ball by its current speed."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bounce the ball off the top or bottom wall."""
        self.y_move *= -1

    def bounce_x(self):
        """Bounce the ball off the paddles."""
        self.x_move *= -1
        # Gradually increase ball speed
        self.increase_speed()  

    def increase_speed(self):
        """Increase the ball's speed up to the max speed."""
        if self.move_speed > MAX_SPEED:
            # Gradually decrease time between moves (increase speed)
            self.move_speed *= 0.95 

    def reset_position(self):
        """Reset the ball's position after a score."""
        self.goto(0, 0)
        self.bounce_x()
        # Reset speed after scoring
        self.move_speed = 0.05

    def check_power_up_collision(self, power_up):
        """Check if the ball collides with the power-up."""
        # Power-up hit
        if self.distance(power_up) < 20:
            # Reset power-up position  
            power_up.reset_position()  
            if random.choice([True, False]):
                # Increase paddle size
                return "size_up"  
            else:
                # Increase ball speed
                return "speed_up"  
        return None