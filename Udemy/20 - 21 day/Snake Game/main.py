
from turtle import Screen
import time
from class__Snake import Snake
from class_Food import Food
from class_Scoreboard import Scoreboard


if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgpic("font_for_snake_game.png")
    screen.title('Snake game. Reva edition.')
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')

    game_switch = True
    while game_switch:
        screen.update()
        time.sleep(0.1)

        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 25:
            food.refresh()
            snake.extend()
            score.increase_score()
            score.score_write()

        # Detect collision with wall
        border = 263
        if snake.head.xcor() > border or snake.head.xcor() < -border or snake.head.ycor() > border or snake.head.ycor() < -border:
            score.game_over()
            game_switch = False

        # Detect collision with tail
        for segment in snake.segments[1:]:
            # if segment == snake.head:
            #     pass
            if snake.head.distance(segment) < 10:
                game_switch = False
                score.game_over()


    screen.exitonclick()
