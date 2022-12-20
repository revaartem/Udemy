
import turtle
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
        ]

timmy = turtle.Turtle()
timmy.penup()
timmy.setpos(-200.0, -200.0)
upper = -200
timmy.hideturtle()

for _ in range(10):

    timmy.setpos(-200, upper)
    for _ in range(10):

        timmy.dot(random.randint(15, 40), random.choice(colors))
        timmy.forward(50)
    upper += 50



screen = turtle.Screen()
screen.exitonclick()
