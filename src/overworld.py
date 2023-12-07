import pygame

class Overworld:

    def __init__(self, screen, width, height):
        """
        Accepts the pygame screen and its width and height as properties of the initialized object
        args : self, screen, width, height
        return: None
        """
        self.screen = screen
        self.height = height
        self.width = width


    def load_character(self):
        """
        Loads the image of the player character
        args: self
        return: None
        """
        self.hero = pygame.image.load(r"../final-project-easy-py/assets/Hero.png")

    def screen_jump(self, coordinates):
        """
        Displays the player character on screen
        args: self, coordinates
        return: None
        """
        self.screen.blit(self.hero, coordinates)

    def refresh(self):
        """
        Refreshes the screen
        args: self
        return: None
        """        
        pygame.display.flip()
        self.screen.fill("black")
