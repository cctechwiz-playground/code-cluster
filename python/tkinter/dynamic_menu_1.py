from tkinter import *

counter = 0

def update():
    global counter
    counter = counter + 1
    menu.entryconfig(0, label=str(counter))

def hello():
    print("hello!")

root = Tk()
menubar = Menu(root)

menu = Menu(menubar, tearoff=0, postcommand=update)
menu.add_command(label=str(counter), )
menu.add_checkbutton(label="checkme")
menu.add_radiobutton(label="radiome1")
menu.add_radiobutton(label="radiome2")
menu.add_separator()
menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Test", menu=menu)

root.config(menu=menubar)

# create a popup menu
menu2 = Menu(root, tearoff=0)
menu2.add_command(label="Undo", command=hello)
menu2.add_command(label="Redo", command=hello)

# create a canvas
frame = Frame(root, width=512, height=512)
frame.pack()

def popup(event):
    menu2.post(event.x_root, event.y_root)

# attach popup to canvas
frame.bind("<Button-3>", popup)

root.mainloop()
