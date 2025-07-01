import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Frame Widget Example")
root.geometry("300x200")

# Create a Frame inside the main window
frame = tk.Frame(root, bg="lightgray", bd=2, relief=tk.SUNKEN)
frame.pack(padx=20, pady=20, fill='both', expand=True)

# Add a widget inside the frame
tk.Label(frame, text="I'm inside a Frame!").pack(pady=10)
tk.Button(frame, text="Click Me").pack()

root.mainloop()
