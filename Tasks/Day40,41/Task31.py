import tkinter as tk

# Function to handle submission
def submit():
    name = name_entry.get()
    email = email_entry.get()
    print(f"Name: {name}")
    print(f"Email: {email}")

# Create the main window
root = tk.Tk()
root.title("User Form")
root.geometry("300x200")

# Name Label and Entry
tk.Label(root, text="Name:").pack(pady=(10, 0))
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Email Label and Entry
tk.Label(root, text="Email:").pack(pady=(10, 0))
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

# Submit Button
tk.Button(root, text="Submit", command=submit).pack(pady=15)

# Run the main loop
root.mainloop()
