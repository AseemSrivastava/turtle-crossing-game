import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create object of player class
player = Player()
# Create object for car_manager class
car_manager = CarManager()

# Listen keystrokes
screen.listen()
screen.onkey(player.go_up, "Up")
car_list = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
