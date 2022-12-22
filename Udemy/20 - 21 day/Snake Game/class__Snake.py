from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    An instance class Snake can move across the field (screen) in 4 directions,
    absorb into itself an instances class Food, then increase the length of the Snake by 1 segment
    per 1 peace of Food.
    """
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Create Snake starting "body"
        """

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Create Snake starting "body"
        """
        new_object = Turtle('square')
        new_object.color("darkgreen")
        new_object.penup()
        new_object.goto(position)
        self.segments.append(new_object)

    def extend(self):
        """
        Adds to the Snake's body 1 segment in the end of the body
        """
        last_segment = self.segments[-1]
        last_segment_position = last_segment.position()
        self.add_segment(last_segment_position)

    def move(self):
        """
        Moves the Snake's body forward
        """
        for box_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[box_num - 1].xcor()
            new_y = self.segments[box_num - 1].ycor()
            self.segments[box_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """
        Sets the vector of movement - "up"
        """
        if self.head.heading() != DOWN:
            return self.head.setheading(UP)

    def down(self):
        """
        Sets the vector of movement - "down"
        """
        if self.head.heading() != UP:
            return self.head.setheading(DOWN)

    def left(self):
        """
        Sets the vector of movement - "left"
        """
        if self.head.heading() != RIGHT:
            return self.head.setheading(LEFT)

    def right(self):
        """
        Sets the vector of movement - "right"
        """
        if self.head.heading() != LEFT:
            return self.head.setheading(RIGHT)
