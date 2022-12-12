# from turtle import Turtle, Screen
#
# tom = Turtle()
# tom.shape('turtle')
# tom.color("cyan")
# tom.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon name', ['Pikachu', 'Squirtle', 'Pringles'], "l")
table.add_column('Type', ['Electric', 'Water', 'Fire'], "l")
print(table)