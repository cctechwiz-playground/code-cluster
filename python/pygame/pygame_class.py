import pygame
from pygame.locals import *
from pygame import Color


class Game():
    """ Lets try to get this going by simple steps
    One by one. First step, lets figure how to make a class
    that can do the display stuff. Lord have mercy on my soul"""

    def __init__(self, wi=256, hi=224, multii=3):
        """Initialization"""
        pygame.init()
        self.width      = wi*multii
        self.height     = hi*multii
        self.spritesize = 16*multii
        self.clock      = pygame.time.Clock()
        self.fps        = self.clock.get_fps()
        self.screen     = pygame.display.set_mode((self.width, self.height))
        self.runGame = True # I've moved the runGame decleration

    def mainLoop(self):
        """Loop through the main game routines
        1. Drawing  2. Input handling  3. Updating
        Then loop through it until user quits"""
        while self.runGame:
            self.clock.tick(12)
            self.draw()
            self.events()

    def events(self):
        """Time to handle some events"""
        events = pygame.event.get()
        for e in events:
            print(e)
            if ((e.type == pygame.QUIT) or
            (e.type == KEYDOWN and e.key == K_ESCAPE)):
                self.runGame = False

    def draw(self):
        """Draw and update the main screen"""
        self.screen.fill(Color('red'))
        self.fps = self.clock.get_fps() # I reupdate the FPS counter
        pygame.display.set_caption('Grid2. FPS: '+str(self.fps))
        pygame.display.update()


game = Game()
game.mainLoop()
