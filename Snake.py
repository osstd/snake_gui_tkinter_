from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        square_ = Turtle(shape="square")
        square_.color("white")
        square_.penup()
        square_.goto(position)
        self.segments.append(square_)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()

    def right(self):
        if self.segments[0].heading() != left:
            self.segments[0].setheading(right)

    def left(self):
        if self.segments[0].heading() != right:
            self.segments[0].setheading(left)

    def up(self):
        if self.segments[0].heading() != down:
            self.segments[0].setheading(up)

    def down(self):
        if self.segments[0].heading() != up:
            self.segments[0].setheading(down)
