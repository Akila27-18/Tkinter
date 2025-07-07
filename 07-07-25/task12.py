import tkinter as tk

def log_event(event):
    if event.type == tk.EventType.KeyPress:
        log_text.insert(tk.END, f"Key Pressed: {event.keysym}\n")
    elif event.type == tk.EventType.ButtonPress:
        log_text.insert(tk.END, f"Mouse Click at ({event.x}, {event.y})\n")
    log_text.see(tk.END)  # Auto-scroll to latest entry

def clear_log():
    log_text.delete("1.0", tk.END)

# Main Window
root = tk.Tk()
root.title("Event Logger Tool")
root.geometry("500x400")
root.resizable(False, False)

# Text widget for logs
log_text = tk.Text(root, wrap=tk.WORD, width=58, height=20)
log_text.place(x=20, y=20)

# Scrollbar for text
scrollbar = tk.Scrollbar(root, command=log_text.yview)
scrollbar.place(x=460, y=20, height=320)
log_text.config(yscrollcommand=scrollbar.set)

# Clear button
clear_btn = tk.Button(root, text="Clear Log", bg="lightcoral", command=clear_log)
clear_btn.place(x=200, y=350)

# Bind events
root.bind("<Key>", log_event)
root.bind("<Button-1>", log_event)

root.mainloop()
