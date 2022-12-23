
from turtle import Turtle

BORDER = 230


class Paddle(Turtle):
    """
    Instance class Paddle can be moved Up or Down, can handle collision with instance class Ball.
    """

    def __init__(self, coordinates: tuple):
        """
        To create instance class Paddle you must write coordinates (x: int, y: int) as an argument.
        """
        super().__init__()

        self.set_x = coordinates[0]
        self.set_y = coordinates[1]

        self.shape('square')
        self.color('white')
        self.speed('fastest')
        self.shapesize(stretch_len=5)

        self.penup()
        self.goto(self.set_x, self.set_y)
        self.setheading(90)

    def move_up(self):
        """
        Moves the paddle Up, stop working when the Paddle leans against the wall.
        """
        if self.ycor() < BORDER:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
        pass

    def move_down(self):
        """
        Moves the paddle Down, stop working when the Paddle leans against the wall.
        """
        if self.ycor() > -BORDER:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
        pass