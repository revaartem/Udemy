import random
from turtle import Turtle


class Food(Turtle):
    """
    An instance class Food can be "eaten" by an instance of the class Snake and
    increase the Snake by 1 segment per 1 peace of Food.
    Instances class Food are generated on screen in random places.
    """
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        # self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """
        Generated another peace of Food in random place
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
