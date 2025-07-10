
import tkinter as tk
import threading
import time

def long_task(label):
    label.config(text="Please wait...")
    time.sleep(5)
    label.config(text="Done!")

def start_thread(label):
    thread = threading.Thread(target=long_task, args=(label,))
    thread.start()

root = tk.Tk()
root.title("Task 02 - Wait Message")
root.geometry("300x150")

status_label = tk.Label(root, text="Click to Start")
status_label.pack(pady=10)

start_button = tk.Button(root, text="Start Task", command=lambda: start_thread(status_label))
start_button.pack()

root.mainloop()
