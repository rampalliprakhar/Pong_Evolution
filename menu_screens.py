from turtle import Turtle
import random

class MenuScreen:
    def __init__(self, screen):
        self.screen = screen
        self.menu_turtle = Turtle()
        self.menu_turtle.hideturtle()
        self.menu_turtle.color("white")
        self.menu_turtle.penup()
        self.menu_turtle.speed("fastest")
        self.is_visible = False
        
    def show(self):
        """Display the menu screen"""
        if not self.is_visible:
            self.menu_turtle.goto(0, 100)
            self.menu_turtle.write("PONG EVOLUTION", align="center", font=("Courier", 32, "bold"))
            
            self.menu_turtle.goto(0, 50)
            self.menu_turtle.write("Press 'ENTER' to Start", align="center", font=("Courier", 20, "normal"))
            
            self.menu_turtle.goto(0, 10)
            self.menu_turtle.write("Use Arrow Keys to Move", align="center", font=("Courier", 16, "normal"))
            
            self.menu_turtle.goto(0, -20)
            self.menu_turtle.write("First to 5 points wins!", align="center", font=("Courier", 14, "normal"))
            
            self.menu_turtle.goto(0, -50)
            self.menu_turtle.write("Watch out for power-ups!", align="center", font=("Courier", 14, "normal"))
            
            self.menu_turtle.goto(0, -80)
            self.menu_turtle.color("cyan")
            self.menu_turtle.write("Player vs AI", align="center", font=("Courier", 16, "italic"))
            
            self.is_visible = True
    
    def hide(self):
        """Hide the menu screen"""
        if self.is_visible:
            self.menu_turtle.clear()
            self.is_visible = False
    
    def cleanup(self):
        """Clean up the menu turtle"""
        self.menu_turtle.clear()
        self.menu_turtle.hideturtle()

class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen
        self.game_over_turtle = Turtle()
        self.game_over_turtle.hideturtle()
        self.game_over_turtle.penup()
        self.game_over_turtle.speed("fastest")
        self.is_visible = False
    
    def show(self, player_score=0, ai_score=0, high_score=0):
        """Display the enhanced game over screen with score information"""
        if not self.is_visible:
            # Determine winner
            winner = "PLAYER WINS!" if player_score > ai_score else "AI WINS!"
            winner_color = "lime" if player_score > ai_score else "red"
            
            # Main "GAME OVER" title
            self.game_over_turtle.goto(0, 120)
            self.game_over_turtle.color("red")
            self.game_over_turtle.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
            
            # Winner announcement
            self.game_over_turtle.goto(0, 80)
            self.game_over_turtle.color(winner_color)
            self.game_over_turtle.write(winner, align="center", font=("Courier", 24, "bold"))
            
            # Decorative line
            self.game_over_turtle.goto(0, 50)
            self.game_over_turtle.color("white")
            self.game_over_turtle.write("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", align="center", font=("Courier", 12, "normal"))
            
            # Final score
            self.game_over_turtle.goto(0, 20)
            self.game_over_turtle.color("cyan")
            self.game_over_turtle.write(f"FINAL SCORE: {player_score} | {ai_score}", align="center", font=("Courier", 20, "bold"))
            
            # Score labels
            self.game_over_turtle.goto(-30, -5)
            self.game_over_turtle.color("white")
            self.game_over_turtle.write("Player", align="center", font=("Courier", 12, "normal"))
            
            self.game_over_turtle.goto(30, -5)
            self.game_over_turtle.write("AI", align="center", font=("Courier", 12, "normal"))
            
            # High score section
            self.game_over_turtle.goto(0, -35)
            max_score = max(player_score, ai_score)
            if max_score == high_score and max_score > 0:
                self.game_over_turtle.color("gold")
                self.game_over_turtle.write("🏆 NEW HIGH SCORE! 🏆", align="center", font=("Courier", 18, "bold"))
            else:
                self.game_over_turtle.color("yellow")
                self.game_over_turtle.write(f"High Score: {high_score}", align="center", font=("Courier", 16, "normal"))
            
            # Performance message
            self.game_over_turtle.goto(0, -65)
            performance_msg, performance_color = self.get_performance_message(player_score, ai_score)
            self.game_over_turtle.color(performance_color)
            self.game_over_turtle.write(performance_msg, align="center", font=("Courier", 14, "italic"))
            
            # Decorative line
            self.game_over_turtle.goto(0, -90)
            self.game_over_turtle.color("white")
            self.game_over_turtle.write("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", align="center", font=("Courier", 12, "normal"))
            
            # Controls section
            self.game_over_turtle.goto(0, -120)
            self.game_over_turtle.color("lime")
            self.game_over_turtle.write("Press 'R' to Play Again", align="center", font=("Courier", 16, "normal"))
            
            self.game_over_turtle.goto(0, -145)
            self.game_over_turtle.color("white")
            self.game_over_turtle.write("Press 'M' for Main Menu", align="center", font=("Courier", 16, "normal"))
            
            # Tip
            self.game_over_turtle.goto(0, -175)
            self.game_over_turtle.color("orange")
            tip = self.get_random_tip()
            self.game_over_turtle.write(f"💡 Tip: {tip}", align="center", font=("Courier", 12, "normal"))
            
            self.is_visible = True
    
    def get_performance_message(self, player_score, ai_score):
        """Return a performance message and color based on scores"""
        if player_score == 0:
            return "The AI dominated! Try again!", "gray"
        elif player_score == ai_score:
            return "It was a close match!", "yellow"
        elif player_score > ai_score:
            if player_score == 5 and ai_score == 0:
                return "PERFECT GAME! Flawless victory!", "gold"
            elif player_score == 5 and ai_score <= 2:
                return "Dominant performance!", "lime"
            else:
                return "Well played! You beat the AI!", "cyan"
        else:
            if ai_score == 5 and player_score >= 3:
                return "Close game! You almost had it!", "orange"
            else:
                return "The AI was tough today!", "red"
    
    def get_random_tip(self):
        """Return a random gameplay tip"""
        tips = [
            "Try to predict where the ball will go!",
            "Power-ups can change the game - use them wisely!",
            "Stay calm and focused on the ball",
            "The AI gets harder as the game progresses",
            "Practice makes perfect - keep playing!",
            "Watch the ball's angle after it bounces",
            "Position yourself early for better returns",
            "Speed power-ups make the game more intense!"
        ]
        return random.choice(tips)
    
    def hide(self):
        """Hide the game over screen"""
        if self.is_visible:
            self.game_over_turtle.clear()
            self.is_visible = False
    
    def cleanup(self):
        """Clean up the game over turtle"""
        self.game_over_turtle.clear()
        self.game_over_turtle.hideturtle()

