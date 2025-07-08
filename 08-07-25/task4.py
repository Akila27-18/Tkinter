import tkinter as tk

root = tk.Tk()
outer_frame = tk.Frame(root, bg="lightblue")
outer_frame.pack(padx=20, pady=20)

inner_frame = tk.Frame(outer_frame, bg="lightgreen")
inner_frame.pack(padx=10, pady=10)

tk.Label(inner_frame, text="Nested Frame").pack()

root.mainloop()
