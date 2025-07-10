
import tkinter as tk
import threading
import time

def animate(label):
    colors = ["red", "green", "blue", "orange"]
    for color in colors:
        time.sleep(0.5)
        label.after(0, label.config, {'fg': color})

def start_animation(label):
    threading.Thread(target=animate, args=(label,)).start()

root = tk.Tk()
root.title("Task 10 - Label Animation")
root.geometry("300x150")

anim_label = tk.Label(root, text="Color Changing Text", font=("Arial", 14))
anim_label.pack(pady=10)

tk.Button(root, text="Animate", command=lambda: start_animation(anim_label)).pack()

root.mainloop()
