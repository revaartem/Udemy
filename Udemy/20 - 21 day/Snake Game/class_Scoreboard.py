
from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('arial', 20, 'bold')


class Scoreboard(Turtle):
    """
    An instance class Scoreboard show current score on the screen, increase score and show "GAME OVER"
    """
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('black')
        self.goto(0, 240)
        self.score_write()

    def increase_score(self):
        """
        Add to score +1
        """
        self.score += 1

    def score_write(self):
        """
        Show to the player current score on the screen
        """
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Show to the player message "GAME OVER"
        """
        self.penup()
        self.goto(0, 0)
        self.color('red')
        self.write('GAME OVER', align=ALIGNMENT, font=('arial', 45, 'normal'))
