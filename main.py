from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from powerup import PowerUp
from menu_screens import MenuScreen, GameOverScreen, PauseScreen
import time
import random
import sys

# Constants
PADDLE_HEIGHT = 50
PADDLE_WIDTH = 20
UPPER_Y_BOUNDARY = 280
LOWER_Y_BOUNDARY = -280
RIGHT_EDGE = 380
LEFT_EDGE = -380
BALL_RESET_POSITION = (0, 0)
SCORE_LIMIT = 5

# Create the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Evolution")
screen.tracer(0)

# Initialize menu screens
menu_screen = MenuScreen(screen)
game_over_screen = GameOverScreen(screen)
pause_screen = PauseScreen(screen)

# Game state variables
game_state = "menu"
is_game_on = True

# Object initialization
l_paddle = None
r_paddle = None
ball = None
scoreboard = None
power_up = None

def init_game_objects():
    """Initialize or reset game objects"""
    global l_paddle, r_paddle, ball, scoreboard, power_up
    l_paddle = Paddle((-350, 0))
    r_paddle = Paddle((350, 0), is_ai=True)
    ball = Ball()
    scoreboard = Scoreboard()
    power_up = PowerUp()

def hide_game_objects():
    """Hide all game objects by moving them off-screen"""
    global l_paddle, r_paddle, ball, scoreboard, power_up
    if l_paddle:
        l_paddle.goto(1000, 1000)
    if r_paddle:
        r_paddle.goto(1000, 1000)
    if ball:
        ball.goto(1000, 1000)
    if scoreboard:
        scoreboard.clear()
    if power_up:
        power_up.goto(1000, 1000)

def show_game_objects():
    """Show game objects in their proper positions"""
    global l_paddle, r_paddle, ball, scoreboard, power_up
    if l_paddle:
        l_paddle.goto(-350, 0)
        l_paddle.shapesize(stretch_wid=5, stretch_len=1)
    if r_paddle:
        r_paddle.goto(350, 0)
        r_paddle.shapesize(stretch_wid=5, stretch_len=1)
    if ball:
        ball.goto(0, 0)
    if scoreboard:
        scoreboard.update_scoreboard()
    if power_up:
        power_up.reset_position()

def start_game():
    """Start a new game"""
    global game_state
    if game_state == "menu":
        game_state = "playing"
        menu_screen.hide()
        init_game_objects()
        show_game_objects()

def pause_game():
    """Pause/unpause the game"""
    global game_state
    if game_state == "playing":
        game_state = "paused"
        pause_screen.show(scoreboard.l_score, scoreboard.r_score)
    elif game_state == "paused":
        game_state = "playing"
        pause_screen.hide()

def restart_game():
    """Restart the game from game over screen"""
    global game_state
    if game_state == "game_over":
        game_state = "playing"
        game_over_screen.hide()
        init_game_objects()
        show_game_objects()

def return_to_menu():
    """Return to main menu"""
    global game_state
    if game_state == "game_over":
        game_state = "menu"
        game_over_screen.hide()
        hide_game_objects()
        menu_screen.show()

def end_game():
    """End the current game and show game over screen"""
    global game_state
    # Store final scores before hiding objects
    final_l_score = scoreboard.l_score
    final_r_score = scoreboard.r_score
    final_high_score = scoreboard.high_score
    
    # Save high score
    scoreboard.save_high_score()
    
    # Hide all game objects first
    hide_game_objects()
    
    # Change state and show game over screen
    game_state = "game_over"
    game_over_screen.show(final_l_score, final_r_score, final_high_score)

def safe_exit():
    """Safely exit the game without errors"""
    global is_game_on
    is_game_on = False
    
    # Save high score if scoreboard exists
    if scoreboard:
        try:
            scoreboard.save_high_score()
        except:
            pass

def window_close():
    """Handle window close button"""
    global is_game_on
    is_game_on = False

# Screen Functions
screen.listen()

def on_up():
    if game_state == "playing" and l_paddle:
        l_paddle.move_up()

def on_down():
    if game_state == "playing" and l_paddle:
        l_paddle.move_down()

def on_enter():
    if game_state == "menu":
        start_game()

def on_p():
    if game_state in ["playing", "paused"]:
        pause_game()

def on_r():
    if game_state == "game_over":
        restart_game()

def on_m():
    if game_state == "game_over":
        return_to_menu()

# Bind keys
screen.onkey(on_up, "Up")
screen.onkey(on_down, "Down")
screen.onkey(on_enter, "Return")
screen.onkey(on_p, "p")
screen.onkey(on_r, "r")
screen.onkey(on_m, "m")
screen.onkey(safe_exit, "Escape")

# Handle window close button properly
try:
    root = screen.getcanvas().winfo_toplevel()
    root.protocol("WM_DELETE_WINDOW", window_close)
except:
    pass

# Show initial menu
menu_screen.show()

# Main game loop
try:
    while is_game_on:
        if game_state == "playing":
            time.sleep(ball.move_speed)
            screen.update()
            
            ball.move()

            # Move AI paddle
            if r_paddle.is_ai:
                r_paddle.move_ai(ball)

            # Detect wall collision
            if ball.ycor() > UPPER_Y_BOUNDARY or ball.ycor() < LOWER_Y_BOUNDARY:
                ball.bounce_y()

            # Detect collision with both paddles
            if (ball.distance(r_paddle) < PADDLE_HEIGHT and ball.xcor() > 320 and ball.x_move > 0) or \
               (ball.distance(l_paddle) < PADDLE_HEIGHT and ball.xcor() < -320 and ball.x_move < 0):
                ball.bounce_x()

            # Detect right paddle misses
            if ball.xcor() > RIGHT_EDGE:
                ball.reset_position()
                scoreboard.l_point()

            # Detect left paddle misses
            if ball.xcor() < LEFT_EDGE:
                ball.reset_position()
                scoreboard.r_point()

            # Check if a power-up has been hit
            power_up_collision = ball.check_power_up_collision(power_up)
            if power_up_collision == "size_up":
                l_paddle.shapesize(stretch_wid=7, stretch_len=1)
                r_paddle.shapesize(stretch_wid=7, stretch_len=1)
            elif power_up_collision == "speed_up":
                ball.move_speed *= 0.8

            # Check for game over condition
            if scoreboard.l_score == SCORE_LIMIT or scoreboard.r_score == SCORE_LIMIT:
                end_game()
        else:
            screen.update()
            time.sleep(0.02)

except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"Game ended: {e}")
finally:
    try:
        if scoreboard:
            scoreboard.save_high_score()
    except:
        pass
    sys.exit(0)
