import tkinter as tk

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)  # Delete from index 0 to the end

# Create main window
root = tk.Tk()
root.title("Clear Entry Example")
root.geometry("300x120")

# Create Entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create Button to clear the entry
clear_btn = tk.Button(root, text="Clear", command=clear_entry)
clear_btn.pack(pady=10)

# Start the event loop
root.mainloop()

