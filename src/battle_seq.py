from src.unit import *

class BattleSeq:

    def __init__(self, save, name):
        self.merant = Hero(save, "Merant")
        self.enemy = Enemy(save, name)
        self.enemy_name = name

    def in_battle(self, input):
        while not (self.merant.lose() and self.enemy.win()):
            if input == "1":
                player_info = self.merant.attack(self.enemy_name)
                enemy_info = self.enemy.attack("Merant")
                return {"Player Narration": player_info, "Enemy Narration": enemy_info}
        if self.merant.lose():
            pass
        elif self.enemy.win():
            pass