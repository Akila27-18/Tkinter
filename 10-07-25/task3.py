
import tkinter as tk
import threading
import time

def background_task(callback):
    time.sleep(3)
    callback("Fetched Data!")

def start_thread(label):
    def update_text(result):
        label.config(text=result)

    def thread_target():
        background_task(lambda text: label.after(0, update_text, text))

    threading.Thread(target=thread_target).start()

root = tk.Tk()
root.title("Task 03 - after() Update")
root.geometry("300x150")

info_label = tk.Label(root, text="Waiting...")
info_label.pack(pady=10)

tk.Button(root, text="Fetch Data", command=lambda: start_thread(info_label)).pack()

root.mainloop()
