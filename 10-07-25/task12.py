import tkinter as tk
import threading
import time

def log_messages(text_widget):
    for i in range(5):
        time.sleep(1)
        try:
            text_widget.after(0, lambda i=i: text_widget.insert("end", f"Log {i+1}\n"))
        except RuntimeError:
            break  # Tkinter has likely been closed

def start_logging(text_widget):
    threading.Thread(target=log_messages, args=(text_widget,), daemon=True).start()

root = tk.Tk()
root.title("Task 12 - Log Messages")
root.geometry("300x200")

log_box = tk.Text(root, height=8, width=30)
log_box.pack(pady=10)

tk.Button(root, text="Start Logging", command=lambda: start_logging(log_box)).pack()

root.mainloop()
