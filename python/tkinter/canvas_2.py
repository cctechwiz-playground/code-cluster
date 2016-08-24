import tkinter as tk
import math

WIDTH = 800
HEIGHT = 600

rx = WIDTH / 2
ry = HEIGHT / 2
rw = 20
rwm = rw / 2
round_to = 10

selected_elem = None

def motion(event):
    global selected_elem
    canvas = event.widget
    x, y = event.x, event.y
    if selected_elem:
        canvas.coords(selected_elem, x - rwm, y - rwm, x + rwm, y + rwm)

def elem_click(event):
    global selected_elem
    canvas = event.widget
    x, y = event.x, event.y
    cx = canvas.canvasx(event.x)
    cy = canvas.canvasy(event.y)
    clicked_elem = canvas.find_closest(cx, cy)
    if selected_elem == clicked_elem:
        selected_elem = None
        canvas.itemconfig(clicked_elem, fill="blue", activefill="green")
        nx1 = int(math.ceil((x - rwm) / round_to)) * round_to
        ny1 = int(math.ceil((y - rwm) / round_to)) * round_to
        nx2 = int(math.ceil((x + rwm) / round_to)) * round_to
        ny2 = int(math.ceil((y + rwm) / round_to)) * round_to
        canvas.coords(clicked_elem, nx1, ny1, nx2, ny2)
    else:
        canvas.itemconfig(clicked_elem, fill="red", activefill="red")
        selected_elem = clicked_elem

master = tk.Tk()

canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT, bg="#595959")
canvas.pack()
canvas.tag_bind("elem", "<Button-1>", elem_click)
canvas.bind("<Motion>", motion)

elem1 = canvas.create_rectangle(rx, ry, rx + rw, ry + rw,
                                fill="blue", activefill="green",
                                tags="elem")

tk.mainloop()
