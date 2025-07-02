import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Password Entry")
root.geometry("300x150")

# Label
tk.Label(root, text="Enter your password:").pack(pady=5)

# Password Entry (masked with *)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=10)

# Run the event loop
root.mainloop()
