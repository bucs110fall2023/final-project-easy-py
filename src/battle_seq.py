from src.unit import Hero, Enemy

class BattleSeq:

    def __init__(self, save, name):
        """
        Initializes the classes that are going to be in the battle sequence
        args: self, save, name
        return: None
        """
        self.merant = Hero(save, "Merant")
        self.enemy = Enemy(save, name)
        self.enemy_name = name

    def in_battle(self, input):
        """
        Follows the events of a battle (the main part of the game)
        args: self input
        return: None
        """
        while not (self.merant.lose() and self.enemy.win()):
            if input == "1":
                player_info = self.merant.attack(self.enemy_name)
                enemy_info = self.enemy.attack("Merant")
                return {"Player Narration": player_info, "Enemy Narration": enemy_info}
        if self.merant.lose():
            pass
        elif self.enemy.win():
            pass