import tkinter as tk
from tkinter import ttk

def save_text():
    content = text_area.get("1.0", tk.END).strip()
    print("Saved Content:\n", content)

def clear_text():
    text_area.delete("1.0", tk.END)

def load_preset():
    preset = "This is a preset note.\nYou can edit this text."
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", preset)

def update_word_count(event=None):
    content = text_area.get("1.0", tk.END)
    words = content.strip().split()
    word_count.set(f"Words: {len(words)}")

# Main window
root = tk.Tk()
root.title("Mini Notepad")
root.geometry("500x400")

# Word count label
word_count = tk.StringVar(value="Words: 0")
label_word = ttk.Label(root, textvariable=word_count)
label_word.pack(anchor='e', padx=10, pady=5)

# Text editing area
text_area = tk.Text(root, wrap=tk.WORD, height=15)
text_area.pack(fill=tk.BOTH, expand=True, padx=10)
text_area.bind("<KeyRelease>", update_word_count)

# Buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Save", command=save_text).pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text="Clear", command=clear_text).pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text="Load Preset", command=load_preset).pack(side=tk.LEFT, padx=5)

root.mainloop()
