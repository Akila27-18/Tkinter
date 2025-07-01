import tkinter as tk

root = tk.Tk()
root.title("Using pack() and grid() safely")

# Frame using pack()
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

tk.Label(top_frame, text="I'm packed").pack()

# Frame using grid()
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)

tk.Label(bottom_frame, text="Name:").grid(row=0, column=0, padx=5)
tk.Entry(bottom_frame).grid(row=0, column=1, padx=5)

root.mainloop()
