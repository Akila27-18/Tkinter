import tkinter as tk

def calculate_bmi():
    try:
        height_cm = float(height_entry.get())
        weight_kg = float(weight_entry.get())

        height_m = height_cm / 100  # Convert cm to meters
        bmi = weight_kg / (height_m ** 2)

        # Determine category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi:.2f} ({category})")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

# GUI setup
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

# Height Entry
tk.Label(root, text="Height (cm):").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack()

# Weight Entry
tk.Label(root, text="Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

# Calculate Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
