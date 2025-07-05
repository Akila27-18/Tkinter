import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        if weight <= 0 or weight >= 150:
            result_label.config(text="Weight must be between 0 and 150 kg", fg="red")
            return

        if height_cm <= 0:
            result_label.config(text="Height must be a positive number", fg="red")
            return

        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        result_label.config(text=f"BMI: {bmi:.2f}", fg="black")

    except ValueError:
        result_label.config(text="Enter valid numeric values", fg="red")

# === GUI Setup ===
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")
root.resizable(False, False)

# === Layout ===
tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10, sticky="e")
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

tk.Label(root, text="Height (cm):").grid(row=1, column=0, padx=10, pady=10, sticky="e")
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

calc_btn = tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="green", fg="white")
calc_btn.grid(row=2, column=0, columnspan=2, pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
