import tkinter as tk

# Function to run when Enter key is pressed
def on_enter(event):
    text = entry.get()
    result_label.config(text=f"You typed: {text}")

# Create main window
root = tk.Tk()
root.title("Enter Key Event")
root.geometry("300x150")

# Entry widget
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

# Bind Enter key to the entry
entry.bind("<Return>", on_enter)

# Label to show result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the event loop
root.mainloop()
