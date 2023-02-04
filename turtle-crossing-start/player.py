from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280

"""
Create a turtle player that starts at the bottom of the screen
 and listen for the "Up" keypress to move the turtle north.
"""
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.reset_position()

    def go_up(self):
        """
        Function handles forward movement for the player.
        """
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)
