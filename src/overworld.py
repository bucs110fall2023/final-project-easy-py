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

    def screen_jump(self, coordinates):
        self.screen.blit(self.hero, coordinates)

    def refresh(self):
        pygame.display.flip()
        self.screen.fill("black")

def test():
    pygame.init()
    display = pygame.display.set_mode()
    width, height = pygame.display.get_window_size()
    explorer = Overworld(display, width, height)
    explorer.load_character()
    while True:
        explorer.screen_jump(500, 500)
        explorer.refresh()
# test()