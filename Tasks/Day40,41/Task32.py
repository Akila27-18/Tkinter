import tkinter as tk

# Function to retrieve and print the entered values
def submit():
    name = name_entry.get()
    email = email_entry.get()
    print("Name:", name)
    print("Email:", email)

# Create the main window
root = tk.Tk()
root.title("User Info")
root.geometry("300x200")

# Name field
tk.Label(root, text="Name:").pack(pady=(10, 0))
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Email field
tk.Label(root, text="Email:").pack(pady=(10, 0))
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.pack(pady=15)

# Start the event loop
root.mainloop()
