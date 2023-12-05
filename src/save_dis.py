import pygame

class SaveDis:

    def __init__(self, screen, width, height):
        """
        Accepts the pygame screen and its width and height as properties of the initialized object
        args : self, screen, width, height
        return: None
        """
        self.screen = screen
        self.height = height
        self.width = width

    def save_display(self):
        """
        Displays the save screen for the player to choose a save file
        args: Self
        return None
        """
        request = "Select a save file:"
        fst = "Save 1: press 1"
        scnd = "Save 2: press 2"
        trd = "Save 3 press 3"
        font = pygame.font.Font(None, int(self.width / 10))
        req_msg = font.render(request, True, "white") #(10, self.width / 10))
        fst_msg = font.render(fst, True, "white") #(10, self.width / 3))
        scnd_msg = font.render(scnd, True, "white") #(10, ( 2 * self.width) / 3))
        trd_msg = font.render(trd, True, "white") #(10, ( 3 * self.width) / 3))
        self.screen.blit(req_msg, (10, 0))
        self.screen.blit(fst_msg, (10, (self.width / 3) - (self.width / 10)))
        self.screen.blit(scnd_msg, (10, ((2 * self.width) / 3) - (self.width / 10)))
        self.screen.blit(trd_msg, (10, ((3 * self.width) / 3) - (self.width / 10)))
        pygame.display.flip()

def test():
    pygame.init()
    display = pygame.display.set_mode()
    width, height = pygame.display.get_window_size()
    test = SaveDis(display, width, height)
    while True:
        test.save_display()
test()