import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Multi-line Text Widget")
root.geometry("400x300")

# Label for instruction
tk.Label(root, text="Enter your text below:").pack(pady=5)

# Multi-line Text widget
text_box = tk.Text(root, height=10, width=50, wrap="word")
text_box.pack(padx=10, pady=10)

# Start the GUI loop
root.mainloop()
