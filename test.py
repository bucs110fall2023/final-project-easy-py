import pygame
import json
from src.controller import Controller
def test():
    test = Controller()
    test.save = "Save 1"
    test.story_loop()
test()