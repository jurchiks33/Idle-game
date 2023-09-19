import tkinter as tk

class SimpleWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Game Window")

        self.master.configure(bg="grey")

        width_in_pixel = (35 / 2.54) * 96
        height_in_pixel = (25 / 2.54) * 96

        size = "{}x{}".format(int(width_in_pixel), int(height_in_pixel))
        self.master.geometry(size)

        label = tk.Label(self.master, text="IDLE MASTER", font=("Arial", 24, "bold"), bg="grey", fg="black")
        label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    window = SimpleWindow(root)
    root.mainloop()