import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

tk.Label(frame, text="Name:").grid(row=0, column=0)
tk.Entry(frame).grid(row=0, column=1)
tk.Button(frame, text="Submit").grid(row=1, columnspan=2)

root.mainloop()
