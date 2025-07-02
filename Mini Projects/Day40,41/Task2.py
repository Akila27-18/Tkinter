import tkinter as tk
from tkinter import filedialog, messagebox

def save_note():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as f:
            f.write(text_area.get("1.0", tk.END))
        messagebox.showinfo("Saved", "Note saved successfully!")

def load_note():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as f:
            content = f.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, content)

def clear_note():
    text_area.delete("1.0", tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("Simple Notepad")
root.geometry("500x400")  # Allow resizing

# Text Area
text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both")

# Button Frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

# Buttons
tk.Button(btn_frame, text="Save", command=save_note, width=10).pack(side="left", padx=5)
tk.Button(btn_frame, text="Load", command=load_note, width=10).pack(side="left", padx=5)
tk.Button(btn_frame, text="Clear", command=clear_note, width=10).pack(side="left", padx=5)

root.mainloop()
