import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("3x3 Button Matrix")
root.geometry("200x200")

# Create a 3x3 grid of buttons
button_texts = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

for i in range(3):         # Rows
    for j in range(3):     # Columns
        btn = tk.Button(root, text=button_texts[i][j], width=5, height=2)
        btn.grid(row=i, column=j, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
