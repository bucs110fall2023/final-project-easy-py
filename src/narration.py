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

    def compile(self):
        """
        Compiles the text to be displayed on screen
        args: self
        return: None
        """
        with open(self.file, "r") as text:
            self.story_line = text.read()
            self.font = pygame.font.Font(None, int(self.height / 20))
            self.y_pos = self.height
    
    
    def scroll(self): # revisit, currently a bust
        """
        Scroll a line of text on the screen
        args: self
        return: boolean
        """
        if self.y_pos >= 0:    
            scrolling_line = self.story_line
            msg = self.font.render(scrolling_line, True, "white")
            self.screen.blit(msg, (10, self.y_pos))
            self.y_pos -= 1
            return True

    def refresh(self):
        """
        Refreshes the screen
        args: self
        return: None
        """
        pygame.display.flip()
        self.screen.fill("black")
