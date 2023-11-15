import json


class Unit:

    def __init__(self, save, name):
        with open("save_data.json") as stats:

            #r we using the json as a memory to load previous data through a username? I feel like that would be the best way to store it 
            # if I understand what you're saying, then yeah
            stat = json.load(stats)
            self.ackt = stat[str(save)]["Unit Stats"][str(name)]["Attack"]
            self.defn = stat[str(save)]["Unit Stats"][str(name)]["Defense"]
            self.ackt = stat[str(save)]["Unit Stats"][str(name)]["Attack"]
            self.max_hp = stat[str(save)]["Unit Stats"][str(name)]["Maximum Health Points"]
            self.max_mp = stat[str(save)]["Unit Stats"][str(name)]["Maximum Magic Points"]
            self.hp = self.max_hp
            self.mp = self.max_mp

    def attack(self, opponent):
        damage = self.ackt - opponent.defn
        if damage <= 0:
            return "No Sell"
        else:
            opponent.hp = opponent.hp - damage
            return {"Opponent": opponent.name, "Enemy Damage": damage}


class Enemy(Unit):
    def __init__(self, save, name):
        with open("save_data.json") as stats:
            super().__init__(save, name)
            stat = json.load(stats)
            self.exp_val = stat[str(save)]["Unit Stats"][str(name)]["Experience Value"]

    def win(self):
        if self.hp <= 0:
            return True
        else:
            return False


class Hero(Unit):
    def __init__(self, save, name):
        with open("save_data.json") as stats:
            super().__init__(save, name)
            stat = json.load(stats)
            self.exp_pnts = stat[str(save)]["Unit Stats"][str(name)]["Experience Points"]
            self.exp = stat[str(save)]["Unit Stats"][str(name)]["Current Experience"]

    def lose(self):
        if self.hp <= 0:
            return True
        else:
            return False
    
    def exp_gain(self, opponent):
        self.exp =+ opponent.exp_val

    def level_up(self):
        pass