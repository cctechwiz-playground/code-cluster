import tkinter as tk
import pygame
import time
import random

# Constants
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Globals
high_score = 0


class DriversEd(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(DriversEd, self).__init__(*args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = GamePane(container, self)
        self.frames[GamePane] = frames

        self.show_frame(GamePane)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class GamePane(tk.Frame):
    def __init__(self, parent, app):
        super(GamePane, self).__init__(parent)
        # Setup pygame
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Drivers Ed")
        self.clock = pygame.time.Clock()

        # Load and display a sprite
        self.carImg = pygame.image.load("car.png")
        self.car_width = 30 # define this from the image loaded

        # Run the game
        self.game_loop()
        pygame.quit()
        quit()

    def text_objects(self, text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def message_display(self, text):
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surface, text_rect = self.text_objects(text, large_text, RED)
        text_rect.center = ((WIDTH / 2), (HEIGHT / 2))
        self.gameDisplay.blit(text_surface, text_rect)
        pygame.display.update()
        # Show the message for 2 seconds and restart the game
        time.sleep(2)
        self.game_loop()

    def things_dodged(self, count):
        global high_score
        high_score = max(high_score, count)
        font = pygame.font.SysFont(None, 25)
        text = font.render("Dodged: {} - High Score: {}".format(count, high_score), True, GREEN)
        self.gameDisplay.blit(text, (0,0))

    def things(self, x, y, w, h, color):
        pygame.draw.rect(self.gameDisplay, color, [x, y, w, h])

    def car(self, x, y):
        self.gameDisplay.blit(self.carImg, (x, y))

    def crash(self):
        self.message_display("You Crashed!")

    def game_loop(self):
        # Initial position of car sprite relative to top left corner
        car_x = (WIDTH * 0.45)
        car_y = (HEIGHT * 0.8)
        car_move = 0

        thing_x = random.randrange(0, WIDTH)
        thing_y = -600
        thing_v = 4
        thing_w = 100
        thing_h = 100

        dodged = 0

        # Game Loop
        game_exit = False
        while not game_exit:
            for event in pygame.event.get():
                # Clicked close button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Any key is pressed
                # TODO: Do events queue up?
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        car_move = -5
                    elif event.key == pygame.K_RIGHT:
                        car_move = 5

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        car_move = 0

            self.gameDisplay.fill(WHITE)

            self.things(thing_x, thing_y, thing_w, thing_h, BLUE)
            thing_y += thing_v

            car_x += car_move
            self.car(car_x, car_y)
            self.things_dodged(dodged) # Draw this last so it doesn't get covered

            if car_x > (WIDTH - self.car_width) or car_x < 0:
                self.crash()

            if thing_y > HEIGHT:
                thing_y = 0 - thing_h
                thing_x = random.randrange(0, WIDTH)
                dodged += 1
                thing_v += .5 # Too hard!
                thing_w += (dodged * 1.2) # Will take whole screen eventually

            if car_y < (thing_y + thing_h):
                # Have y cross-over
                if ((car_x > thing_x) and
                    (car_x < (thing_x + thing_w)) or
                    ((car_x + self.car_width) > thing_x) and
                    ((car_x + self.car_width) < (thing_x + thing_w))):
                    # Have x cross-over
                    self.crash()


            pygame.display.update() # or .flip()
            self.clock.tick(60) # fps - aka run through the loop in 60 fps


game = DriversEd()
game.mainloop()
