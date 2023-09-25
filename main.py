from PIL import Image, ImageTk
import tkinter as tk


class Enemy:
    def __init__(self, container, img_path, health):
        self.health = health
        self.max_health = health
    
    self.tree_image = ImageTk.PhotoImage(Image.open(img_path))
    self.tree_label = tk.Label(container, image=self.tree_image, bg="grey")
    self.tree_label.pack(side=tk.TOP, padx=10)

    self.health_label = tk.Label(container, text=str(self.health) + "HP", bg="grey", font=("Arial", 12, "Bold"))
    self.health_label.pack(side=tk.TOP, pady=5)

    self.health_bar_canvas = tk.Canvas(container, width=200, height=20, bg="grey")
    self.health_bar_canvas.pack(side=tk.TOP, pady=5)
    self.health_bar = self.health_bar_canvas.create_rectangle(0, 0, 200, 20, fill="red", outline="black")

    self.tree_label.bind("<ButtonPress-1>")

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

        title_canvas = tk.Canvas(self.master, bg="grey", bd=0, highlightthickness=0, height=10)
        title_canvas.pack(fill=tk.X, pady=(0, 20))
        title_canvas.create_line(0, 5, width_in_pixel, 5, fill="brown", width=3)

        names = ["sword", "fists", "bow", "fireball", "frostbolt"]

        frame_width = int((5 / 2.54) * 96)
        frame_height = int((2 / 2.54) * 96)

        outer_container = tk.Frame(self.master, bg="grey")
        outer_container.pack(side=tk.RIGHT, padx=5, pady= 5)
        self.tree_image = ImageTk.PhotoImage(Image.open("tree.jpg"))
        image_width = self.tree_image.width()
        tree_label = tk.Label(outer_container, image=self.tree_image, bg="grey")
        tree_label.pack(side=tk.TOP, padx=10)  

        self.health = 500

        self.health_label = tk.Label(outer_container, text=str(self.health) + "HP", bg="grey", font=("Arial", 12, "bold"))
        self.health_label.pack(side=tk.TOP, pady=5) 

        
        
        self.health_bar_canvas = tk.Canvas(outer_container, width=200, height=20, bg="grey")
        self.health_bar_canvas.pack(side=tk.TOP, pady=5)  
        self.health_bar = self.health_bar_canvas.create_rectangle(0, 0, 200, 20, fill="red", outline="black")

        
        tree_label.bind("<ButtonPress-1>", self.decrease_health)

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

        line_canvas = tk.Canvas(left_container, bg="grey", bd=0, highlightthickness=0, width=10, height=height_in_pixel)
        line_canvas.pack(side=tk.RIGHT, fill=tk.BOTH)
        line_canvas.create_line(5, 0, 5, height_in_pixel, fill="brown", width=3)

           
    def increase_value(self, value, label, name):
        current_value = int(value.get())
        new_value = current_value + 1
        value.set(str(new_value))
        label.config(text=name + ": " + str(new_value))
        self.decrease_health(new_value)  

    def decrease_health(self, value=1):
        if isinstance(value, tk.Event):  
            value = 1  
        if self.health > 0:
            self.health -= value  
            if self.health < 0:
                self.health = 0  
            self.health_label.config(text=str(self.health) + "HP")
            self.health_bar_canvas.coords(self.health_bar, 0, 0, 200 * (self.health / 500), 20)

if __name__ == "__main__":
    root = tk.Tk()
    window = SimpleWindow(root)
    root.mainloop()