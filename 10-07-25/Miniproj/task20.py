import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(
        title="Open Text File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not file_path:
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except Exception as e:
        messagebox.showerror("Error", f"Could not open file:\n{e}")
        return

    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, content)
    update_counts()

def update_counts(event=None):
    content = text_box.get("1.0", tk.END).strip()
    words = content.split()
    lines = content.splitlines()
    chars = len(content)

    label_words.config(text=f"Words: {len(words)}")
    label_lines.config(text=f"Lines: {len(lines)}")
    label_chars.config(text=f"Characters: {chars}")

# GUI Setup
root = tk.Tk()
root.title("File Preview and Word Counter")
root.geometry("600x500")

tk.Button(
    root,
    text="Open File",
    command=open_file,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12),
    padx=10,
    pady=5
).pack(pady=10)

text_box = tk.Text(root, wrap="word", height=20, width=70, font=("Courier New", 10))
text_box.pack(padx=10, pady=10)
text_box.bind("<KeyRelease>", update_counts)

frame_counts = tk.Frame(root)
frame_counts.pack(pady=5)

label_words = tk.Label(frame_counts, text="Words: 0", font=("Arial", 10))
label_words.grid(row=0, column=0, padx=10)

label_lines = tk.Label(frame_counts, text="Lines: 0", font=("Arial", 10))
label_lines.grid(row=0, column=1, padx=10)

label_chars = tk.Label(frame_counts, text="Characters: 0", font=("Arial", 10))
label_chars.grid(row=0, column=2, padx=10)

root.mainloop()
