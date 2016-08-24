import tkinter as tk
import tkinter.ttk as ttk


def main():
    root = tk.Tk()
    ft = ttk.Frame()
    fb = ttk.Frame()
    tf = ttk.Frame()

    ft.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
    fb.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
    tf.pack(expand=True, fill=tk.BOTH, side=tk.TOP)

    pb_hd = ttk.Progressbar(ft, orient='horizontal', mode='determinate')
    pb_hD = ttk.Progressbar(ft, orient='horizontal', mode='indeterminate')
    pb_vd = ttk.Progressbar(fb, orient='vertical', mode='determinate')
    pb_vD = ttk.Progressbar(fb, orient='vertical', mode='indeterminate')

    test = ttk.Progressbar(tf, orient='horizontal', mode='determinate',
                            maximum=100, value=50)

    pb_hd.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
    pb_hD.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
    pb_vd.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
    pb_vD.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
    test.pack(expand=True, fill=tk.BOTH, side=tk.TOP)

    pb_hd.start(50)
    pb_hD.start(50)
    pb_vd.start(50)
    pb_vD.start(50)

    test.config(value=75)

    root.mainloop()

if __name__ == '__main__':
    main()
