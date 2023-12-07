import pygame
import json
from src.battle_seq import BattleSeq
from src.battle_dis import BattleDis
from src.save_selec import SaveSelec
from src.save_dis import SaveDis
from src.narration import ScrollingText
from src.movable import OverworldUnit
from src.overworld import Overworld
from src.save_prog import SaveProg

class Controller:

    def __init__(self):
        """
        Initializes the information necessary for pygame to run
        args: self
        return: None
        """
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.screen_width, self.screen_height = self.screen.get_size()
        self.state = "SELECTION"


    def main_loop(self):
        """
        Selects a screenloop for the game
        args: self
        return: None
        """
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
        """
        Selects a save file as well as allowing the player to reset their data
        args: self
        return: None
        """
        saving = SaveSelec()
        saving_view = SaveDis(self.screen, self.screen_width, self.screen_height)
        while self.state == "SELECTION":
            saving_view.save_display()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.save = saving.selection("1")
                        self.screen.fill("black")
                        self.state = "STORY"
                    if event.key == pygame.K_2:
                        self.save = saving.selection("2")
                        self.screen.fill("black")
                        self.state = "STORY"    
                    if event.key == pygame.K_3:
                        self.save = saving.selection("3")
                        self.screen.fill("black")
                        self.state = "STORY"
                    if event.key == pygame.K_r:
                        SaveProg().save_reset()

        # event loop

        # update data

        # redraw

    def story_loop(self):
        """
        Selects a line to scroll and guides the player on where to go
        args: self
        return: None
        """
        with open(r"../final-project-easy-py/assets/save_data.json", "r") as phew:
            save_data = json.load(phew)
            if save_data[self.save]["Progress"] == 0:
                self.file = r"../final-project-easy-py/assets/story_beginning.txt"
            if save_data[self.save]["Progress"] == 1:
                self.file = r"../final-project-easy-py/assets/story_middle.txt"
            if save_data[self.save]["Progress"] == 2:
                self.file = r"../final-project-easy-py/assets/story_end.txt"
            if save_data[self.save]["Progress"] == 3:
                self.file = r"../final-project-easy-py/assets/a_winner.txt"
        
        text = ScrollingText(self.screen, self.file, self.screen_width, self.screen_height)
        text.compile()
        while self.state == "STORY":
            text.scroll()
            text.refresh()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and save_data[self.save]["Progress"] < 3:
                        self.state = "OVERWORLD"
                    elif event.key == pygame.K_ESCAPE:
                        self.state = "GAMEOVER"
            
            
            
    
    def overworld_game_loop(self):
        """
        Allows the player to travel on an overworld and reach a designated destination
        args: self
        return: None
        """
        with open(r"../final-project-easy-py/assets/save_data.json", "r") as phew:
            save_data = json.load(phew)
            if save_data[self.save]["Progress"] == 0:
                self.place = "WEST"
            if save_data[self.save]["Progress"] == 1:
                self.place = "SOUTH"
            if save_data[self.save]["Progress"] == 2:
                self.place = "NORTH"
            adventure = Overworld(self.screen, self.screen_width, self.screen_height)
            adventurer = OverworldUnit(self.screen_height, self.screen_height)
            pos = adventurer.start()
            adventure.load_character()
            adventure.screen_jump(pos)
            adventure.refresh()
            while self.state == "OVERWORLD":
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            pos = adventurer.move("UP")
                            adventure.screen_jump(pos)
                            adventure.refresh()
                        if event.key == pygame.K_DOWN:
                            pos = adventurer.move("DOWN")
                            adventure.screen_jump(pos)
                            adventure.refresh()
                        if event.key == pygame.K_LEFT:
                            pos = adventurer.move("LEFT")
                            adventure.screen_jump(pos)
                            adventure.refresh()
                        if event.key == pygame.K_RIGHT:
                            pos = adventurer.move("RIGHT")
                            adventure.screen_jump(pos)
                            adventure.refresh()
                        if adventurer.destination(self.place):
                            self.state = "BATTLE"

        
        # event loop

        # update data

        # redraw

    def battle_gameloop(self):
        """
        Allows the player to battle other enemies
        args: self
        return: None"""
        with open(r"../final-project-easy-py/assets/save_data.json", "r") as phew:
            save_data = json.load(phew)
            if save_data[self.save]["Progress"] == 0:
                self.enemy = "Brigand"
            if save_data[self.save]["Progress"] == 1:
                self.enemy = "Swooper"
            if save_data[self.save]["Progress"] == 2:
                self.enemy = "Golu-Gross"
        completion = SaveProg(self.save)
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
                            battle_info = battle_do.in_battle("2")
                            battle_eye.battle_dialogue(battle_do.get_hp(), battle_info["Enemy Narration"]["Enemy Damage"])
            elif battle_do.in_battle()["Victory"] == False:
                battle_eye.loss()
                pygame.time.wait(5000)
                self.state = "GAMEOVER"
            elif battle_do.in_battle()["Victory"] == True:
                completion.save_update()
                battle_eye.victory()
                pygame.time.wait(5000)
                self.state = "STORY"

    def gameover_loop(self):
        """
        Quits the game
        args: self
        return: None
        """
        pygame.quit()
        exit()
        # event loop

        # update data

        # redraw