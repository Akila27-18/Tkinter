import tkinter as tk

# List to store contacts
contacts = []

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    
    if name and phone:
        contact = f"{name} - {phone}"
        contacts.append(contact)
        update_contact_display()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        contact_display.insert(tk.END, "Please enter both name and phone.\n")

def update_contact_display():
    contact_display.delete("1.0", tk.END)
    for contact in contacts:
        contact_display.insert(tk.END, contact + "\n")

# GUI setup
root = tk.Tk()
root.title("Basic Contact Book")
root.geometry("400x400")

# Name Entry
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

# Phone Entry
tk.Label(root, text="Phone:").pack(pady=5)
phone_entry = tk.Entry(root, width=40)
phone_entry.pack(pady=5)

# Add Button
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack(pady=10)

# Display Area
contact_display = tk.Text(root, height=12, width=45)
contact_display.pack(pady=10)

# Run the application
root.mainloop()
