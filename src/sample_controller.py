import pygame
from src.battle_seq import *
class Controller:

    def __init__(self):
        # setup pygame data
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.screen_width, self.screen_length = self.screen.get_size()
        self.state = "SELECTION"


    def main_loop(self):
        # select state loop
        while True:
            if self.state == "SELECTION":
                self.selectionloop()


      ### below are some sample loop states ###

    def selection_loop(self):
        pass
        # event loop

        # update data

        # redraw

    def overworld_game_loop(self):
        pass
        # event loop

        # update data

        # redraw

    def battle_gameloop
    
    def gameover_loop(self):
        pass
        # event loop

        # update data

        # redraw
