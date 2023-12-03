import pygame

class BattleDis:

    def __init__(self, screen, length, width):
        self.screen = screen
        self.length = length
        self.width = width

    def battle_screen(self, hp):
        while True:    
            font = pygame.font.Font(None, int(self.width / 10))
            stats_msg = f"Merant: hp {hp}"
            player_hp = font.render(stats_msg, True, "white")
            self.screen.blit(player_hp, ((10, (self.width - (self.width / 10)))))
            pygame.display.flip()

    def battle_dialogue(self, hp, hero_damage=None, enemy_damage=None, enemy_name=None, victory_bool=None, loss_bool=None): # revisit, also a bust
        while True:    
            self.battle_screen(hp) # can't have both at the same time.
            if hero_damage or hero_damage == 0:
                font = pygame.font.Font(None, int(self.width / 10))
                merant_damage_msg = f"Merant endured damage of {hero_damage}"
                battle_event = font.render(merant_damage_msg, True, "white")
                self.screen.blit(battle_event, ((10, (self.width / 10))))
                pygame.display.flip()
                self.screen.fill("black")
            if enemy_damage or enemy_damage == 0:
                font = pygame.font.Font(None, int(self.width / 10))
                enemy_damage_msg = f"{enemy_name} endured damage of {hero_damage}"
                battle_event = font.render(enemy_damage_msg, True, "white")
                self.screen.blit(battle_event, ((10, (self.width / 10))))
                pygame.display.flip()
                self.screen.fill("black")           
            if victory_bool:
                font = pygame.font.Font(None, int(self.width / 10))
                declaration = f"Merant Wins!"
                battle_event = font.render(declaration, True, "white")
                self.screen.blit(battle_event, ((10, (self.width / 2))))
                pygame.display.flip()
                self.screen.fill("black")
            if loss_bool:
                font = pygame.font.Font(None, int(self.width / 10))
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
