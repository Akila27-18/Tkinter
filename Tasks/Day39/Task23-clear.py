import tkinter as tk

def clear_widgets():
    entry.delete(0, tk.END)         # Clear Entry widget
    text_box.delete("1.0", tk.END)  # Clear Text widget

# Main window
root = tk.Tk()
root.title("Clear Entry/Text Example")
root.geometry("400x250")

# Entry widget
tk.Label(root, text="Single-line Entry:").pack()
entry = tk.Entry(root, width=40)
entry.pack(pady=5)
entry.insert(0, "Default entry text")

# Text widget
tk.Label(root, text="Multi-line Text:").pack()
text_box = tk.Text(root, width=40, height=5)
text_box.pack(pady=5)
text_box.insert("1.0", "Default multi-line text")

# Clear button
tk.Button(root, text="Clear All", command=clear_widgets).pack(pady=10)

root.mainloop()
