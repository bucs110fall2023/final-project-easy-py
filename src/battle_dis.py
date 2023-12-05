import pygame

class BattleDis:

    def __init__(self, screen, length, width):
        """
        Accepts the pygame screen and its length and width as properties of the initialized object
        args : self
        return: None
        """        
        self.screen = screen
        self.length = length
        self.width = width

    def battle_screen(self, hp):
        """
        Displays the hp for the player character
        args: self, hp
        return: object
        """
        while True:   
            font = pygame.font.Font(None, int(self.width / 10))
            stats_msg = f"Merant: hp {hp}"
            player_hp = font.render(stats_msg, True, "white")
            self.screen.blit(player_hp, ((10, (self.width - (self.width / 10)))))
            return self.screen

    def battle_dialogue(self, hp, hero_damage=None, enemy_damage=None, enemy_name="ENEMY", victory_bool=False, loss_bool=False): # revisit, also a bust
        """
        displays battle dialogue based on the player's input
        args: self, hp, hero_damage, enemy_damage, enemy_name, victory_bool, loss_bool
        return: None
        """
        while True:    
            self.screen = self.battle_screen(hp) # can't have both at the same time.
            font = pygame.font.Font(None, int(self.width / 10))
            if hero_damage or hero_damage == 0:
                merant_damage_msg = f"Merant endured damage of {hero_damage}"
                battle_event = font.render(merant_damage_msg, True, "white")
                self.screen.blit(battle_event, ((10, (self.width / 10))))
                pygame.display.flip()
                self.screen.fill("black")
            if enemy_damage or enemy_damage == 0:
                enemy_damage_msg = f"{enemy_name} endured damage of {hero_damage}"
                battle_event = font.render(enemy_damage_msg, True, "white")
                self.screen.blit(battle_event, ((10, (self.width / 10))))
                pygame.display.flip()
                self.screen.fill("black")           
            if victory_bool:
                declaration = f"Merant Wins!"
                battle_event = font.render(declaration, True, "white")
                self.screen.blit(battle_event, ((10, (self.width / 2))))
                pygame.display.flip()
                self.screen.fill("black")
            if loss_bool:
                declaration = f"Merant Loses."
                battle_event = font.render(declaration, True, "white")
                self.screen.blit(battle_event, ((10, (self.width / 2))))
                pygame.display.flip()
                self.screen.fill("black")



def test():
    pygame.init()
    display = pygame.display.set_mode()
    length, width = pygame.display.get_window_size()
    test = BattleDis(display, length, width)
    test.battle_dialogue(10, 10)
test()
