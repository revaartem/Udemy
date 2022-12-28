from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 2


class CarManager(Turtle):
    """
    Class for creating and manage objects named new_car.
    """

    def __init__(self, quantities_of_cars: int):
        """
        quantities_of_cars - how many instances will be crated on screen, when the game started
        """
        self.quantities_of_cars = quantities_of_cars
        super().__init__()
        self.cars = []
        self.adding_cars(self.quantities_of_cars)
        self.hideturtle()
        self.cars_for_adding = 5

    def adding_cars(self, quantities_of_cars: int):
        """
        Create instances, add them to list.
        """
        for _ in range(quantities_of_cars):
            new_car = Turtle(shape='square')
            new_car.penup()
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(random.randint(-270, 300), random.randint(-250, 250))
            new_car.setheading(180)
            self.cars.append(new_car)

    def car_home_position(self):
        """
        If the car ride out of the screen, func return the car to the "starting point" with
        random Y-axis position.
        """
        for car in self.cars:
            if car.xcor() < -320:
                car.goto(330, random.randint(-250, 250))
            else:
                pass

    def reset_car_position(self):
        """
        Place the car randomly on the screen.
        """
        for car in self.cars:
            car.goto(random.randint(-270, 280), random.randint(-250, 250))

    def all_cars_move(self, level):
        """
        Make the car move across the screen.
        """
        time.sleep(0.01)
        if level == 1:
            for car in self.cars:
                car.goto(car.xcor() - STARTING_MOVE_DISTANCE, car.ycor())
        if level > 1:
            increased_distance = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (level - 1))
            for car in self.cars:
                car.goto(car.xcor() - increased_distance, car.ycor())

    def car_collision(self, player):
        """
        Detect collision between the car and Player.
        """
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        else:
            return False
