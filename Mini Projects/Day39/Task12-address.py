import tkinter as tk

def display_info():
    name = name_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    info = f"Name: {name}\nAddress: {address}\nPhone: {phone}\nEmail: {email}"
    
    output_box.config(state='normal')
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, info)
    output_box.config(state='disabled')  # Make it read-only

# GUI setup
root = tk.Tk()
root.title("Simple Address Form")
root.geometry("400x350")

# Name
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack()

# Address
tk.Label(root, text="Address:").pack(pady=5)
address_entry = tk.Entry(root, width=40)
address_entry.pack()

# Phone
tk.Label(root, text="Phone:").pack(pady=5)
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

# Email
tk.Label(root, text="Email:").pack(pady=5)
email_entry = tk.Entry(root, width=40)
email_entry.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit", command=display_info)
submit_button.pack(pady=10)

# Output Box (read-only)
output_box = tk.Text(root, height=6, width=45)
output_box.pack(pady=5)
output_box.config(state='disabled')

root.mainloop()
