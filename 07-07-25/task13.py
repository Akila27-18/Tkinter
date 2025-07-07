import tkinter as tk
from tkinter import filedialog

def save_text():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as f:
            content = text_area.get("1.0", tk.END)
            f.write(content)

def clear_text():
    text_area.delete("1.0", tk.END)
    update_count()

def insert_sample():
    sample = "Welcome to the Tkinter Text Editor!\nYou can write and save your notes here."
    text_area.insert("1.0", sample)
    update_count()

def update_count(event=None):
    content = text_area.get("1.0", tk.END).strip()
    char_count = len(content)
    word_count = len(content.split())
    count_label.config(text=f"Chars: {char_count}  |  Words: {word_count}")

# Main window setup
root = tk.Tk()
root.title("Text Editor")
root.geometry("500x400")
root.resizable(False, False)

# Text widget
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(padx=10, pady=10, expand=True, fill="both")

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Save", command=save_text).pack(side="left", padx=10)
tk.Button(button_frame, text="Clear", command=clear_text).pack(side="left", padx=10)
tk.Button(button_frame, text="Insert Sample", command=insert_sample).pack(side="left", padx=10)

# Character/Word count label
count_label = tk.Label(root, text="Chars: 0  |  Words: 0", font=("Arial", 10))
count_label.pack(pady=5)

# Update count on any key press
text_area.bind("<KeyRelease>", update_count)

# Start with sample text
insert_sample()

# Run the application
root.mainloop()
