import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

tk.Button(frame, text="Button 1").pack()
tk.Button(frame, text="Button 2").pack()
tk.Button(frame, text="Button 3").pack()

root.mainloop()
