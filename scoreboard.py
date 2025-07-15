from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.high_score = self.load_high_score()
        self.update_scoreboard()

    def load_high_score(self):
        """Load the high score from a file."""
        try:
            with open("high_score.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        """Save the high score to a file."""
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def update_scoreboard(self):
        """Update the scoreboard display."""
        self.clear()

        # Display the high score at the top
        self.goto(0, 260)
        self.write(f"High Score: {self.high_score}", align="center", font=("Courier", 16, "normal"))

        # Display the main score in x | y format
        self.goto(0, 220)
        self.write(f"{self.l_score} | {self.r_score}", align="center", font=("Courier", 24, "normal"))

        # Display labels under the scores
        self.goto(-30, 195)
        self.write("Player", align="center", font=("Courier", 12, "normal"))
        
        self.goto(30, 195)
        self.write("AI", align="center", font=("Courier", 12, "normal"))

    def l_point(self):
        """Left player scores a point."""
        self.l_score += 1
        if self.l_score > self.high_score:
            self.high_score = self.l_score
        self.update_scoreboard()

    def r_point(self):
        """Right player scores a point."""
        self.r_score += 1
        if self.r_score > self.high_score:
            self.high_score = self.r_score
        self.update_scoreboard()

    def game_over(self):
        """Display game over message."""
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 50, "normal"))
        self.save_high_score()