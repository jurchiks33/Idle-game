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

        label_title = tk.Label(self.master, text="IDLE MASTER", font=("Arial", 24, "bold"), bg="grey", fg="black")
        label_title.pack(pady=20)

        names = ["sword", "fists", "bow", "fireball", "frostbolt"]

        frame_width = int((5 / 2.54) * 96)
        frame_height = int((2 / 2.54) * 96)

        left_container = tk.Frame(self.master, bg="grey")
        left_container.pack(side=tk.LEFT, padx=5, pady=5)

        for name in names:
            value = tk.StringVar()
            value.set("1")

            frame = tk.Frame(left_container, bg="white", width=frame_width, height=frame_height)
            frame.pack_propagate(0)
            frame.pack(side=tk.TOP, pady=5)

            label = tk.Label(frame, text=name + ": 1", bg="white", font=("Arial", 12, "bold"), takefocus=0)
            label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            frame.bind("<Enter>", lambda e, f=frame, l=label: (f.configure(bg="lightblue"), l.configure(bg="lightblue")), add='+')
            frame.bind("<Leave>", lambda e, f=frame, l=label: (f.configure(bg="white"), l.configure(bg="white")), add='+')
            frame.bind("<ButtonPress-1>", lambda event, v=value, lbl=label, nm=name: self.increase_value(v, lbl, nm))
            label.bind("<ButtonPress-1>", lambda event, v=value, lbl=label, nm=name: self.increase_value(v, lbl, nm))

           
    def increase_value(self, value, label, name):
        current_value = int(value.get())
        new_value = str(current_value + 1)
        value.set(new_value)
        label.config(text=name + ": " + new_value)

if __name__ == "__main__":
    root = tk.Tk()
    window = SimpleWindow(root)
    root.mainloop()