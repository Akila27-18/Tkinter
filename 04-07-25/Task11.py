import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        temp = float(spin_temp.get())
        direction = combo_direction.get()

        if direction == "Celsius to Fahrenheit":
            result = (temp * 9/5) + 32
            result_label.config(text=f"{temp}°C = {result:.2f}°F")
        elif direction == "Fahrenheit to Celsius":
            result = (temp - 32) * 5/9
            result_label.config(text=f"{temp}°F = {result:.2f}°C")
        else:
            result_label.config(text="Select conversion direction.")
    except ValueError:
        result_label.config(text="Invalid temperature input.")

# Root window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")

# Spinbox for temperature input
tk.Label(root, text="Temperature:").pack(pady=5)
spin_temp = tk.Spinbox(root, from_=-100, to=100, width=10)
spin_temp.pack()

# Combobox for conversion direction
tk.Label(root, text="Convert:").pack(pady=5)
combo_direction = ttk.Combobox(root, state="readonly", values=[
    "Celsius to Fahrenheit", 
    "Fahrenheit to Celsius"
])
combo_direction.current(0)
combo_direction.pack()

# Convert button
btn_convert = tk.Button(root, text="Convert", command=convert_temperature)
btn_convert.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=5)

root.mainloop()
