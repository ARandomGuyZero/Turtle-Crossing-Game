"""
Turtle Crossing

Author: Alan
Date: September 10th

This script generates the famous Crossing game.
The player controls the turtle with the Up arrow key or W key.
If they manage to cross to the other side, they'll go to the next level.
If they get hit by a car, the game ends.
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Create new screen object to configure the width, height, title and its background color
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create new objects for the game elements
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Configure player movement
screen.listen()
screen.onkeypress(player.go_forwards, "w")
screen.onkeypress(player.go_forwards, "Up")

game_is_on = True

# Simple loop get the game on
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create a new car
    car_manager.create_car()
    # Move the car
    car_manager.move_cars()

    # Detect collision with the player
    for car in car_manager.all_cars:
        # If it detects a collision, the game ends
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect if the player got to finish line, if they do, the game restarts, increasing speed.
    if player.is_player_at_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.score_point()

screen.exitonclick()