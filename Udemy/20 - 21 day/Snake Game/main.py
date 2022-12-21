
from turtle import Screen, Turtle
import time
from class__Snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('Snake game. Reva edition.')
screen.tracer(0)

snake = Snake()

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
    # snake.up()
    # snake.left()
    # snake.right()

screen.exitonclick()