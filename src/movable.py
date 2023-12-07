
class OverworldUnit:

    def __init__(self, screen_width, screen_height):
        """
        Initializes the information the player unit in the overworld
        args: self, screen_width, screen_height
        return: None
        """
        self.screen_width = screen_width
        self.screen_height = screen_height

    def move(self, input):
        """
        Allows the player unit to move in the overworld
        args: self, input
        return: tuple
        """
        if input == "UP":
            self.y -= 40
        elif input == "DOWN":
            self.y += 40
        elif input == "RIGHT":
            self.x += 40
        elif input == "LEFT":
            self.x -= 40
        return self.x, self.y

    def start(self):
        """
        Places the player character at the center of the screen
        args: self
        return: tuple
        """
        self.x = self.screen_width / 2
        self.y = self.screen_height / 2
        return self.x, self.y
    
    def destination(self, objective):
        """
        Checks if the player has reached their destination
        args: self, objective
        return: boolean
        """
        if objective == "WEST" and self.x <= 0:
            return True
        if objective == "SOUTH" and self.y >= self.screen_height:
            return True
        if objective == "NORTH" and self.y <= 0:
            return True