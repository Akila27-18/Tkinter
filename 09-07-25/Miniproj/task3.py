import tkinter as tk

def on_key_press(event):
    key = event.keysym

    # Exit on Escape
    if key == 'Escape':
        root.destroy()
        return

    # Show current key
    current_key_label.config(text=f"Key Pressed: {key}")

    # Log key (exclude modifier keys for cleaner log)
    if len(key) == 1 or key.isalnum() or key in ['space', 'Return', 'BackSpace', 'Tab']:
        log_text.insert(tk.END, f"{key}\n")
        log_text.see(tk.END)

# Setup main window
root = tk.Tk()
root.title("Live Key Press Tracker")
root.geometry("400x300")
root.configure(padx=10, pady=10)

# Display currently pressed key
current_key_label = tk.Label(root, text="Press any key...", font=("Arial", 16), fg="blue")
current_key_label.pack(pady=10)

# Key log display
log_text = tk.Text(root, height=10, width=40, font=("Consolas", 12))
log_text.pack(pady=10)
log_text.insert(tk.END, "Key Log:\n")
log_text.config(state="normal")

# Bind key press
root.bind("<KeyPress>", on_key_press)

# Focus for capturing key events
root.focus_set()

root.mainloop()
