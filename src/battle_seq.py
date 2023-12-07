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

    def get_hp(self):
        """
        Gets the hp of the player charater
        args: self
        return: integer
        """
        return self.merant.hp
    
    def in_battle(self, input=None):
        """
        Follows the events of a battle (the main part of the game)
        args: self input
        return: dictionary, boolean
        """
        if input == "1":
            player_info = self.merant.attack(self.enemy)
            enemy_info = self.enemy.attack(self.merant)
            return {"Player Narration": player_info, "Enemy Narration": enemy_info}
        if input == "2":
            player_info = self.merant.heal()
            enemy_info = self.enemy.attack(self.merant)
            return {"Player Narration": player_info, "Enemy Narration": enemy_info}
        if self.merant.lose():
            return {"Victory": False}
        elif self.enemy.win():
            return {"Victory": True}
        else:
            return None