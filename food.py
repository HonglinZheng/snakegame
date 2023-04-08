from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self, snake):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.refresh(snake)

    def refresh(self, snake):
        # generate random food positions until it doesn't appear on the snake body
        on_snake = True
        while on_snake:
            on_snake = False
            x_pos = random.randint(-270, 270)
            y_pos = random.randint(-270, 270)
            for body in snake.segments:
                if body.xcor() - x_pos < 5 and x_pos - body.xcor() < 5 and body.ycor() - y_pos < 5 and y_pos - body.ycor() < 5:
                    print("food appears on the snake body.")
                    on_snake = True
        self.goto(x_pos, y_pos)
