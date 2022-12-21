from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.boxes = []
        self.create_snake()
        self.head = self.boxes[0]

    def create_snake(self):

        for position in STARTING_POSITIONS:
            new_object = Turtle('square')
            new_object.color("white")
            new_object.penup()
            new_object.goto(position)
            self.boxes.append(new_object)

    def move(self):
        for box_num in range(len(self.boxes) - 1, 0, -1):
            new_x = self.boxes[box_num - 1].xcor()
            new_y = self.boxes[box_num - 1].ycor()
            self.boxes[box_num].goto(new_x, new_y)
        self.boxes[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            return self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            return self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            return self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            return self.head.setheading(RIGHT)