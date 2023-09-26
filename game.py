import tkinter as tk

class SimpleWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Game Window")

        width_in_pixel = (35 / 2.54) * 96
        height_in_pixel = (25 / 2.54) * 96

        size = "{}x{}".format(int(width_in_pixel), int(height_in_pixel))
        self.master.geometry(size)

if __name__ == "__main__":
    root = tk.Tk()
    window = SimpleWindow(root)
    root.mainloop()