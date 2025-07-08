import tkinter as tk
from tkinter import messagebox

# Functions for logging control
def start_logging():
    root.bind("<Key>", log_key)
    root.bind("<Button-1>", log_click)
    log_message("Logging started...")

def stop_logging():
    root.unbind("<Key>")
    root.unbind("<Button-1>")
    log_message("Logging stopped.")

def clear_log():
    text_area.config(state='normal')
    text_area.delete(1.0, tk.END)
    text_area.config(state='disabled')

def log_message(msg):
    text_area.config(state='normal')
    text_area.insert(tk.END, msg + "\n")
    text_area.see(tk.END)
    text_area.config(state='disabled')

def log_key(event):
    log_message(f"Key Pressed: {event.keysym}")

def log_click(event):
    log_message(f"Mouse Click at ({event.x_root}, {event.y_root})")

# Main window
root = tk.Tk()
root.title("Event Logger Tool")
root.geometry("500x300")

# Toolbar
toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
toolbar.pack(side=tk.TOP, fill=tk.X)

tk.Button(toolbar, text="Clear Log", command=clear_log).pack(side=tk.LEFT, padx=4, pady=4)

# Menu
menu_bar = tk.Menu(root)
event_menu = tk.Menu(menu_bar, tearoff=0)
event_menu.add_command(label="Start Logging", command=start_logging)
event_menu.add_command(label="Stop Logging", command=stop_logging)
menu_bar.add_cascade(label="Events", menu=event_menu)
root.config(menu=menu_bar)

# Text area with scrollbar
log_frame = tk.Frame(root)
log_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

scrollbar = tk.Scrollbar(log_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_area = tk.Text(log_frame, yscrollcommand=scrollbar.set, state='disabled', wrap='word')
text_area.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=text_area.yview)

# Start app
root.mainloop()
