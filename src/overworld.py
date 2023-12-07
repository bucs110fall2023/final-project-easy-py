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
        self.hero = pygame.image.load(r"../final-project-easy-py/assets/Hero.png")

    def screen_jump(self, x, y):
        self.screen.blit(self.hero, x, y, 50)