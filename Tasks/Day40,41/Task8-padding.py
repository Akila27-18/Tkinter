import tkinter as tk

# Create main window
root = tk.Tk()
root.title("User Registration Form")
root.geometry("350x200")

# Labels and Entry fields
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)

email_label = tk.Label(root, text="Email:")
email_entry = tk.Entry(root)

password_label = tk.Label(root, text="Password:")
password_entry = tk.Entry(root, show="*")

# Use grid with padding
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry.grid(row=0, column=1, padx=10, pady=10)

email_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
email_entry.grid(row=1, column=1, padx=10, pady=10)

password_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
password_entry.grid(row=2, column=1, padx=10, pady=10)

# Submit button
submit_btn = tk.Button(root, text="Register")
submit_btn.grid(row=3, column=0, columnspan=2, pady=20)

# Start the event loop
root.mainloop()
