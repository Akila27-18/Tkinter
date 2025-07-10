
import tkinter as tk
import threading
import time

def simulate_download(label):
    for i in range(6):
        time.sleep(1)
        label.after(0, label.config, {'text': f"Downloading... {i*20}%"})
    label.after(0, label.config, {'text': "Download Complete!"})

def start_download(label):
    threading.Thread(target=simulate_download, args=(label,)).start()

root = tk.Tk()
root.title("Task 06 - File Download")
root.geometry("300x150")

status = tk.Label(root, text="Ready to Download")
status.pack(pady=10)

tk.Button(root, text="Download", command=lambda: start_download(status)).pack()

root.mainloop()
