import tkinter as tk

def new_file():
    global current_file
    current_file = None
    text.delete("1.0", tk.END)
    root.title("New File")

current_file = None

root = tk.Tk()
root.title("Text Editor")

text = tk.Text(root, width=60, height=20)
text.pack(padx=10, pady=10)

tk.Button(root, text="New", command=new_file).pack(pady=10)

root.mainloop()
