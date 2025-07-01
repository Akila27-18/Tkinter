import tkinter as tk

root = tk.Tk()
root.title("Grid Span Example")
root.geometry("300x200")

# Label across 2 columns
tk.Label(root, text="This spans two columns", bg="lightblue").grid(row=0, column=0, columnspan=2, pady=10)

# Button in first column
tk.Button(root, text="Left").grid(row=1, column=0, padx=10, pady=10)

# Button in second column
tk.Button(root, text="Right").grid(row=1, column=1, padx=10, pady=10)

# Textbox that spans 2 rows
tk.Text(root, height=4, width=20).grid(row=2, column=0, rowspan=2, padx=10, pady=10)

# Label next to textbox
tk.Label(root, text="Next to textbox").grid(row=2, column=1)

root.mainloop()
