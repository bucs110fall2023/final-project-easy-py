import pygame
from src.battle_seq import Hero, Enemy, BattleSeq
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
                self.selection_loop()
            if self.state == "STORY":
                self.story_loop()
            if self.state == "OVERWORLD":
                self.overworld_game_loop()
            if self.state == "BATTLE":
                self.battle_gameloop()
            if self.state == "GAMEOVER":
                self.gameover_loop()


      ### below are some sample loop states ###

    def selection_loop(self):
        pass
        # event loop

        # update data

        # redraw

    def story_loop(self):
        pass
    
    def overworld_game_loop(self):
        pass
        # event loop

        # update data

        # redraw

    def battle_gameloop():
        pass
    
    def gameover_loop(self):
        pass
        # event loop

        # update data

        # redraw
