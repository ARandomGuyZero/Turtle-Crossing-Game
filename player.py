from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    """
    This class contains the logic of the player
    """
    def __init__(self):
        super().__init__()
        self.shape("turtle") # Shape of the player to reassemble the turtle
        self.penup() # Disable drawing
        self.left(90) # Turns the turtle to look up
        self.go_to_start() # Move the turtle to the starting line

    def go_forwards(self):
        """
        Moves the player forwards
        """
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """
        Moves the player to the start
        """
        self.goto(STARTING_POSITION)

    def is_player_at_finish_line(self):
        """
        Checks if the player is at the finishing line
        :return: True if they are, False if not
        """
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False