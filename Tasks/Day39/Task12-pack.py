import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Pack() Layout Example")
root.geometry("300x200")

# Widget 1: Label
label = tk.Label(root, text="This is a Label", bg="lightblue", pady=10)
label.pack(fill='x')  # fill x-axis for full width

# Widget 2: Entry
entry = tk.Entry(root)
entry.pack(pady=10)  # vertical spacing

# Widget 3: Button
button = tk.Button(root, text="Click Me")
button.pack(pady=10)

# Run the application
root.mainloop()
