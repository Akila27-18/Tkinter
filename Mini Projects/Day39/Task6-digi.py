import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")  # Format: HH:MM:SS
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # Call this function again after 1 second

# GUI setup
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x150")
root.resizable(False, False)

clock_label = tk.Label(root, text="", font=("Arial", 40), fg="white", bg="black")
clock_label.pack(expand=True, fill="both")

update_time()  # Start the clock

root.mainloop()
