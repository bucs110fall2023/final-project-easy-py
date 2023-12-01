
class OverworldUnit:

    def __init__(self, x, y, length, width):
        """
        Initializes the information the player unit in the overworld
        args: self, x, y, length, width
        return: None
        """
        self.x = x
        self.y = y
        self.length = length # proportion of screen
        self.width = width # proportion of screen 

    def move(self, input):
        """
        Allows the player unit to move in the overworld
        args: self, input
        return: None
        """
        if input == "UP":
            self.y += 30
        elif input == "DOWN":
            self.y -= 30
        elif input == "RIGHT":
            self.x += 30
        elif input == "LEFT":
            self.x -= 30