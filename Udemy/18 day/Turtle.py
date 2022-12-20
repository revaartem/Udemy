import turtle
from turtle import Turtle, Screen
import random


timmy = Turtle()
turtle.colormode(255)


# for _ in range(50):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# range_int = 3
# for _ in range(15):
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#                "SeaGreen"]
#     timmy.color(random.choice(colours))
#     timmy.pensize(random.randint(1, 10))
#     timmy.speed(10)
#     angle = 360 / range_int
#     for _ in range(range_int):
#         timmy.forward(100)
#         timmy.right(angle)
#     range_int += 1

# distance = 30
#
# direction = [0, 90, 180, 270]
#
def random_colors():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return r, g, b
#
# timmy.pensize(5)
# timmy.speed(10)
#
# for _ in range(100):
#     timmy.pencolor(random_colors())
#     timmy.forward(distance)
#     timmy.setheading(random.choice(direction))
timmy.speed('fastest')
for _ in range(180):
    timmy.pencolor(random_colors())
    timmy.circle(100)
    timmy.left(1)

timmy.penup()
timmy.left(90)
timmy.forward(200)
timmy.right(90)
timmy.pendown()

for _ in range(180):
    timmy.pencolor(random_colors())
    timmy.circle(100)
    timmy.right(1)


screen = Screen()
screen.exitonclick()
