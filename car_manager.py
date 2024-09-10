import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    """
    This class has the logic of the car manager
    """
    def __init__(self):
        super().__init__()
        self.all_cars = [] # List of cars
        self.car_speed = STARTING_MOVE_DISTANCE # Speed of the car

    def create_car(self):
        """
        Creates a car for the user to avoid
        """
        random_chance = random.randint(1, 100)

        # The car has a chance to spawn
        if random_chance < 10:
            new_car = Turtle("square") # New square turtle
            new_car.shapesize(1, 2) # Car size
            new_car.penup() # Disable Drawing
            new_car.color(random.choice(COLORS)) # Randomly choices the car's color
            new_car.goto(300, random.randrange(-251, 251, 20)) # Generates the car in a random y-axis in the left side
            self.all_cars.append(new_car) # Appends the car to the all_car list

    def move_cars(self):
        """
        Moves each of the car in all_cars
        """
        for car in self.all_cars:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())

    def increase_speed(self):
        """
        Increases the speed of the cars
        """
        self.car_speed += MOVE_INCREMENT