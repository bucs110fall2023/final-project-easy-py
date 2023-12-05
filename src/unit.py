import json
import pygame

class Unit:

    def __init__(self, save, name):
        """
        Initializes the object for the rpg unit as well as takes properties found in the JSON file
        args: self, save, name
        return: None
        """
        with open(r"../assets/save_data.json") as stats:

            stat = json.load(stats)
            self.ackt = stat[save]["Unit Stats"][name]["Attack"]
            self.defn = stat[save]["Unit Stats"][name]["Defense"]
            self.max_hp = stat[save]["Unit Stats"][name]["Maximum Health Points"]
            self.max_mp = stat[save]["Unit Stats"][name]["Maximum Magic Points"]
            self.hp = self.max_hp
            self.mp = self.max_mp
            self.save = save
            self.name = name

    def attack(self, opponent):
        """
        The rpg unit attacks the opponent using the attack stat
        args: self, opponent
        return: dictionary
        """
        damage = self.ackt - opponent.defn
        if damage <= 0:
            return {"Opponent": opponent.name, "Lack of Damage": "No sell"}
        else:
            opponent.hp = opponent.hp - damage
            return {"Opponent": opponent.name, "Enemy Damage": damage}


class Enemy(Unit):
    def __init__(self, save, name):
        """
        Inherits from the Unit class as well as having a value for experience
        args: self, save, name
        returns: None
        """
        with open(r"../assets/save_data.json") as stats:
            super().__init__(save, name)
            stat = json.load(stats)
            self.exp_val = stat[save]["Unit Stats"][name]["Experience Value"]
            self.weak_pnt = stat[save]["Unit Stats"][name]["Weakness"]

    def win(self):
        """
        Checks if the player wins
        args: self
        returns: boolean
        """
        if self.hp <= 0:
            return True
        else:
            return False


class Hero(Unit):
    def __init__(self, save, name):
        """
        Inherits from the Unit class as well as accepting Exp points, Current exp, and Current Level
        args: self, save, name
        returns: None
        """
        with open(r"../assets/save_data.json") as stats:
            super().__init__(save, name)
            stat = json.load(stats)
            self.exp_pnts = stat[save]["Unit Stats"][name]["Experience Points"]
            self.exp = stat[save]["Unit Stats"][name]["Current Experience"]
            self.curr_lvl = stat[save]["Unit Stats"][name]["Current Level"]

    def lose(self):
        """
        Checks if the player loses
        args: self
        returns: boolean
        """  
        if self.hp <= 0:
            return True
        else:
            return False
    
    def exp_gain(self, opponent):
        """
        Keep tract of exp gain
        args: self, opponent
        return: None
        """
        self.exp =+ opponent.exp_val

    def level_up(self):
        """
        Provides the sequence for the player character leveling up
        args: self
        returns: dictionary
        """
        for i in self.exp_pnts:
            if self.curr_lvl < self.exp_pnts.keys()[i] and self.exp > self.exp_pnts[i]:
                self.curr_lvl += 1
                ackt_inc = range(1, 4)
                hp_inc = range(1, 4)
                defe_inc = range(1, 4)
                mp_inc = range(1, 4)
                with open(r"../assets/save_data.json", "w") as updated_txt:
                    update = json.load(updated_txt)
                    update[self.save]["Unit Stats"][self.name]["Attack"] += ackt_inc
                    update[self.save]["Unit Stats"][self.name]["Defense"] += defe_inc
                    update[self.save]["Unit Stats"][self.name]["Maximum Health Points"] += hp_inc
                    update[self.save]["Unit Stats"][self.name]["Maximum Magic Points"] += mp_inc
                    update[self.save]["Unit Stats"][self.name]["Maximum Magic Points"] = self.curr_lvl
                    json.dump(update, updated_txt, indent=4)
                return {"Merant": self.name, "Attack": str(ackt_inc), "Defense": str(defe_inc), "Health Points": str(hp_inc), "Magic Points": str(mp_inc), "New Level": str(self.curr_lvl)}
            else:
                return {}






pygame.init()

#game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Health Bar')


class HealthBar:
    def __init__(self, x, y, w, h, max_hp):
        """
        

        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.max_hp = max_hp

    def draw(self, surface):
        """
        draws the hero's health bar
        args: self, surface
        return: 
        """
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))


health_bar = HealthBar(250, 200, 300, 40, 100)

run = True
while run:

  screen.fill("indigo")

  #draw health bar
  health_bar.hp = 50
  health_bar.draw(screen)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.flip()

pygame.quit()