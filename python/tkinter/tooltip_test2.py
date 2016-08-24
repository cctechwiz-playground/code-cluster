from tkinter import *
from tooltip_lib2 import *

master = Tk()

b = Button(master, text="Hello", command=master.destroy)
ListboxToolTip(b, ["Hello", "world"])

b2 = Button(master, text="Hello Again", command=master.destroy)
ToolTip(b2, "Hovering...")

b.pack()
b2.pack()

master.mainloop()
