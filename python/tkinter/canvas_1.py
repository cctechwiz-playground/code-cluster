import tkinter as tk
import math

# Constants
PI = math.pi
WIDTH = 800
HEIGHT = 600


class hex:
    def __init__(self, coords, name):
        self.coords =coords
        self.name = name

# Generate Hex points
def gen_hex(center_x, center_y, is_pointy, size, name):
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
    return hex(tuple(hexagon), name)

def next_hex(my_x, my_y, size, dir, is_pointy, name):
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
    return hex(tuple(hexagon), name)
def get_idx_from_tags(tags):
    idx_str = ""
    for t in tags:
        if "idx:" in t:
            idx_str = t
    idx = int(idx_str.split(":")[1])
    return idx

def print_hex(event):
    global hexes
    global chars
    canvas = event.widget
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    item = canvas.find_closest(x, y)
    print("selected: ", item)
    tags = canvas.gettags(item)
    print("selected tags: ", tags)
    overlapped = canvas.find_overlapping(x, y, x+1, y+1)
    print("overlapped: ", overlapped)
    if "map" in tags:
        idx = get_idx_from_tags(tags)
        print("hexes[{}].name = {}".format(idx, hexes[idx].name))
    if "char" in tags:
        #idx2 = item[0] - len(hexes) - 1  # TODO: This is violent abuse
        idx = get_idx_from_tags(tags)
        print("chars[{}].name = {}".format(idx, chars[idx].name))

# Where, Color, ((coords), width)
x, y, s, p = 400, 300, 25, False
hexes = []
hexes.append(gen_hex(x, y, p, s, "hex1"))
hexes.append(next_hex(x, y, s, "x+", p, "hex2"))
hexes.append(next_hex(x, y, s, "x-", p, "hex3"))
hexes.append(next_hex(x, y, s, "y+", p, "hex4"))
hexes.append(next_hex(x, y, s, "y-", p, "hex5"))
hexes.append(next_hex(x, y, s, "z+", p, "hex6"))
hexes.append(next_hex(x, y, s, "z-", p, "hex7"))

c_x, c_y, c_s, c_p = 400, 300, 10, False
chars = []
chars.append(gen_hex(c_x, c_y, c_p, c_s, "Alpha"))
chars.append(next_hex(c_x-35, c_y, c_s, "x+", c_p, "Beta"))
chars.append(next_hex(c_x+35, c_y, c_s, "x-", c_p, "Gamma"))
chars.append(next_hex(c_x, c_y-35, c_s, "y+", c_p, "Delta"))
chars.append(next_hex(c_x, c_y+35, c_s, "y-", c_p, "Epsilon"))
chars.append(next_hex(c_x-35, c_y-35, c_s, "z+", c_p, "Zeta"))
chars.append(next_hex(c_x+35, c_y+35, c_s, "z-", c_p, "Eta"))

master = tk.Tk()

w = tk.Canvas(master, width=WIDTH, height=HEIGHT)
w.pack()

# w.create_line(0, 0, 200, 100)
# w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
# w.create_rectangle(50, 25, 150, 75, fill="blue")

w.bind("<Button-1>", print_hex)

h_idx = 0
for h in hexes:
    idx_tag = "idx:{}".format(h_idx)
    w.create_polygon(h.coords,
                    fill="red",
                    activefill="blue",
                    outline="black",
                    stipple="gray12",
                    activestipple="gray50",
                    offset=tk.NE,
                    tags=("map", h.name, idx_tag))
    h_idx += 1

c_idx = 0
for c in chars:
    idx_tag = "idx:{}".format(c_idx)
    w.create_polygon(c.coords,
                    fill="green",
                    activefill="black",
                    outline="white",
                    tags=("char", c.name, idx_tag))
    c_idx += 1

tk.mainloop()
