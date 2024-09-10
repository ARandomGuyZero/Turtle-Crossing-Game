from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    """
    This class has the logic of the scoreboard
    """
    def __init__(self):
        super().__init__()
        self.hideturtle() # hides the turtle
        self.penup() # Disable drawing
        self.goto(-280, 260) # Goes to the top left of the screen
        self.score = 1 # Stores the score
        self.show_score()

    def show_score(self):
        """
        Shows the score of the game
        """
        self.clear()
        self.write(f"Level {self.score}", font=FONT)

    def score_point(self):
        """
        Adds a point to the total score
        """
        self.score += 1
        self.show_score()

    def game_over(self):
        """
        Prints Game Over at the center of the screen
        """
        self.goto(0,0)
        self.write("Game Over", font=FONT)