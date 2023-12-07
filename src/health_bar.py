import pygame
class HealthBar:
    def __init__(self, x, y, w, h, max_hp):
        """
        holds the x and y coordinates and the width and height of the healthbar]
        args: self, x, y, w, h, max_hp
        return: None
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
        return: None
        """
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))
