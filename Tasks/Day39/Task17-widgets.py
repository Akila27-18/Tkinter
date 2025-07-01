import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Widgets in a Frame")
root.geometry("300x200")

# Create a Frame
frame = tk.Frame(root, bg="lightblue", bd=2, relief=tk.GROOVE)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Add a Label inside the frame
tk.Label(frame, text="Enter your name:", bg="lightblue").pack(pady=5)

# Add an Entry inside the frame
tk.Entry(frame, width=25).pack(pady=5)

root.mainloop()
