import pygame

class ScrollingText:

    def __init__(self, screen, file, width, height):
        """
        Accepts the pygame screen and its width and height as properties of the initialized object as well as a file address
        args : self, screen, file, width, height
        return: None
        """        
        self.screen = screen
        self.file = file
        self.height = height
        self.width = width

    def scroll(self): # revisit, currently a bust
        with open(self.file, "r") as text:
            story_lines = []
            for line in text.readlines():
                story_lines.append(line)
            font = pygame.font.Font(None, int(self.height / 20))
            y_pos = self.height
            while True:
                y_pos += 50    
                for scrolling_line in story_lines:
                    msg = font.render(scrolling_line, True, "white")
                    self.screen.blit(msg, (10, y_pos))
                    pygame.display.flip()
                    y_pos -= 1
                    self.screen.fill("black")

def test():
    pygame.init()
    display = pygame.display.set_mode()
    width, height = pygame.display.get_window_size()
    test = ScrollingText(display, "../assets/story_beginning.txt", width, height)
    test.scroll()
test()

