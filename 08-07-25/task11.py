import tkinter as tk

root = tk.Tk()

frame_top = tk.Frame(root)
frame_top.pack()

frame_bottom = tk.Frame(root)
frame_bottom.pack()

tk.Label(frame_top, text="Top Label (pack)").pack()

tk.Label(frame_bottom, text="Name:").grid(row=0, column=0)
tk.Entry(frame_bottom).grid(row=0, column=1)

root.mainloop()
