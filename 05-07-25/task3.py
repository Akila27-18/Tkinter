import tkinter as tk
from tkinter import filedialog, messagebox

# Save file function with validation
def save_file(event=None):
    content = text_area.get("1.0", tk.END).strip()
    if not content:
        messagebox.showwarning("Empty Text", "Nothing to save. Please enter some text.")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            messagebox.showinfo("Success", f"File saved to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{e}")

# Clear text function with confirmation
def clear_text():
    if messagebox.askyesno("Confirm Clear", "Are you sure you want to clear all text?"):
        text_area.delete("1.0", tk.END)

# Word count function with validation
def show_word_count():
    content = text_area.get("1.0", tk.END).strip()
    if not content:
        messagebox.showwarning("No Text", "Nothing to count. Text area is empty.")
    else:
        word_count = len(content.split())
        messagebox.showinfo("Word Count", f"Total words: {word_count}")

# --- GUI Setup ---

root = tk.Tk()
root.title("Validated Simple Notepad")
root.geometry("600x400")

# Frame for Text and Scrollbar
frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Text widget
text_area = tk.Text(frame, wrap=tk.WORD)
text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(frame, command=text_area.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_area.config(yscrollcommand=scrollbar.set)

# Frame for Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

# Buttons
btn_save = tk.Button(btn_frame, text="Save", command=save_file)
btn_save.grid(row=0, column=0, padx=5)

btn_clear = tk.Button(btn_frame, text="Clear", command=clear_text)
btn_clear.grid(row=0, column=1, padx=5)

btn_count = tk.Button(btn_frame, text="Word Count", command=show_word_count)
btn_count.grid(row=0, column=2, padx=5)

# Keyboard Shortcut: Ctrl+S to Save
root.bind('<Control-s>', save_file)

# Run the App
root.mainloop()
