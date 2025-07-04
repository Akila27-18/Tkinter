import tkinter as tk
from tkinter import ttk

# Main app window
root = tk.Tk()
root.title("Customer Feedback Collector")
root.geometry("600x400")

# Store feedback as (category, name, message)
feedback_list = []

# ---- Input Section ----

# Feedback category
category_var = tk.StringVar()
category_combo = ttk.Combobox(root, textvariable=category_var, values=["Service", "Product", "Delivery"], state="readonly")
category_combo.set("Service")
category_combo.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
tk.Label(root, text="Category:").grid(row=0, column=0, padx=10, sticky="e")

# Name entry
name_var = tk.StringVar()
name_entry = tk.Entry(root, textvariable=name_var)
name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
tk.Label(root, text="Name:").grid(row=1, column=0, padx=10, sticky="e")

# Message entry
message_var = tk.StringVar()
message_entry = tk.Entry(root, textvariable=message_var)
message_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
tk.Label(root, text="Message:").grid(row=2, column=0, padx=10, sticky="e")

# ---- Submit Feedback ----

def submit_feedback():
    category = category_var.get()
    name = name_var.get().strip()
    message = message_var.get().strip()
    
    if name and message:
        feedback = (category, name, message)
        feedback_list.append(feedback)
        name_var.set("")
        message_var.set("")
        update_listbox()
    else:
        print("Please enter both name and message.")

submit_btn = tk.Button(root, text="Submit Feedback", command=submit_feedback)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

# ---- Feedback Display Section ----

# Frame for Listbox + Scrollbar
list_frame = tk.Frame(root)
list_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

feedback_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, width=80, height=10)
feedback_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=feedback_listbox.yview)

# ---- Filter Section ----

filter_var = tk.StringVar()
filter_combo = ttk.Combobox(root, textvariable=filter_var, values=["All", "Service", "Product", "Delivery"], state="readonly")
filter_combo.set("All")
filter_combo.grid(row=5, column=1, padx=10, pady=5, sticky="ew")
tk.Label(root, text="Filter by Category:").grid(row=5, column=0, padx=10, sticky="e")

def update_listbox(*args):
    feedback_listbox.delete(0, tk.END)
    selected_category = filter_var.get()

    for cat, name, msg in feedback_list:
        if selected_category == "All" or selected_category == cat:
            feedback_listbox.insert(tk.END, f"[{cat}] {name}: {msg}")

# Trigger filtering when filter changed
filter_combo.bind("<<ComboboxSelected>>", update_listbox)

# Grid expand behavior
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(1, weight=1)

# Run app
root.mainloop()
