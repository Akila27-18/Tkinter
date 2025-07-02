import tkinter as tk

def button_click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + char)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: Div by 0")
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Invalid Input")

# --- GUI Setup ---
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")
root.resizable(False, False)

# Entry for input/output
entry = tk.Entry(root, width=25, font=("Arial", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button definitions
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        tk.Button(root, text=text, width=5, height=2, command=calculate).grid(row=row, column=col, padx=5, pady=5)
    elif text == "C":
        tk.Button(root, text=text, width=22, height=2, command=clear).grid(row=row, column=col, columnspan=4, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, height=2, command=lambda t=text: button_click(t)).grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