class PauseScreen:
    def __init__(self, screen):
        self.screen = screen
        self.pause_turtle = Turtle()
        self.pause_turtle.hideturtle()
        self.pause_turtle.color("yellow")
        self.pause_turtle.penup()
        self.pause_turtle.speed("fastest")
        self.is_visible = False
    
    def show(self, player_score=0, ai_score=0):
        """Display the enhanced pause screen"""
        if not self.is_visible:
            # Semi-transparent background effect
            self.pause_turtle.goto(0, 200)
            self.pause_turtle.color("black")
            for i in range(20):
                y_pos = 200 - (i * 20)
                self.pause_turtle.goto(-300, y_pos)
                self.pause_turtle.write("█" * 50, align="left", font=("Courier", 8, "normal"))
            
            # Main pause content
            self.pause_turtle.goto(0, 80)
            self.pause_turtle.color("yellow")
            self.pause_turtle.write("⏸️ PAUSED ⏸️", align="center", font=("Courier", 32, "bold"))
            
            # Current score
            self.pause_turtle.goto(0, 40)
            self.pause_turtle.color("cyan")
            self.pause_turtle.write(f"Current Score: {player_score} | {ai_score}", align="center", font=("Courier", 18, "normal"))
            
            self.pause_turtle.goto(-30, 15)
            self.pause_turtle.color("white")
            self.pause_turtle.write("Player", align="center", font=("Courier", 12, "normal"))
            
            self.pause_turtle.goto(30, 15)
            self.pause_turtle.write("AI", align="center", font=("Courier", 12, "normal"))
            
            self.pause_turtle.goto(0, -20)
            self.pause_turtle.color("white")
            self.pause_turtle.write("Game is temporarily stopped", align="center", font=("Courier", 16, "normal"))
            
            self.pause_turtle.goto(0, -50)
            self.pause_turtle.color("lime")
            self.pause_turtle.write("Press 'P' to Resume", align="center", font=("Courier", 20, "bold"))
            
            self.pause_turtle.goto(0, -80)
            self.pause_turtle.color("orange")
            self.pause_turtle.write("Take a moment to plan your strategy!", align="center", font=("Courier", 14, "italic"))
            
            self.is_visible = True
    
    def hide(self):
        """Hide the pause screen"""
        if self.is_visible:
            self.pause_turtle.clear()
            self.is_visible = False
    
    def cleanup(self):
        """Clean up the pause turtle"""
        self.pause_turtle.clear()
        self.pause_turtle.hideturtle()