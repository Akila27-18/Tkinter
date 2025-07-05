import tkinter as tk
import re

def validate_name(name):
    return re.match(r'^[A-Za-z ]+$', name)

def validate_number(number):
    return re.match(r'^\d{10}$', number)

def add_contact():
    name = name_entry.get().strip()
    number = number_entry.get().strip()

    if not name or not number:
        message_label.config(text="Both fields are required!", fg="red")
        return

    if not validate_name(name):
        message_label.config(text="Invalid name. Use only letters and spaces.", fg="red")
        return

    if not validate_number(number):
        message_label.config(text="Invalid number. Enter 10-digit number.", fg="red")
        return

    contact = f"{name} - {number}"
    contact_listbox.insert(tk.END, contact)
    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)
    message_label.config(text="Contact added successfully!", fg="green")

def show_selected(event):
    selected = contact_listbox.curselection()
    if selected:
        contact = contact_listbox.get(selected[0])
        selected_label.config(text=f"Selected: {contact}")

def clear_contacts():
    contact_listbox.delete(0, tk.END)
    selected_label.config(text="")
    message_label.config(text="All contacts cleared!", fg="blue")

# === GUI Setup ===
root = tk.Tk()
root.title("Contact Book with Validation")
root.geometry("400x360")
root.resizable(False, False)

# === Input Fields ===
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Phone Number:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
number_entry = tk.Entry(root, width=30)
number_entry.grid(row=1, column=1)

# === Buttons ===
add_btn = tk.Button(root, text="Add Contact", command=add_contact, bg="green", fg="white", width=15)
add_btn.grid(row=2, column=0, columnspan=2, pady=10)

clear_btn = tk.Button(root, text="Clear All", command=clear_contacts, bg="red", fg="white", width=15)
clear_btn.grid(row=3, column=0, columnspan=2)

# === Listbox with Scrollbar ===
list_frame = tk.Frame(root)
list_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

contact_listbox = tk.Listbox(list_frame, width=45, height=8, yscrollcommand=scrollbar.set)
contact_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=contact_listbox.yview)

contact_listbox.bind("<Double-Button-1>", show_selected)

# === Selected Contact Label ===
selected_label = tk.Label(root, text="", font=("Arial", 10))
selected_label.grid(row=5, column=0, columnspan=2)

# === Message Label ===
message_label = tk.Label(root, text="", font=("Arial", 10))
message_label.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()
