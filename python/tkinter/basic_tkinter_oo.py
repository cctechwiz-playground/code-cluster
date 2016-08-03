# tkinter in object oriented python
import tkinter as tk


# Constants
LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk): # Inherits from tk.Tk
    # Class Constructor
    def __init__(self, *args, **kwargs):
        # Initialize Tk
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        # fill-> fill given space, expand-> spill over to empty space
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # Create a dictionary to hold all frames (views)
        self.frames = { }
        # Add all pages to frames dictionary
        for Page in (StartPage, PageOne, PageTwo):
            frame = Page(container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        # display the passed frame
        self.show_frame(StartPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise() # Tk method to bring the frame to the front


class StartPage(tk.Frame): # Inherits from tk.Frame

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()
        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()
        button2 = tk.Button(self, text="Back to home",
                            command=lambda: controller.show_frame(StartPage))
        button2.pack()


# Start running tkinter app
app = SeaofBTCapp()
app.mainloop()
