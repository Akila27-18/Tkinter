import tkinter as tk

def read_text():
    content = text_box.get("1.0", tk.END)  # Get all text from line 1, character 0 to end
    print("Text widget content:\n", content.strip())  # Print to console

# GUI setup
root = tk.Tk()
root.title("Read Text Widget")
root.geometry("400x300")

tk.Label(root, text="Enter your notes:").pack(pady=5)

# Multi-line Text widget
text_box = tk.Text(root, height=10, width=50, wrap="word")
text_box.pack(padx=10, pady=10)

# Button to trigger read function
tk.Button(root, text="Print Text", command=read_text).pack(pady=10)

root.mainloop()
