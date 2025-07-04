import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == '+':
            result.set(num1 + num2)
        elif op == '-':
            result.set(num1 - num2)
        elif op == '*':
            result.set(num1 * num2)
        elif op == '/':
            if num2 != 0:
                result.set(num1 / num2)
            else:
                result.set("Error: Divide by 0")
        else:
            result.set("Select operation")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

# Main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry fields
tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Operation selector
tk.Label(root, text="Operation:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
operation = ttk.Combobox(root, values=["+", "-", "*", "/"], state="readonly")
operation.grid(row=2, column=1, padx=5, pady=5)
operation.set('+')  # Default value

# Calculate button
calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
result = tk.StringVar()
tk.Label(root, text="Result:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, textvariable=result).grid(row=4, column=1, padx=5, pady=5)

root.mainloop()
