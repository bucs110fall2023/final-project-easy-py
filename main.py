import pygame
from src.controller import Controller
#import your controller

def main():
    #Create an instance on your controller object
    #Call your mainloop
    merants_venture = Controller()
    merants_venture.main_loop()
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
