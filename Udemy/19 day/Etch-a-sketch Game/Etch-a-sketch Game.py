import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

colors = [
        (29, 112, 175),
        (235, 220, 228),
        (169, 13, 59),
        (211, 218, 233),
        (187, 14, 5),
        (159, 53, 114),
        (16, 133, 94),
        (15, 20, 98),
        ]    # timmy.speed('fastest')


timmy = Turtle()
screen = Screen()


def move_forward():
    # timmy.hideturtle()
    timmy.pencolor(random.choice(colors))
    timmy.speed('fastest')
    timmy.forward(10)
    timmy.right(135)
    timmy.forward(50)
    timmy.right(170)
    timmy.forward(44)
    timmy.right(54)
    timmy.forward(10)
    timmy.left(135)
    timmy.forward(50)
    timmy.left(170)
    timmy.forward(44)
    timmy.left(54)
    timmy.forward(15)




def move_back():
    timmy.dot(random.randint(15, 40), random.choice(colors))
    timmy.back(50)


def turn_left():
    timmy.left(15)


def turn_right():
    timmy.right(15)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear)
screen.exitonclick()