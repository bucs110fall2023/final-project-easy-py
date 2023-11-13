import json


class Unit:

    def __init__(self, save, name):
        with open("save_data.json") as stats:
            json.load(stats)
            self.ackt = stats[str(save)][str(name)]["Attack"]
            self.defn = stats[str(save)][str(name)]["Defence"]
            self.ackt = stats[str(save)][str(name)]["Attack"]
            self.max_hp = stats[str(save)][str(name)]["Maximum Health Points"]
            self.max_mp = stats[str(save)][str(name)]["Maximum Magic Points"]
            self.hp = self.max_hp
            self.mp = self.max_mp



class Enemy(Unit):
    pass


class Hero(Unit):
    pass