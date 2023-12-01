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
            story_lines = []
            for line in text.readlines():
                story_lines.append(line)
            font = pygame.font.Font(None, int(self.width / 20))
            y_pos = self.width
            while True:    
                for scrolling_line in story_lines:
                    msg = font.render(scrolling_line, True, "white")
                    self.screen.blit(msg, (10, y_pos))
                    pygame.display.flip()
                    y_pos -= 1
                    self.screen.fill((0, 0, 0))

def test():
    pygame.init()
    display = pygame.display.set_mode()
    length, width = pygame.display.get_window_size()
    test = ScrollingText(display, "story_beginning.txt", length, width)
    test.scroll()
test()

