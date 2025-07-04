import tkinter as tk

root = tk.Tk()
root.title("Time Selector")
root.geometry("250x200")

# Label
tk.Label(root, text="Select Time:", font=("Arial", 12)).pack(pady=10)

# Frame to hold the two spinboxes side by side
frame = tk.Frame(root)
frame.pack(pady=10)

# Spinbox for hours (1 to 12)
hour_spin = tk.Spinbox(frame, from_=1, to=12, width=5, font=("Arial", 10))
hour_spin.pack(side=tk.LEFT, padx=5)

# Spinbox for AM/PM using values option
ampm_spin = tk.Spinbox(frame, values=("AM", "PM"), width=5, font=("Arial", 10), state="readonly")
ampm_spin.pack(side=tk.LEFT, padx=5)

# Optional: Show selected time on button click
def show_time():
    selected_time = f"{hour_spin.get()} {ampm_spin.get()}"
    result_label.config(text=f"Selected Time: {selected_time}")

tk.Button(root, text="Show Time", command=show_time).pack(pady=5)
result_label = tk.Label(root, text="", font=("Arial", 10))
result_label.pack()

root.mainloop()
