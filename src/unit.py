import json


class Unit:

    def __init__(self, save, name):
        with open("save_data.json") as stats:

            #r we using the json as a memory to load previous data through a username? I feel like that would be the best way to store it 
            # if I understand what you're saying, then yeah
            stat = json.load(stats)
            self.ackt = stat[str(save)]["Unit Stats"][str(name)]["Attack"]
            self.defn = stat[str(save)]["Unit Stats"][str(name)]["Defense"]
            self.max_hp = stat[str(save)]["Unit Stats"][str(name)]["Maximum Health Points"]
            self.max_mp = stat[str(save)]["Unit Stats"][str(name)]["Maximum Magic Points"]
            self.hp = self.max_hp
            self.mp = self.max_mp
            self.save = save
            self.name = name

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
            self.curr_lvl = 0

    def lose(self):
        if self.hp <= 0:
            return True
        else:
            return False
    
    def exp_gain(self, opponent):
        self.exp =+ opponent.exp_val

    def level_up(self):
        for i in self.exp_pnts:
            if self.curr_lvl < self.exp_pnts.keys()[i] and self.exp > self.exp_pnts[i]:
                ackt_inc = range(1, 4)
                hp_inc = range(1, 4)
                defe_inc = range(1, 4)
                mp_inc = range(1, 4)
                with open("save_data.json", "w") as updated_txt:
                    update = json.load(updated_txt)
                    update[str(self.save)]["Unit Stats"][str(self.name)]["Attack"] += ackt_inc
                    update[str(self.save)]["Unit Stats"][str(self.name)]["Defense"] += defe_inc
                    update[str(self.save)]["Unit Stats"][str(self.name)]["Maximum Health Points"] += hp_inc
                    update[str(self.save)]["Unit Stats"][str(self.name)]["Maximum Magic Points"] += mp_inc
                    json.dump(update, updated_txt, indent=4)

