import tkinter as tk

def submit_survey():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    color = color_entry.get().strip()

    if name and age and color:
        try:
            int(age)  # Validate that age is a number
            summary = (
                f"Survey Summary:\n"
                f"Name: {name}\n"
                f"Age: {age}\n"
                f"Favorite Color: {color}"
            )
            result_label.config(text=summary, fg="blue")
            name_entry.delete(0, tk.END)
            age_entry.delete(0, tk.END)
            color_entry.delete(0, tk.END)
        except ValueError:
            result_label.config(text="Age must be a number.", fg="red")
    else:
        result_label.config(text="Please fill in all fields.", fg="red")

# GUI setup
root = tk.Tk()
root.title("Simple Survey App")
root.geometry("400x350")

# Name
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack()

# Age
tk.Label(root, text="Age:").pack(pady=5)
age_entry = tk.Entry(root, width=40)
age_entry.pack()

# Favorite Color
tk.Label(root, text="Favorite Color:").pack(pady=5)
color_entry = tk.Entry(root, width=40)
color_entry.pack()

# Submit Button
tk.Button(root, text="Submit", command=submit_survey).pack(pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()
