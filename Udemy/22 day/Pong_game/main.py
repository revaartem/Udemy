from turtle import Screen
from class_Paddle import Paddle
from class_Ball import Ball
from class_Scoreboard import Scoreboard
import time

if __name__ == "__main__":
    screen = Screen()

    screen.tracer(0)

    right_paddle = Paddle((350, 0))
    left_paddle = Paddle((-350, 0))
    ball = Ball()
    score = Scoreboard()

    screen.setup(height=600, width=800)
    screen.title('Pong. The game.')
    screen.bgpic('background.png')
    screen.bgcolor('black')
    screen.listen()

    # right_paddle movement
    screen.onkey(right_paddle.move_up, 'Up')
    screen.onkey(right_paddle.move_down, 'Down')

    # left_paddle movement
    screen.onkey(left_paddle.move_up, 'w')
    screen.onkey(left_paddle.move_down, 's')

    game_on = True  # Game switch

    while game_on:
        speed_of_ball = 0.02
        time.sleep(speed_of_ball)
        screen.update()

        # If ball touch upper wall or bottom wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # If ball touch right paddle
        if ball.xcor() > 330 and ball.distance(right_paddle) < 50:
            ball.bounce_x()

        # If ball touch left paddle
        if ball.xcor() < -330 and ball.distance(left_paddle) < 50:
            ball.bounce_x()

        # If ball go past right paddle
        if ball.xcor() > 370:
            score.l_increase_score()
            ball.ball_reset()

        # If ball go past Left paddle
        if ball.xcor() < -370:
            score.r_increase_score()
            ball.ball_reset()

        ball.move()

    screen.exitonclick()
