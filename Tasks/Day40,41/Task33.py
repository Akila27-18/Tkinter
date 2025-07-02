import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Pre-filled Entry")
root.geometry("300x100")

# Create entry and insert default text
entry = tk.Entry(root, width=30)
entry.insert(0, "Enter Name")  # Insert at position 0
entry.pack(pady=20)

# Start the event loop
root.mainloop()
