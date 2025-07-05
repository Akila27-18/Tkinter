import tkinter as tk

def log_event(event):
    if event.type == tk.EventType.KeyPress:
        log = f"Key Pressed: {event.keysym}"
    elif event.type == tk.EventType.ButtonPress:
        log = f"Mouse Click at ({event.x}, {event.y})"
    elif event.type == tk.EventType.Double:
        log = f"Mouse Double Click at ({event.x}, {event.y})"
    else:
        log = f"Event: {event.type}"
    
    log_area.insert(tk.END, log + "\n")
    log_area.see(tk.END)  # Scroll to latest

def clear_logs():
    log_area.delete("1.0", tk.END)

# === GUI Setup ===
root = tk.Tk()
root.title("Event Logger")
root.geometry("500x300")

# === Widgets ===
log_area = tk.Text(root, wrap="word", height=12, width=58)
log_area.grid(row=0, column=0, padx=(10,0), pady=10)

scrollbar = tk.Scrollbar(root, command=log_area.yview)
scrollbar.grid(row=0, column=1, sticky="ns", pady=10)
log_area.config(yscrollcommand=scrollbar.set)

clear_btn = tk.Button(root, text="Clear Logs", command=clear_logs, bg="red", fg="white")
clear_btn.grid(row=1, column=0, columnspan=2, pady=5)

# === Event Bindings ===
root.bind("<Key>", log_event)
root.bind("<Button-1>", log_event)
root.bind("<Double-Button-1>", log_event)

# === Focus so key events are captured ===
log_area.focus_set()

root.mainloop()
