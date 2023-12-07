
class OverworldUnit:

    def __init__(self, screen_width, screen_height):
        """
        Initializes the information the player unit in the overworld
        args: self, x, y, length, width
        return: None
        """
        self.screen_width = screen_width
        self.screen_height = screen_height

    def move(self, input):
        """
        Allows the player unit to move in the overworld
        args: self, input
        return: None
        """
        if input == "UP":
            self.y += 10
        elif input == "DOWN":
            self.y -= 10
        elif input == "RIGHT":
            self.x += 10
        elif input == "LEFT":
            self.x -= 10
        return self.x, self.y

    def start(self):
        self.x = self.screen_width / 2
        self.y = self.screen_height / 2

    def destination(self, objective):
        if objective == "WEST" and self.x == 0:
            return True
        if objective == "SOUTH" and self.y == self.screen_height:
            return True
        if objective == "NORTH" and self.y == 0:
            return True