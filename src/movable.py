
class OverworldUnit:

    def __init__(self, x, y, width, height, screen_width, screen_height):
        """
        Initializes the information the player unit in the overworld
        args: self, x, y, length, width
        return: None
        """
        self.x = x
        self.y = y
        self.height = height # proportion of screen
        self.width = width # proportion of screen 
        self.screen_width = screen_width
        self.screen_height = screen_height

    def move(self, input):
        """
        Allows the player unit to move in the overworld
        args: self, input
        return: None
        """
        if input == "UP":
            self.y += 1 / self.screen_height
        elif input == "DOWN":
            self.y -= 1 / self.screen_height
        elif input == "RIGHT":
            self.x += 1 / self.screen_width
        elif input == "LEFT":
            self.x -= 1 / self.screen_width

    def start(self):
        self.x = self.width / 2
        self.y = self.height / 2

    def destination(self, objective):
        if objective == "WEST" and self.x == 0:
            return True
        if objective == "SOUTH" and self.y == self.height:
            return True
        if objective == "NORTH" and self.y == 0:
            return True