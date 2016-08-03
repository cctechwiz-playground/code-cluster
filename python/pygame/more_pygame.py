import pygame
import time
import math

# Constants
PI = math.pi
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
gameDisplay.fill(BLACK)
pygame.display.set_caption("Drawing")
clock = pygame.time.Clock()

# Map the display
px_array = pygame.PixelArray(gameDisplay)
px_array[10][20] = GREEN
# Where Color, Begin(x, y), End(x, y), w
pygame.draw.line(gameDisplay, BLUE, (100, 200), (300, 450), 5)
# Where, Color, (x, y, w, h)
pygame.draw.rect(gameDisplay, RED, (400, 400, 50, 25))
# Where, Color, Center(x, y), r
pygame.draw.circle(gameDisplay, WHITE, (150, 150), 75)

# Generate Hex points
def gen_hex(center_x, center_y, is_pointy, size):
    hexagon = list()
    # Change from True to False to render hex pointy or not
    if is_pointy:
        rot = 30
    else:
        rot = 0
    hex_size = size
    hex_center_x = center_x
    hex_center_y = center_y
    for i in range(1,7):
        angle_deg = 60 * i + rot
        angle_rad = PI / 180 * angle_deg
        point_x = hex_center_x + hex_size * math.cos(angle_rad)
        point_y = hex_center_y + hex_size * math.sin(angle_rad)
        point =(point_x, point_y)
        hexagon.append(point)
    return tuple(hexagon)

def next_hex(my_x, my_y, size, dir, is_pointy):
    hexagon = list()
    hex_size = size
    # Calc offsets
    width = size * 2
    horiz_diff = width * (3/4)
    height = math.sqrt(3)/2 * width
    vert_diff = height
    # Apply offsets
    if dir == "x+":
        hex_center_x = my_x
        hex_center_y = my_y - vert_diff
    elif dir == "x-":
        hex_center_x = my_x
        hex_center_y = my_y + vert_diff
    elif dir == "y+":
        hex_center_x = my_x + horiz_diff
        hex_center_y = my_y + (vert_diff * (1/2))
    elif dir == "y-":
        hex_center_x = my_x - horiz_diff
        hex_center_y = my_y - (vert_diff * (1/2))
    elif dir == "z+":
        hex_center_x = my_x + horiz_diff
        hex_center_y = my_y - (vert_diff * (1/2))
    elif dir == "z-":
        hex_center_x = my_x - horiz_diff
        hex_center_y = my_y + (vert_diff * (1/2))
    else:
        print("bad dir value")
        quit()

    if is_pointy:
        rot = 30
    else:
        rot = 0

    for i in range(1,7):
        angle_deg = 60 * i + rot
        angle_rad = PI / 180 * angle_deg
        point_x = hex_center_x + hex_size * math.cos(angle_rad)
        point_y = hex_center_y + hex_size * math.sin(angle_rad)
        point =(point_x, point_y)
        hexagon.append(point)
    return tuple(hexagon)

# Where, Color, ((coords), width)
x, y, s, p = 400, 300, 25, False
hex1 = gen_hex(x, y, p, s)
hex2 = next_hex(x, y, s, "x+", p)
hex3 = next_hex(x, y, s, "x-", p)
hex4 = next_hex(x, y, s, "y+", p)
hex5 = next_hex(x, y, s, "y-", p)
hex6 = next_hex(x, y, s, "z+", p)
hex7 = next_hex(x, y, s, "z-", p)
pygame.draw.polygon(gameDisplay, GREEN, hex1, 2)
pygame.draw.polygon(gameDisplay, GREEN, hex2, 2)
pygame.draw.polygon(gameDisplay, GREEN, hex3, 2)
pygame.draw.polygon(gameDisplay, GREEN, hex4, 2)
pygame.draw.polygon(gameDisplay, GREEN, hex5, 2)
pygame.draw.polygon(gameDisplay, GREEN, hex6, 2)
pygame.draw.polygon(gameDisplay, GREEN, hex7, 2)

while True:
    for event in pygame.event.get():
        # Clicked close button
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
    clock.tick(60)
