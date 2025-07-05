import tkinter as tk
from tkinter import ttk

def convert_temp():
    try:
        temp = float(temp_spinbox.get())
        direction = direction_combo.get()

        if direction == "Celsius to Fahrenheit":
            result = (temp * 9/5) + 32
            result_label.config(text=f"{temp}°C = {result:.2f}°F", fg="black")
        elif direction == "Fahrenheit to Celsius":
            result = (temp - 32) * 5/9
            result_label.config(text=f"{temp}°F = {result:.2f}°C", fg="black")
        else:
            result_label.config(text="Please select conversion type.", fg="red")

    except ValueError:
        result_label.config(text="Enter a valid number!", fg="red")

# === GUI Setup ===
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x200")
root.resizable(False, False)

# === Layout ===
tk.Label(root, text="Temperature:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
temp_spinbox = tk.Spinbox(root, from_=-100, to=100, width=10)
temp_spinbox.grid(row=0, column=1)

tk.Label(root, text="Convert:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
direction_combo = ttk.Combobox(root, values=["Celsius to Fahrenheit", "Fahrenheit to Celsius"], state="readonly", width=25)
direction_combo.grid(row=1, column=1)

convert_btn = tk.Button(root, text="Convert", command=convert_temp, bg="blue", fg="white", width=15)
convert_btn.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
