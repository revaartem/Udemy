
from turtle import Turtle


class Ball(Turtle):
    """
    Instance class Ball can move across the play field, detect and handle collisions with walls and
    instance class Paddle.
    """

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 6
        self.y_move = 6

    def move(self):
        """
        Move the ball according to the processed coordinates.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Changing the increasing of Y-axis to the opposite way.
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Changing the increasing of X-axis to the opposite way.
        """
        self.x_move *= -1

    def ball_reset(self):
        """
        Re-create "ball" in the center of the screen.
        """
        self.bounce_x()
        self.bounce_y()
        self.goto(0, 0)