import tkinter as tk
from datetime import datetime

def log_temperature():
    temp = temp_entry.get().strip()
    if temp:
        try:
            float(temp)  # Validate that it's a number
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = f"{timestamp} - {temp} °C\n"
            log_box.insert(tk.END, entry)
            temp_entry.delete(0, tk.END)
        except ValueError:
            log_box.insert(tk.END, "Invalid input: Please enter a numeric value.\n")
    else:
        log_box.insert(tk.END, "Please enter a temperature value.\n")

# GUI setup
root = tk.Tk()
root.title("Temperature Logger")
root.geometry("400x350")

# Temperature Entry
tk.Label(root, text="Enter Temperature (°C):").pack(pady=5)
temp_entry = tk.Entry(root, width=30)
temp_entry.pack(pady=5)

# Log Button
tk.Button(root, text="Log Temperature", command=log_temperature).pack(pady=10)

# Log Display
tk.Label(root, text="Temperature Log:").pack()
log_box = tk.Text(root, height=12, width=50, wrap='word')
log_box.pack(padx=10, pady=5)

root.mainloop()
