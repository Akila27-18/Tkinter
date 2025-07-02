import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)  # Call this function again after 1 second

# --- GUI Setup ---
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x150")
root.resizable(False, False)  # Disable resizing

# Time display label
time_label = tk.Label(root, font=("Helvetica", 40), fg="blue")
time_label.place(relx=0.5, rely=0.5, anchor="center")

# Start the clock
update_time()

root.mainloop()
