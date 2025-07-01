import tkinter as tk

# Main window
root = tk.Tk()
root.title("Default Entry Text")
root.geometry("300x120")

# Entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=20)

# Set default text
entry.insert(0, "Enter your name here")  # 0 = start position

root.mainloop()
