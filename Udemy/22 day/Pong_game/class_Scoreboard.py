
from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('arial', 30, 'bold')


class Scoreboard(Turtle):
    """
    An instance class Scoreboard show the current score on the screen and increase the score.
    """

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.r_score = 0
        self.l_score = 0
        self.goto(0, 250)
        self.score_write()
        screen_divider = Turtle()
        screen_divider.hideturtle()
        screen_divider.penup()
        screen_divider.goto(6, -350)
        screen_divider.write('|\n \n' * 12, align=ALIGNMENT, font=('arial', 15, 'bold'))

    def r_increase_score(self):
        """
        Increase score of the right player by 1
        """
        self.r_score += 1
        self.score_write()

    def l_increase_score(self):
        """
        Increase score of the left player by 1
        """
        self.l_score += 1
        self.score_write()

    def score_write(self):
        """
        Showing current score on the screen
        """
        self.clear()
        self.write(f" {self.l_score} : {self.r_score}", align=ALIGNMENT, font=FONT)
