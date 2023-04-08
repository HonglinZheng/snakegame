from turtle import Turtle
# global keys
ORIGINAL_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
PACE = 10
RIGHT_DIR = 0
UP_DIR = 90
LEFT_DIR = 180
DOWN_DIR = 270


class Snake:
    def __init__(self):
        self.segments = []
        for position in ORIGINAL_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.shapesize(0.5, 0.5)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # extend the body length of snake after eating
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(PACE)

    def up(self):
        if self.head.heading() != DOWN_DIR:
            self.head.setheading(UP_DIR)

    def down(self):
        if self.head.heading() != UP_DIR:
            self.head.setheading(DOWN_DIR)

    def left(self):
        if self.head.heading() != RIGHT_DIR:
            self.head.setheading(LEFT_DIR)

    def right(self):
        if self.head.heading() != LEFT_DIR:
            self.head.setheading(RIGHT_DIR)

    def detect_collision(self):
        # collision with snake body
        for body in self.segments[1:]:
            if self.head.distance(body) < 8:
                print("body hit!!")
                return True
        # collision with walls
        return self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280

