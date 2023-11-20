import pygame
from src.unit import *
class Controller:

    def __init__(self):
        # setup pygame data
        pygame.init()
        self.screen = pygame.display.set_mode()


    def mainloop(self):
        # select state loop
        for event in pygame.event.get():
            if event == pygame.QUIT:
                exit()

      ### below are some sample loop states ###

    def menuloop(self):
        pass
        # event loop

        # update data

        # redraw

    def gameloop(self):
        pass
        # event loop

        # update data

        # redraw

    def gameoverloop(self):
        pass
        # event loop

        # update data

        # redraw
