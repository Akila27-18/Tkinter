import tkinter as tk
from tkinter import ttk

# Sample employee list
employees = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen", "Ian", "Jack", "Karen", "Leo"]

# Tkinter app
root = tk.Tk()
root.title("Employee Shift Scheduler")
root.geometry("600x400")

# ---- Employee Listbox ----
tk.Label(root, text="Select Employee:").grid(row=0, column=0, padx=10, pady=5, sticky="w")

emp_listbox = tk.Listbox(root, height=8, selectmode=tk.SINGLE)
emp_listbox.grid(row=1, column=0, padx=10, pady=5, sticky="n")

# Populate employees
for emp in employees:
    emp_listbox.insert(tk.END, emp)

# ---- Shift Selection ----
tk.Label(root, text="Shift Type:").grid(row=0, column=1, padx=10, pady=5, sticky="w")
shift_var = tk.StringVar()
shift_combo = ttk.Combobox(root, textvariable=shift_var, values=["Morning", "Evening", "Night"], state="readonly")
shift_combo.set("Morning")
shift_combo.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Hours:").grid(row=2, column=1, padx=10, pady=5, sticky="w")
hours_var = tk.IntVar(value=8)
hours_spin = tk.Spinbox(root, from_=1, to=12, textvariable=hours_var, width=5)
hours_spin.grid(row=3, column=1, padx=10, sticky="w")

# ---- Assigned Shifts Listbox ----
tk.Label(root, text="Assigned Shifts:").grid(row=0, column=2, padx=10, pady=5, sticky="w")

shift_frame = tk.Frame(root)
shift_frame.grid(row=1, column=2, rowspan=5, padx=10, pady=5, sticky="nsew")

scrollbar = tk.Scrollbar(shift_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

assigned_listbox = tk.Listbox(shift_frame, height=12, yscrollcommand=scrollbar.set, width=40)
assigned_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=assigned_listbox.yview)

# ---- Assign Shift Function ----
def assign_shift():
    selection = emp_listbox.curselection()
    if not selection:
        return
    
    emp = emp_listbox.get(selection[0])
    shift = shift_var.get()
    hours = hours_var.get()
    
    assigned_listbox.insert(tk.END, f"{emp} - {shift} Shift - {hours} hours")

# ---- Assign Button ----
assign_btn = tk.Button(root, text="Assign Shift", command=assign_shift)
assign_btn.grid(row=4, column=1, pady=10)

# Configure resizing
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=2)

root.mainloop()
