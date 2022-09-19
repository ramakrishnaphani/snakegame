from turtle import Turtle


class Snake:

    def __init__(self):
        self.segments = []
        for _ in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.pu()
            new_segment.goto(_ * -20, 0)
            self.segments.append(new_segment)
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def tail_increment(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.goto(self.segments[-1].pos())
        self.segments.append(new_segment)
