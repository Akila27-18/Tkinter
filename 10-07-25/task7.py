
import tkinter as tk
import threading
import time

cancel_flag = False

def long_task(label):
    global cancel_flag
    cancel_flag = False
    for i in range(10):
        if cancel_flag:
            label.after(0, label.config, {'text': "Task Canceled!"})
            return
        time.sleep(1)
        label.after(0, label.config, {'text': f"Running... {i+1}"})
    label.after(0, label.config, {'text': "Task Completed!"})

def start_task(label):
    threading.Thread(target=long_task, args=(label,)).start()

def stop_task():
    global cancel_flag
    cancel_flag = True

root = tk.Tk()
root.title("Task 07 - Cancelable Task")
root.geometry("300x150")

status = tk.Label(root, text="Idle")
status.pack(pady=10)

tk.Button(root, text="Start", command=lambda: start_task(status)).pack()
tk.Button(root, text="Stop", command=stop_task).pack()

root.mainloop()
