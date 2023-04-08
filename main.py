import snake as s
from turtle import Screen
import time
import food as f
import scoreboard as sc
# global keys
SPEED = 0.3
GAME_ON = "yes"
# set screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# create snake, food and scoreboard
snake = s.Snake()
food = f.Food(snake)
scoreboard = sc.Scoreboard()


def intro():
    global GAME_ON
    GAME_ON = screen.textinput("WELCOME!", "You can press space to pause game. "
                                           "You can use up, down, left and right arrow to control the snake. "
                                           "Do you want to play? enter yes or no:")
    screen.listen()


def choose_speed():
    global SPEED
    level = screen.textinput("CHOOSE SPEED LEVEL", "You can choose the speed of snake. please enter easy, middle, hard:")
    if level.lower() == "easy":
        SPEED = 0.5
    elif level.lower() == "middle":
        SPEED = 0.3
    else:
        SPEED = 0.1
    screen.listen()


def pause():
    global GAME_ON
    GAME_ON = screen.textinput("PAUSE", "Do you want to continue? enter yes or no:")
    screen.listen()


# enable key controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(pause, "space")


# start the game
intro()
choose_speed()
while GAME_ON == "yes":
    screen.update()
    time.sleep(SPEED)
    snake.move()
    # eat food
    if snake.head.distance(food) < 10:
        snake.extend()
        food.refresh(snake)
        scoreboard.refresh()
    # collision check
    if snake.detect_collision():
        GAME_ON = "no"


# report result
scoreboard.report()
screen.exitonclick()
