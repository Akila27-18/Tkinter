# task24_log_mouse_events.py
import tkinter as tk

def log(event):
    log_text.insert("end", f"Event: {event.type} at ({event.x}, {event.y})\n")
    log_text.see("end")

root = tk.Tk()
log_text = tk.Text(root, height=10)
log_text.pack()

frame = tk.Frame(root, width=200, height=150, bg="lightgray")
frame.pack(pady=10)
frame.bind("<Enter>", log)
frame.bind("<Leave>", log)
frame.bind("<Button-1>", log)
frame.bind("<Motion>", log)
root.mainloop()
