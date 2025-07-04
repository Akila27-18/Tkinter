import tkinter as tk
from tkinter import ttk, messagebox

# Store progress in a dictionary
progress_data = {}

def update_progress():
    module = combo_module.get()
    level = int(spin_level.get())

    if not module:
        messagebox.showerror("Input Error", "Please select a module.")
        return

    # Save progress
    progress_data[module] = level

    # Add to completed list if not already
    if module not in listbox.get(0, tk.END):
        listbox.insert(tk.END, module)

    draw_progress_bar()

def draw_progress_bar():
    canvas.delete("all")
    canvas.create_rectangle(10, 20, 310, 50, outline="black", width=2)
    
    for i, (module, level) in enumerate(progress_data.items()):
        fill_width = 300 * (level / 10)
        color = "#4caf50" if level >= 7 else "#ffa500" if level >= 4 else "#f44336"
        canvas.create_rectangle(10, 20, 10 + fill_width, 50, fill=color, outline="")
        canvas.create_text(160, 35, text=f"{module}: {level}/10", fill="white", font=("Arial", 12, "bold"))

# Main window
root = tk.Tk()
root.title("Learning Dashboard – Project Tracker")
root.geometry("400x350")

# --- Module Selection ---
tk.Label(root, text="Select Module:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
combo_module = ttk.Combobox(root, values=[
    "Tkinter Basics", "Canvas Widgets", "Event Handling", "Layout Managers", "Widgets and Styling"
], state="readonly")
combo_module.grid(row=0, column=1, padx=10, pady=5)

# --- Understanding Level ---
tk.Label(root, text="Understanding Level (1–10):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
spin_level = tk.Spinbox(root, from_=1, to=10, width=5)
spin_level.grid(row=1, column=1, sticky="w", padx=10, pady=5)
spin_level.delete(0, tk.END)
spin_level.insert(0, 5)

# --- Update Button ---
btn_update = tk.Button(root, text="Update Progress", command=update_progress)
btn_update.grid(row=2, column=0, columnspan=2, pady=10)

# --- Canvas Progress ---
tk.Label(root, text="Progress Bar:").grid(row=3, column=0, padx=10, pady=5, sticky="ne")
canvas = tk.Canvas(root, width=320, height=60, bg="white")
canvas.grid(row=3, column=1, padx=10, pady=5)

# --- Completed Topics ---
tk.Label(root, text="Completed Topics:").grid(row=4, column=0, padx=10, pady=5, sticky="ne")
frame_listbox = tk.Frame(root)
frame_listbox.grid(row=4, column=1, padx=10, pady=5, sticky="nsew")

listbox = tk.Listbox(frame_listbox, height=6, width=35)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame_listbox, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

root.mainloop()
