import tkinter as tk
from tkinter import ttk

def convert():
    try:
        val = float(input_entry.get())
        option = conversion_type.get()

        if option == "cm to inch":
            result = val / 2.54
        elif option == "inch to cm":
            result = val * 2.54
        elif option == "Celsius to Fahrenheit":
            result = (val * 9/5) + 32
        elif option == "Fahrenheit to Celsius":
            result = (val - 32) * 5/9
        else:
            result = "Invalid"

        output_entry.config(state='normal')
        output_entry.delete(0, tk.END)
        output_entry.insert(0, f"{round(result, 2)}")
        output_entry.config(state='readonly')
    except ValueError:
        output_entry.config(state='normal')
        output_entry.delete(0, tk.END)
        output_entry.insert(0, "Enter valid number")
        output_entry.config(state='readonly')

# GUI setup
root = tk.Tk()
root.title("Unit Converter")
root.geometry("350x250")

# Conversion Type
tk.Label(root, text="Select Conversion:").pack(pady=5)
conversion_type = ttk.Combobox(root, values=[
    "cm to inch",
    "inch to cm",
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius"
], state="readonly")
conversion_type.pack(pady=5)
conversion_type.current(0)

# Input Field
tk.Label(root, text="Enter value:").pack(pady=5)
input_entry = tk.Entry(root, width=25)
input_entry.pack(pady=5)

# Convert Button
tk.Button(root, text="Convert", command=convert).pack(pady=10)

# Output Field
tk.Label(root, text="Result:").pack(pady=5)
output_entry = tk.Entry(root, width=25, state='readonly')
output_entry.pack(pady=5)

root.mainloop()
