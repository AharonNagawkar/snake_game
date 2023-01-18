from turtle import Turtle

init_pos = [(20, 0), (0, 0), (-20, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in init_pos:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape='square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.snake.append(segment)

    def extend(self):
        self.add_segment(self.snake[-1].pos())

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_pos = self.snake[seg_num - 1].pos()
            self.snake[seg_num].goto(new_pos)
        self.head.forward(MOVE_DISTANCE)

    def portal_snake(self):
        current = self.head.pos()
        if abs(self.head.pos()[0]) >= 290:
            self.head.goto(current[0] * -1, current[1])
        else:
            self.head.goto(current[0], current[1] * -1)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
