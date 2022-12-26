import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_COORDINATE = 230


# for y -230 to +230,,,for x it is fixed at +230

class CarManager:
    def __init__(self):
        self.all_cars = []

    # Create a car at random location at right edge of screen
    def create_car(self):
        # Generate a new car only if 1 is present (1 in 6 chance of generating a new car )
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    # Move the created cars from right to left of screen
    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
