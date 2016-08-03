import pygame
init_results = pygame.init()  # (success, fails)
clock = pygame.time.Clock()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)  # (red, gree, blue [, alpha])
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 00)
BLUE = (0, 0, 255)

GAME_EXIT = False
lead_x, lead_y = 300, 300
lead_xv, lead_yv = 0, 0

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Slither')
# update can take paremetes and update only those items, empty == whole display
# pygame.display.update()  # pygame.display.flip()

l, r, u, d = False, False, False, False

# Game loop
while not GAME_EXIT:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_EXIT = True
        # Register keys that are pressed this time around
        # Key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: l = True
            if event.key == pygame.K_RIGHT: r = True
            if event.key == pygame.K_UP: u = True
            if event.key == pygame.K_DOWN: d = True
        # Key released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: l = False
            if event.key == pygame.K_RIGHT: r = False
            if event.key == pygame.K_UP: u = False
            if event.key == pygame.K_DOWN: d = False

    # Handle all keys that are currently pressed, allows for negations
    # Left and Right
    if l == False and r == False: lead_xv = 0
    if l == True and r == True: lead_xv = 0
    if l == True and r == False: lead_xv = -10
    if l == False and r == True: lead_xv = 10
    # Up and Down
    if u == False and d == False: lead_yv = 0
    if u == True and d == True: lead_yv = 0
    if u == True and d == False: lead_yv = -10
    if u == False and d == True: lead_yv = 10

    gameDisplay.fill(WHITE)  # fills the whole screen, can fill rect too
    # rect(display, color, [x, y, w, h])
    lead_x += lead_xv
    lead_y += lead_yv
    pygame.draw.rect(gameDisplay, BLACK, [lead_x, lead_y, 10, 10])

    pygame.display.update()
    clock.tick(30)  # FPS may change throughout the program

pygame.quit()  # Uninit all pygame components
quit()  # Exit out of python
