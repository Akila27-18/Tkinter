import tkinter as tk
from tkinter import ttk, messagebox

def calculate_bmi():
    try:
        height_cm = float(height_spin.get())
        weight_kg = float(weight_spin.get())

        if height_cm <= 0 or weight_kg <= 0:
            raise ValueError

        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        bmi = round(bmi, 2)

        # Determine category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi} ({category})")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid height and weight.")

# Main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

# Height input
ttk.Label(root, text="Height (cm):").pack(pady=5)
height_spin = tk.Spinbox(root, from_=50, to=250, width=10)
height_spin.pack()

# Weight input
ttk.Label(root, text="Weight (kg):").pack(pady=5)
weight_spin = tk.Spinbox(root, from_=10, to=200, width=10)
weight_spin.pack()

# Calculate button
calc_btn = ttk.Button(root, text="Calculate BMI", command=calculate_bmi)
calc_btn.pack(pady=15)

# Result label
result_label = ttk.Label(root, text="Enter your height and weight")
result_label.pack(pady=10)

# Run app
root.mainloop()
