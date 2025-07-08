import tkinter as tk

root = tk.Tk()

personal_frame = tk.LabelFrame(root, text="Personal Info", padx=10, pady=10)
contact_frame = tk.LabelFrame(root, text="Contact Info", padx=10, pady=10)

personal_frame.pack(padx=10, pady=5, fill="x")
contact_frame.pack(padx=10, pady=5, fill="x")

tk.Label(personal_frame, text="Name:").grid(row=0, column=0)
tk.Entry(personal_frame).grid(row=0, column=1)

tk.Label(contact_frame, text="Email:").grid(row=0, column=0)
tk.Entry(contact_frame).grid(row=0, column=1)

root.mainloop()
