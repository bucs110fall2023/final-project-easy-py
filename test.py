import pygame
import json
from src.sample_controller import Controller
def test():
    test = Controller()
    test.save = "Save 1"
    test.state = "BATTLE"
    test.battle_gameloop()
test()