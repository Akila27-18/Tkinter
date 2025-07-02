import tkinter as tk
from datetime import datetime

def save_note():
    note = text_note.get("1.0", tk.END).strip()
    if note:
        filename = datetime.now().strftime("%Y-%m-%d") + ".txt"
        with open(filename, "w") as f:
            f.write(note)
        status_label.config(text="Note saved", fg="green")
    else:
        status_label.config(text="Note is empty", fg="red")

# --- GUI Setup ---
root = tk.Tk()
root.title("Simple Diary App")
root.geometry("500x400")

# Widgets
tk.Label(root, text="Write your note:", font=("Arial", 12)).grid(row=0, column=0, pady=10, padx=10, sticky="w")

text_note = tk.Text(root, width=60, height=15, wrap="word")
text_note.grid(row=1, column=0, padx=10)

tk.Button(root, text="Save Note", command=save_note, width=15).grid(row=2, column=0, pady=10)

status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.grid(row=3, column=0)

root.mainloop()
