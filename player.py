from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    # Set shape, starting position and heading of turtle
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    # Move the turtle up
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    # Moves the turtle to starting position
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    # Check if turtle is at finish line or not
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
