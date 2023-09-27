from PIL import Image, ImageTk
import tkinter as tk


class Enemy:
    def __init__(self, container, img_path, health, window_instance):
        self.container = container
        self.health = health
        self.max_health = health
        self.window_instance = window_instance

        width_in_pixel = int((2.5 / 2.54) * 96)
        height_in_pixel = int((2.5 / 2.54) * 96)

        img = Image.open(img_path)
        img = img.resize((width_in_pixel, height_in_pixel))
        self.tree_image = ImageTk.PhotoImage(img)
    
        self.tree_label = tk.Label(container, image=self.tree_image, bg="grey")
        self.tree_label.pack(side=tk.TOP, padx=10)
        
        self.health_label = tk.Label(container, text=str(self.health) + "HP", bg="grey", font=("Arial", 12, "bold"))
        self.health_label.pack(side=tk.TOP, pady=5)
        
        self.health_bar_canvas = tk.Canvas(container, width=width_in_pixel, height=20, bg="grey")
        self.health_bar_canvas.pack(side=tk.TOP, pady=5)
        self.health_bar = self.health_bar_canvas.create_rectangle(0, 0, 200, 20, fill="red", outline="black")
        
        self.tree_label.bind("<ButtonPress-1>", self.select_enemy)
        self.health_label.bind("<ButtonPress-1>", self.select_enemy)
        self.health_bar_canvas.bind("<ButtonPress-1>"), self.select_enemy

        self.isSelected = False
        self.container.bind("<ButtonPress-1>", self.select_enemy)

        self.container.bind("<Enter>", lambda e: self.container.config(cursor='hand2'))
        self.container.bind("<Leave>", lambda e: self.container.config(cursor=''))

    
    def select_enemy(self, event=None):
        self.tree_label.configure(bg="green")
        self.health_label.configure(bg="green")
        self.health_bar_canvas.configure(bg="green")
        
        for enemy in self.window_instance.enemies:
            enemy.unselect_enemy()
        self.isSelected = True
        self.container.configure(bg="green")
    
    def unselect_enemy(self):
        self.tree_label.configure(bg="grey")
        self.health_label.configure(bg="grey")
        self.health_bar_canvas.configure(bg="grey")
        
        self.isSelected = False
        self.container.configure(bg="grey")

    def decrease_health(self, event=None, value=1):
        self.select_enemy() 
        if self.health > 0:
            self.health -= value
            if self.health <= 0:
                self.defeat_enemy(value)
                self.health = 0
            self.health_label.config(text=str(self.health) + "HP")
            
            canvas_width = self.health_bar_canvas.winfo_width()
            new_width = canvas_width * (self.health / self.max_health)

            self.health_bar_canvas.coords(self.health_bar, 0, 0, new_width, 20)

            damage_label = tk.Label(self.container, text="-"+str(value), fg="red", bg="grey", font=("Arial", 12, "bold"))

            x = self.container.winfo_width() // 2
            y = self.container.winfo_height() // 2 - 10

            damage_label.place(x=x, y=y, anchor=tk.CENTER)
            self.container.after(1000, damage_label.destroy)

    def defeat_enemy(self, value):
        self.window_instance.increase_skill("sword", self.max_health)

    def reset_health(self):
        self.health = self.max_health
        self.health_label.config(text=str(self.health) + "HP")
        self.health_bar_canvas.coords(self.health_bar, 0, 0, 200, 20)

class SimpleWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Game Window")
        self.master.configure(bg="grey")
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_enemies)
        self.reset_button.pack(pady=20)

        names = ["sword", "fists", "bow", "fireball", "frostbolt"]
        self.skills = {name: tk.StringVar(value="1") for name in names}

        width_in_pixel = (35 / 2.54) * 96
        height_in_pixel = (25 / 2.54) * 96

        size = "{}x{}".format(int(width_in_pixel), int(height_in_pixel))
        self.master.geometry(size)

        label_title = tk.Label(self.master, text="IDLE MASTER", font=("Arial", 24, "bold"), bg="grey", fg="black")
        label_title.pack(pady=20)

        title_canvas = tk.Canvas(self.master, bg="grey", bd=0, highlightthickness=0, height=10)
        title_canvas.pack(fill=tk.X, pady=(0, 20))
        title_canvas.create_line(0, 5, width_in_pixel, 5, fill="brown", width=3)

        

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

        line_canvas = tk.Canvas(left_container, bg="grey", bd=0, highlightthickness=0, width=10, height=height_in_pixel)
        line_canvas.pack(side=tk.RIGHT, fill=tk.BOTH)
        line_canvas.create_line(5, 0, 5, height_in_pixel, fill="brown", width=3)

        self.enemies = []
        enemy_container = tk.Frame(self.master, bg="grey")
        enemy_container.pack(side=tk.RIGHT, padx=5, pady=5)

        self.column1 = tk.Frame(enemy_container, bg="grey")
        self.column1.pack(side=tk.LEFT, padx=5, pady=5)

        self.column2 = tk.Frame(enemy_container, bg="grey")
        self.column2.pack(side=tk.RIGHT, padx=5, pady=5)

        self.column3 = tk.Frame(enemy_container, bg="grey")
        self.column3.pack(side=tk.RIGHT, padx=5, pady=5)

        self.add_enemy(enemy_container, "tree.jpg", 500)
        self.add_enemy(enemy_container, "enemy2.jpg", 7000)
        self.add_enemy(enemy_container, "enemy3.jpg", 25000)
        self.add_enemy(enemy_container, "enemy4.jpg", 40000)
        self.add_enemy(enemy_container, "enemy5.jpg", 75000)
        self.add_enemy(enemy_container, "enemy6.jpg", 150000)
        self.add_enemy(enemy_container, "enemy7.jpg", 275000)
        self.add_enemy(enemy_container, "enemy8.jpg", 350000)
        self.add_enemy(enemy_container, "enemy9.jpg", 440000)
        self.add_enemy(enemy_container, "enemy10.jpg", 550000)

    def add_enemy(self, container, img_path, health):
        num_enemies_col1 = len(self.column1.winfo_children())
        num_enemies_col2 = len(self.column2.winfo_children())
        num_enemies_col3 = len(self.column3.winfo_children())
       
        min_enemies = min(num_enemies_col1, num_enemies_col2, num_enemies_col3)

        if num_enemies_col1 <= num_enemies_col2 and num_enemies_col1 <= num_enemies_col3:
            container = self.column1
        elif num_enemies_col2 <= num_enemies_col1 and num_enemies_col2 <= num_enemies_col3:
            container = self.column2
        else:
            container = self.column3
    
        enemy_frame = tk.Frame(container, bg="grey")
        enemy_frame.pack(side=tk.TOP, pady=5)

        enemy = Enemy(enemy_frame, img_path, health, self)  
        self.enemies.append(enemy)
          
    def increase_value(self, value, label, name):
        current_value = int(self.skills[name].get())
        new_value = current_value + 1
        value.set(str(new_value))
        label.config(text=name + ": " + str(new_value))
        for enemy in self.enemies:
            if enemy.isSelected:  # Only affect the selected enemy
                enemy.decrease_health(value=new_value)
                break

    def increase_skill(self, name, max_health):
        increase_by = round(0.005 * max_health)
        current_value = int(self.skills[name].get())
        new_value = current_value + increase_by
        self.skills[name].set(str(new_value))  

    def reset_enemies(self):
        for enemy in self.enemies:
            enemy.reset_health()

if __name__ == "__main__":
    root = tk.Tk()
    window = SimpleWindow(root)
    root.mainloop()