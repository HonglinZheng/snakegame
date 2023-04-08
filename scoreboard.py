from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write_text(0, 260, f"Score: {self.score}")

    def write_text(self, x, y, text):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(text, False, align="center", font=("Arial", 24, "normal"))

    # add score after eating
    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 24, "normal"))

    # report the final score to the user
    def report(self):
        self.clear()
        self.write_text(0, 0, f"Your final score is {self.score}.")

