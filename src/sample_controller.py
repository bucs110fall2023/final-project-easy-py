import pygame
import json
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
                    if event.key == pygame.K_1:
                        self.save = saving.selection("1")
                    if event.key == pygame.K_2:
                        self.save = saving.selection("2")
                    if event.key == pygame.K_3:
                        self.save = saving.selection("3")
                    self.state = "STORY"
        # event loop

        # update data

        # redraw

    def story_loop(self):
        
        while self.state == "STORY":
            pass
            
    
    def overworld_game_loop(self):
        pass
        # event loop

        # update data

        # redraw

    def battle_gameloop(self):
        with open(r"../final-project-easy-py/assets/save_data.json", "r") as phew:
            save_data = json.load(phew)
            if save_data[self.save]["Progress"] == 0:
                self.enemy = "Brigand"
            if save_data[self.save]["Progress"] == 1:
                self.enemy = "Swooper"
            if save_data[self.save]["Progress"] == 2:
                self.enemy = "Golu-Gross"
        battle_do = BattleSeq(self.save, self.enemy)
        battle_eye = BattleDis(self.screen, self.screen_width, self.screen_height)
        while self.state == "BATTLE":
            if battle_do.in_battle() == None: 
                battle_eye.battle_screen(battle_do.get_hp())
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN: # ADD README WAIT
                        if event.key == pygame.K_1:
                            self.screen.fill("black")
                            battle_eye.battle_screen(battle_do.get_hp())
                            battle_info = battle_do.in_battle("1")
                            battle_eye.battle_dialogue(battle_do.get_hp(), None, battle_info["Player Narration"]["Enemy Damage"], battle_info["Player Narration"]["Opponent"])
                            battle_eye.battle_dialogue(battle_do.get_hp(), battle_info["Enemy Narration"]["Enemy Damage"])
                        elif event.key == pygame.K_2:
                            print("2")
                            battle_info = battle_do.in_battle("2")
                            battle_eye.battle_dialogue(battle_do.get_hp(), battle_info["Enemy Narration"]["Enemy Damage"])
            elif battle_do.in_battle()["Victory"] == False:
                battle_eye.loss()
                pygame.time.wait(5000)
                self.state = "GAMEOVER"
            elif battle_do.in_battle()["Victory"] == True:
                battle_eye.victory()
                pygame.time.wait(5000)
                self.state = "STORY"

    def gameover_loop(self):
        pygame.quit()
        exit()
        # event loop

        # update data

        # redraw