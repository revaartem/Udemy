from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    Show current level on the screen, show "game over" if the game ends.
    """

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.level = 1
        self.score_write()

    def increase_score(self):
        """
        Increases level by 1 inside current class
        """
        self.level += 1

    def score_write(self):
        """
        Writes current level on the screen.
        """
        self.clear()
        self.write(f'Level : {self.level}', font=FONT)

    def next_level(self):
        """
        Re-writes current level on the screen.
        """
        self.increase_score()
        self.score_write()
        time.sleep(3)

    def game_over(self):
        """
        Writes "Game over"
        """
        self.penup()
        self.goto(0, 0)
        self.color('red')
        self.write('GAME OVER', align='center', font=('arial', 45, 'normal'))
