# https://www.youtube.com/watch?v=Fq74VE-JTWE&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq&index=11

import pygame
import time
import random

init_results = pygame.init()  # (success, fails)
clock = pygame.time.Clock()

WIDTH, HEIGHT = 800, 600
FPS = 10

WHITE = (255, 255, 255)  # (red, gree, blue [, alpha])
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 155, 00)
BLUE = (0, 0, 255)

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Slither')
font = pygame.font.SysFont(None, 25)  # (Face???, Size)
# update can take paremetes and update only those items, empty == whole display
# pygame.display.update()  # pygame.display.flip()

def snake(snake_body, size):
    for seg in snake_body:
        pygame.draw.rect(gameDisplay, BLACK, [seg[0], seg[1], size, size])

def display_message(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [WIDTH/2, HEIGHT/2])

def quit_game():
    pygame.quit()
    quit()

def game_loop():
    GAME_OVER = False
    s_size = 10
    a_size = 10
    align = 10
    apple_x = round(random.randrange(0, WIDTH-a_size)/align)*align
    apple_y = round(random.randrange(0, HEIGHT-a_size)/align)*align
    lead_x, lead_y = WIDTH/2, HEIGHT/2
    lead_xv, lead_yv = 0, 0
    snake_body = []
    snake_len = 1
    # Game loop
    # #########
    while True:
        # Game over screen
        # ################
        while GAME_OVER:
            gameDisplay.fill(WHITE)
            display_message("GAME OVER, press c to play again, or q to quit", RED)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game()
                    if event.key == pygame.K_c:
                        game_loop()
        # Event handling
        # ##############
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            # Register keys that are pressed this time around
            # Key pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_xv = -s_size
                    lead_yv = 0
                if event.key == pygame.K_RIGHT:
                    lead_xv = s_size
                    lead_yv = 0
                if event.key == pygame.K_UP:
                    lead_yv = -s_size
                    lead_xv = 0
                if event.key == pygame.K_DOWN:
                    lead_yv = s_size
                    lead_xv = 0

        # Logic handling
        # ##############
        lead_x += lead_xv
        lead_y += lead_yv
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_body.append(snake_head)

        # Hit boundary
        if (lead_x >= WIDTH or lead_x < 0 or lead_y >= HEIGHT or lead_y < 0):
            GAME_OVER = True
            continue

        # Maintain correct length
        if len(snake_body) > snake_len:
            del snake_body[0]

        # Hit self
        for seg in snake_body[:-1]:
            if seg == snake_head:
                GAME_OVER = True
                continue

        # Hit apple
        left_x_cross = ((lead_x >= apple_x) and
                    (lead_x < (apple_x + a_size)))
        right_x_cross = (((lead_x + s_size) > apple_x) and
                    ((lead_x + s_size) < (apple_x + a_size)))
        top_y_cross = ((lead_y >= apple_y) and
                    (lead_y < (apple_y + a_size)))
        bot_y_cross = (((lead_y + s_size) > apple_y) and
                    ((lead_y + s_size) < (apple_y + a_size)))
        if (left_x_cross or right_x_cross) and (top_y_cross or bot_y_cross):
            # New apple
            apple_x = round(random.randrange(0, WIDTH-a_size)/align)*align
            apple_y = round(random.randrange(0, HEIGHT-a_size)/align)*align
            # Grow snake
            snake_len += 1

        # Graphics rendering
        # ##################
        gameDisplay.fill(WHITE)  # fills the whole screen, can fill rect too
        # rect(display, color, [x, y, w, h])
        pygame.draw.rect(gameDisplay, RED, [apple_x, apple_y, a_size, a_size])
        snake(snake_body, s_size)

        pygame.display.update()
        clock.tick(FPS)  # FPS may change throughout the program

# Main
game_loop()
pygame.quit()  # Uninit all pygame components
quit()  # Exit out of python
