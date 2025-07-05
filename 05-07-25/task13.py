import tkinter as tk
from tkinter import ttk, messagebox

# --- Calculate Function ---
def calculate():
    num1 = entry1.get().strip()
    num2 = entry2.get().strip()
    operation = operation_box.get()

    # Validate input
    try:
        val1 = float(num1)
        val2 = float(num2)
    except ValueError:
        result_label.config(text="❌ Enter valid numbers", fg="red")
        return

    # Perform calculation
    try:
        if operation == "+":
            result = val1 + val2
        elif operation == "-":
            result = val1 - val2
        elif operation == "×":
            result = val1 * val2
        elif operation == "÷":
            if val2 == 0:
                raise ZeroDivisionError
            result = val1 / val2
        else:
            result_label.config(text="❌ Select operation", fg="orange")
            return

        result_label.config(text=f"✅ Result: {result}", fg="green")
    except ZeroDivisionError:
        result_label.config(text="❌ Cannot divide by zero", fg="red")

# --- Main App Window ---
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x250")

# --- UI Layout with grid() ---
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Select operation:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
operation_box = ttk.Combobox(root, values=["+", "-", "×", "÷"], state="readonly")
operation_box.grid(row=2, column=1, padx=10, pady=5)
operation_box.set("+")  # default

calc_btn = tk.Button(root, text="Calculate", command=calculate)
calc_btn.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11, "bold"))
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# --- Run App ---
root.mainloop()
