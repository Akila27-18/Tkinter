import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def key_press(event):
    char = event.char
    if char in "0123456789+-*/.":
        button_click(char)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "BackSpace":
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])

# Main window
root = tk.Tk()
root.title("Calculator with Keyboard Support")
root.geometry("300x400")

# Entry widget
entry = tk.Entry(root, font=('Arial', 20), bd=8, relief=tk.RIDGE, justify='right')
entry.pack(fill='both', padx=10, pady=10, ipady=10)
entry.focus_set()

# Bind keyboard events
root.bind("<Key>", key_press)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill='both')
    for char in row:
        if char == '=':
            btn = tk.Button(row_frame, text=char, font=('Arial', 18), height=2, width=5, command=calculate)
        else:
            btn = tk.Button(row_frame, text=char, font=('Arial', 18), height=2, width=5,
                            command=lambda ch=char: button_click(ch))
        btn.pack(side='left', expand=True, fill='both')

# Clear Button
tk.Button(root, text="Clear", font=('Arial', 16), command=clear_entry).pack(fill='both', padx=10, pady=10)

root.mainloop()
