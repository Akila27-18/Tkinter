import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root, bg="skyblue", width=300, height=100)
frame.pack()
frame.pack_propagate(False)

tk.Button(frame, text="I won't resize the frame").pack()

root.mainloop()
