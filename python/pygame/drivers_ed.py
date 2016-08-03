import pygame
import time
import random
import os

# Constants
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
BRIGHT_RED = (255, 0, 0)
BRIGHT_GREEN = (0, 255, 0)
BRIGHT_BLUE = (0, 0, 255)

# Globals
high_score = 0
pause = False

# Setup pygame
# pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

# Apperently not in the correct wav format for pygame to read
# crash_path = os.path.join(os.getcwd(), "crash.wav")
# background_path = os.path.join(os.getcwd(), "bass_loop.wav")
# crash_sound = pygame.mixer.Sound(crash_path)
# background_music = pygame.mixer.music.load(background_path)

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drivers Ed")
carImg = pygame.image.load("car.png")

# pygame.display.set_icon(carImg)
clock = pygame.time.Clock()

def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surface, text_rect = text_objects(text, large_text, RED)
    text_rect.center = ((WIDTH / 2), (HEIGHT / 2))
    gameDisplay.blit(text_surface, text_rect)
    pygame.display.update()

def things_dodged(count):
    global high_score
    high_score = max(high_score, count)
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: {} - High Score: {}".format(count, high_score), True, GREEN)
    gameDisplay.blit(text, (0,0))

def things(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, w, h])

# Load and display a sprite
car_width = 30 # define this from the image loaded
def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def button(msg, x, y, w, h, active_color, inactive_color, action):
    mouse = pygame.mouse.get_pos() # (x, y)
    mouse_x = mouse[0]
    mouse_y = mouse[1]

    click = pygame.mouse.get_pressed() # (left, middle, right)
    left_click = click[0]

    center_x = x + (w / 2)
    center_y = y + (h / 2)
    center = (center_x, center_y)
    coords = (x, y, w, h)

    if ((x < mouse_x < (x + w)) and
        (y < mouse_y < (y + h))):
        pygame.draw.rect(gameDisplay, active_color, coords)
        if left_click:
            action()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, coords)

    small_text = pygame.font.Font('freesansbold.ttf', 20)
    text_surface, text_rect = text_objects(msg, small_text, BLACK)
    text_rect.center = center
    gameDisplay.blit(text_surface, text_rect)

def crash():
    # pygame.mixer.music.stop()
    # pygame.mixer.Sound.play(crash_sound)

    message_display("You Crashed!")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()

        w, h = 100, 50

        play_btn_x, play_btn_y = 150, 450
        button("Retry", play_btn_x, play_btn_y, w, h,
            BRIGHT_GREEN, GREEN, game_loop)

        quit_btn_x, quit_btn_y = 550, 450
        button("Quit", quit_btn_x, quit_btn_y, w, h,
            BRIGHT_RED, RED, game_exit)

        pygame.display.update()
        clock.tick(15)

def game_exit():
    pygame.quit()
    quit()

def unpause():
    global pause
    # pygame.mixer.music.unpause()
    pause = False

def game_pause():
    # pygame.mixer.music.pause()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()

        gameDisplay.fill(WHITE)
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surface, text_rect = text_objects("Paused", large_text, BLACK)
        text_rect.center = ((WIDTH / 2), (HEIGHT / 2))
        gameDisplay.blit(text_surface, text_rect)

        w, h = 100, 50

        play_btn_x, play_btn_y = 150, 450
        button("Continue", play_btn_x, play_btn_y, w, h,
            BRIGHT_GREEN, GREEN, unpause)

        quit_btn_x, quit_btn_y = 550, 450
        button("Quit", quit_btn_x, quit_btn_y, w, h,
            BRIGHT_RED, RED, game_exit)

        pygame.display.update()
        clock.tick(15)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()

        gameDisplay.fill(WHITE)
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surface, text_rect = text_objects("Drivers Ed", large_text, BLACK)
        text_rect.center = ((WIDTH / 2), (HEIGHT / 2))
        gameDisplay.blit(text_surface, text_rect)

        w, h = 100, 50

        play_btn_x, play_btn_y = 150, 450
        button("Drive", play_btn_x, play_btn_y, w, h,
            BRIGHT_GREEN, GREEN, game_loop)

        quit_btn_x, quit_btn_y = 550, 450
        button("Quit", quit_btn_x, quit_btn_y, w, h,
            BRIGHT_RED, RED, game_exit)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    # pygame.mixer.music.play(-1)  # -1 == loop music forever
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
    exit = False
    while not exit:
        for event in pygame.event.get():
            # Clicked close button
            if event.type == pygame.QUIT:
                game_exit()

            # Any key is pressed
            # TODO: Do events queue up?
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_move = -5
                if event.key == pygame.K_RIGHT:
                    car_move = 5
                if event.key == pygame.K_p:
                    pause = True
                    game_pause()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car_move = 0

        gameDisplay.fill(WHITE)

        things(thing_x, thing_y, thing_w, thing_h, BLUE)
        thing_y += thing_v

        car_x += car_move
        car(car_x, car_y)
        things_dodged(dodged) # Draw this last so it doesn't get covered

        if car_x > (WIDTH - car_width) or car_x < 0:
            crash()

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
                ((car_x + car_width) > thing_x) and
                ((car_x + car_width) < (thing_x + thing_w))):
                # Have x cross-over
                crash()


        pygame.display.update() # or .flip()
        clock.tick(60) # fps - aka run through the loop in 60 fps

# Run the game
game_intro()
game_exit()
