import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()

screen.onkeypress(player.go_up, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Detect successful crossing.
    if player.ycor() > 280:
        player.reset_position()  # Reset position
        # Increase level by one
        # Increase cars speed.
        car_manager.speed_up()
    # Detect if turtle hit a car.
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
    car_manager.create_car()
    car_manager.move()

screen.exitonclick()
