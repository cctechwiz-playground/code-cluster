from tkinter import *
from tooltip_lib import *

master = Tk()

button = Button(master, text="Hover for ToolTip")
createToolTip(button, "Happy, Happy, Happy")
button.pack()

master.mainloop()
