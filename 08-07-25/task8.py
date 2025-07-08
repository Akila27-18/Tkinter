import tkinter as tk

root = tk.Tk()

frame1 = tk.Frame(root, bg="red", width=100, height=100)
frame2 = tk.Frame(root, bg="green", width=100, height=100)
frame3 = tk.Frame(root, bg="blue", width=100, height=100)

for f in (frame1, frame2, frame3):
    f.pack(side="left", padx=5, pady=5)
    f.pack_propagate(False)

root.mainloop()
