
import tkinter as tk
import threading
import time

root = tk.Tk()
root.title("Task 14 - Lambda with Delay")
root.geometry("300x150")

status_label = tk.Label(root, text="Waiting...")
status_label.pack(pady=10)

tk.Button(root, text="Run Delay", command=lambda: threading.Thread(
    target=lambda: [time.sleep(2), status_label.after(0, status_label.config, {'text': "Updated!"})]
).start()).pack()

root.mainloop()
