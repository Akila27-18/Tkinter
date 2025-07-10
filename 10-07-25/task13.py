import tkinter as tk
import threading
import time

def loading_animation(label):
    for i in range(10):
        time.sleep(0.5)
        dots = '.' * ((i % 3) + 1)
        try:
            label.after(0, lambda dots=dots: label.config(text=f"Loading{dots}"))
        except RuntimeError:
            break  # Mainloop has exited

def start_loading(label):
    threading.Thread(target=loading_animation, args=(label,), daemon=True).start()

root = tk.Tk()
root.title("Task 13 - Loading Animation")
root.geometry("300x150")

status_label = tk.Label(root, text="Ready", font=("Arial", 16))
status_label.pack(pady=20)

tk.Button(root, text="Start Loading", command=lambda: start_loading(status_label)).pack()

root.mainloop()
