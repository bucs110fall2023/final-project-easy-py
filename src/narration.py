import pygame
import json

class ScrollingText:

    def __init__(self, screen, file, length, width):
        self.screen = screen
        self.file = file
        self.length = length
        self.width = width

    def scroll(self):
        with open(self.file, "r") as text:
            for line in text.readlines():
                story_lines = []
                story_lines.append(line)
