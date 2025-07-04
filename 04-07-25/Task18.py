import tkinter as tk
from tkinter import ttk, messagebox

# Function to add shift assignment
def add_shift():
    name = entry_name.get().strip()
    shift = combo_shift.get()
    hours = spin_hours.get()

    if not name:
        messagebox.showwarning("Missing Info", "Please enter employee name.")
        return
    if shift == "Select Shift":
        messagebox.showwarning("Missing Info", "Please select a shift.")
        return

    record = f"{name} - {shift} Shift - {hours} hrs"
    listbox.insert(tk.END, record)

    # Clear inputs
    entry_name.delete(0, tk.END)
    combo_shift.set("Select Shift")
    spin_hours.delete(0, tk.END)
    spin_hours.insert(0, "8")

# --- GUI setup
root = tk.Tk()
root.title("Employee Shift Scheduler")
root.geometry("500x400")

# --- Input Frame
frame_input = tk.Frame(root, padx=10, pady=10)
frame_input.grid(row=0, column=0, sticky="w")

# Name Entry
tk.Label(frame_input, text="Employee Name:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
entry_name = tk.Entry(frame_input, width=30)
entry_name.grid(row=0, column=1, padx=5, pady=5)

# Shift Combobox
tk.Label(frame_input, text="Shift Type:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
combo_shift = ttk.Combobox(frame_input, values=["Morning", "Afternoon", "Night"], state="readonly", width=28)
combo_shift.set("Select Shift")
combo_shift.grid(row=1, column=1, padx=5, pady=5)

# Hours Spinbox
tk.Label(frame_input, text="Working Hours:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
spin_hours = tk.Spinbox(frame_input, from_=1, to=12, width=5)
spin_hours.grid(row=2, column=1, padx=5, pady=5, sticky='w')
spin_hours.delete(0, tk.END)
spin_hours.insert(0, "8")

# Add Button
btn_add = tk.Button(frame_input, text="Add Shift", command=add_shift, bg="green", fg="white", width=20)
btn_add.grid(row=3, column=0, columnspan=2, pady=10)

# --- Display Frame
frame_list = tk.Frame(root, padx=10, pady=5)
frame_list.grid(row=1, column=0, sticky="nsew")

# Scrollbar + Listbox
scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame_list, width=60, height=12, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=listbox.yview)

# --- Run App
root.mainloop()
