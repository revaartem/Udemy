from turtle import Turtle, Screen
import random

race_switch = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet!', prompt='Who will win? (red, orange, yellow, green, blue, purple): ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
setpoints = [150, 90, 30, -30, -90, -150]
turtle_list = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, setpoints[turtle_index])
    turtle_list.append(new_turtle)

if user_bet:
    race_switch = True

while race_switch:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            race_switch -= 1
            win_color = turtle.pencolor()
            if win_color == user_bet.lower():
                print(f"You've won! The {win_color} turtle is the winner!")
            else:
                print(f"You've lost! The {win_color} turtle is the winner!")


        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
