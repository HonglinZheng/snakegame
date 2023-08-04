from turtle import Turtle

FONT = "Arial", 24, "normal"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.write_text(0, 260, f"Score: {self.score}; Final Score: {self.high_score}")

    def write_text(self, x, y, text):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(text, False, align="center", font=FONT)

    # add score after eating
    def refresh(self):
        self.score += 1
        self.clear()
        self.write_text(0, 260, f"Score: {self.score}; Highest Record: {self.high_score}")

    # report the final score to the user
    def report(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
            self.write_text(0, 220, f"Your final score is {self.score};\n new record!")
        else:
            self.write_text(0, 220, f"Your final score is {self.score};\n the highest record is {self.high_score}")

    def reset(self):
        self.score = 0
        self.clear()
        self.write_text(0, 260, f"Score: {self.score}; Highest Record: {self.high_score}")


