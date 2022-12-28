from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("Courier", 24, "normal")


class Player(Turtle):
    """
    Class create instance Player.
    """

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('green')
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.level = 1

        self.level_word = Turtle()
        self.level_word.hideturtle()

    def move_up(self):
        """
        Makes the player move up.
        """
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        """
        Makes the player move down.
        """
        if self.ycor() > -275:
            self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
        pass

    def reset_player(self):
        """
        Reset player position to the starting point.
        """
        self.goto(STARTING_POSITION)

    def player_goto_next_level(self):
        """
        Increase level of the game on 1 and reset the player position.
        """
        if self.ycor() >= 280:
            self.level += 1
            self.reset_player()
            return True
