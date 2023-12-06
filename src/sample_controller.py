import pygame
from src.battle_seq import Hero, Enemy, BattleSeq
from src.battle_dis import BattleDis
from src.save_selec import SaveSelec
from src.save_dis import SaveDis
from src.narration import ScrollingText
class Controller:

    def __init__(self):
        # setup pygame data
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.screen_width, self.screen_height = self.screen.get_size()
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
        
        saving = SaveSelec()
        saving_view = SaveDis(self.screen, self.screen_width, self.screen_height)
        while self.state == "SELECTION":
            saving_view.save_display()
            for event in pygame.event.get:
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_1:
                        saving.selection("1")
                    if event.tyoe == pygame.K_2:
                        saving.selection("2")
                    if event.type == pygame.K_3:
                        saving.selection("3")
                    self.state = "STORY"
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
