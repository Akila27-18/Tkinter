import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x150")

# Create labels
username_label = tk.Label(root, text="Username:")
password_label = tk.Label(root, text="Password:")

# Create entry fields
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")  # Hide password characters

# Place labels and entries using grid()
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
username_entry.grid(row=0, column=1, padx=10, pady=10)

password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Start the event loop
root.mainloop()
