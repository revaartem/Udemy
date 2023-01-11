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
        with open("data.txt") as high_score:
            self.high_score = int(high_score.read())
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
        self.write(f'Score: {self.score} High score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", "w") as high_score:
            high_score.write(f'{self.high_score}')
        self.score = 0
        self.score_write()
