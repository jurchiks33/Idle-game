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

        names = ["sword", "fists", "bow", "fireball", "frostbolt"]

        frame_width = int((5 / 2.54) * 96)
        frame_height = int((2 / 2.54) * 96)

        left_container = tk.Frame(self.master, bg="grey")
        left_container.pack(side=tk.LEFT, padx=5, pady=5)

        for name in names:
            frame = tk.Frame(left_container, bg="white", width=frame_width, height=frame_height)
            frame.pack_propagate(0)
            frame.pack(side=tk.TOP, pady=5)

            label = tk.Label(frame, text=name, bg="white", font=("Arial", 12, "bold"))
            label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

if __name__ == "__main__":
    root = tk.Tk()
    window = SimpleWindow(root)
    root.mainloop()