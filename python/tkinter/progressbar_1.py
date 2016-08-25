import tkinter as tk
import tkinter.ttk as ttk
from tooltip_lib2 import *


def main():
    root = tk.Tk()
    # ft = ttk.Frame(root)
    # fb = ttk.Frame(root)
    tf = ttk.Frame(root)

    health = tk.DoubleVar()
    health.set(100)
    health_str = "Health: {} / {}".format(100, 100)
    energy = tk.DoubleVar()
    energy.set(100)
    energy_str = "Energy: {} / {}".format(100, 100)
    exp = tk.DoubleVar()
    exp.set(100)
    exp_str = "Exp: {} / {}".format(100, 100)
    stamina = tk.DoubleVar()
    stamina.set(100)
    stamina_str = "Stamina: {} / {}".format(100, 100)

    s = ttk.Style()
    s.theme_use('clam')
    s.configure("red.Horizontal.TProgressbar",
                foreground='red', background='red')
    s.configure("blue.Horizontal.TProgressbar",
                foreground='blue', background='blue')
    s.configure("green.Horizontal.TProgressbar",
                foreground='green', background='green')
    s.configure("yellow.Horizontal.TProgressbar",
                foreground='yellow', background='yellow')

    # ft.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
    # fb.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
    tf.grid(sticky="nsew")

    # pb_hd = ttk.Progressbar(ft, orient='horizontal', mode='determinate')
    # pb_hD = ttk.Progressbar(ft, orient='horizontal', mode='indeterminate')
    # pb_vd = ttk.Progressbar(fb, orient='vertical', mode='determinate')
    # pb_vD = ttk.Progressbar(fb, orient='vertical', mode='indeterminate')

    test = ttk.Progressbar(tf, style="red.Horizontal.TProgressbar",
                            orient='horizontal', mode='determinate',
                            maximum=100, variable=health)
    ToolTip(test, health_str)

    test2 = ttk.Progressbar(tf, style="blue.Horizontal.TProgressbar",
                            orient='horizontal', mode='determinate',
                            maximum=100, variable=energy)
    ToolTip(test2, energy_str)

    test3 = ttk.Progressbar(tf, style="green.Horizontal.TProgressbar",
                            orient='horizontal', mode='determinate',
                            maximum=100, variable=exp)
    ToolTip(test3, exp_str)

    test4 = ttk.Progressbar(tf, style="yellow.Horizontal.TProgressbar",
                            orient='horizontal', mode='determinate',
                            maximum=100, variable=stamina)
    ToolTip(test4, stamina_str)

    # pb_hd.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
    # pb_hD.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
    # pb_vd.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
    # pb_vD.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

    test.grid(row=0, column=0, sticky="nsew")
    test2.grid(row=1, column=0, sticky="nsew")
    test3.grid(row=2, column=0, sticky="nsew")
    test4.grid(row=3, column=0, sticky="nsew")

    # pb_hd.start(50)
    # pb_hD.start(50)
    # pb_vd.start(50)
    # pb_vD.start(50)

    # test.config(value=75)
    # test2.config(value=100)
    # test3.config(value=20)
    # test4.config(value=35)

    health.set(77)
    health_str = "Health: {} / {}".format(77, 100)
    ToolTip(test, health_str)

    energy.set(54.3)
    energy_str = "Energy: {} / {}".format(54.3, 100)
    ToolTip(test2, energy_str)

    exp.set(20)
    exp_str = "Exp: {} / {}".format(20, 100)
    ToolTip(test3, exp_str)

    stamina.set(35.5)
    stamina_str = "Stamina: {} / {}".format(35.5, 100)
    ToolTip(test4, stamina_str)

    root.mainloop()

if __name__ == '__main__':
    main()
