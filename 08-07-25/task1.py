import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="This is inside a Frame")
label.pack()

root.mainloop()
