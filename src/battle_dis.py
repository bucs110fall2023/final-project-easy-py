import pygame

class BattleDis:

    def __init__(self, screen, width, height):
        """
        Accepts the pygame screen and its width and height as properties of the initialized object
        args : self, screen, width, height
        return: None
        """        
        self.screen = screen
        self.height = height
        self.width = width

    def battle_screen(self, hp):
        """
        Displays the hp for the player character
        args: self, hp
        return: object
        """
        font = pygame.font.Font(None, int(self.height / 10))
        stats_msg = f"Merant: hp {hp}"
        player_hp = font.render(stats_msg, True, "white")
        self.screen.blit(player_hp, ((10, (self.height - (self.height / 10)))))
        sndstats_msg = "Press a key to attack, the mouse to rest"
        request = font.render(sndstats_msg, True, "white")
        self.screen.blit(request, ((10, (self.height - (self.height / 3)))))
        return self.screen

    def battle_dialogue(self, hp= None, hero_damage=None, enemy_damage=None, enemy_name="ENEMY", victory_bool=False, loss_bool=False): # revisit, also a bust
        """
        displays battle dialogue based on the player's input
        args: self, hp, hero_damage, enemy_damage, enemy_name, victory_bool, loss_bool
        return: None
        """   
        if hp == None: return None
        self.screen = self.battle_screen(hp) # can't have both at the same time.
        font = pygame.font.Font(None, int(self.height / 10))  
        if hero_damage or hero_damage == 0:
            merant_damage_msg = f"Merant endured damage of {hero_damage}"
            battle_event = font.render(merant_damage_msg, True, "white")
            self.screen.blit(battle_event, ((10, (self.height / 10))))
            pygame.display.flip()
            pygame.time.wait(2000)
            self.screen.fill("black")
            pygame.display.flip()
        elif enemy_damage or enemy_damage == 0:
            enemy_damage_msg = f"{enemy_name} endured damage of {hero_damage}"
            battle_event = font.render(enemy_damage_msg, True, "white")
            self.screen.blit(battle_event, ((10, (self.height / 10))))
            pygame.display.flip()
            pygame.time.wait(2000)
            self.screen.fill("black")
            pygame.display.flip()

    def victory(self):
        font = pygame.font.Font(None, int(self.height / 10))
        declaration = f"Merant Wins!"
        battle_event = font.render(declaration, True, "white")
        self.screen.blit(battle_event, ((10, (self.height / 2))))
        pygame.display.flip()
        pygame.time.wait(2000)
        self.screen.fill("black")
        pygame.display.flip()

    def loss(self):
        font = pygame.font.Font(None, int(self.height / 10))
        declaration = f"Merant Loses."
        battle_event = font.render(declaration, True, "white")
        self.screen.blit(battle_event, ((10, (self.height / 2))))
        pygame.display.flip()
        pygame.time.wait(2000)
        self.screen.fill("black")
        pygame.display.flip()
