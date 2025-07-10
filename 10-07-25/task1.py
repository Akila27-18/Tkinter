
import tkinter as tk
import threading
import time

def long_running_task():
    print("Long task started...")
    time.sleep(5)
    print("Long task finished.")

def start_task():
    thread = threading.Thread(target=long_running_task)
    thread.start()

root = tk.Tk()
root.title("Task 01 - Threaded Button")
root.geometry("300x150")

start_button = tk.Button(root, text="Start Long Task", command=start_task)
start_button.pack(pady=30)

root.mainloop()
