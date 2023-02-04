import random
from turtle import Turtle

COLORS = ["red", "orange", "turquoise", "green", "blue", "purple", "magenta", "black"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        """
        Function handles creation of each car.
        """
        random_chance = random.randint(1, 6)  # Randomising a number to reduce the number
        # of cars that are being generated on the screen.
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Making the car shape itself.
            new_car.color(random.choice(COLORS))  # Randomising a color for each car.
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def speed_up(self):
        """
        Function handles the speed of the cars when the player has successfully passed a stage.
        """
        x_move = STARTING_MOVE_DISTANCE + 1
        return x_move
