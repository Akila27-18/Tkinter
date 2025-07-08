import tkinter as tk

root = tk.Tk()
pw = tk.PanedWindow(root, orient=tk.HORIZONTAL)
pw.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(pw, bg="white")
pw.add(canvas)

pw.add(tk.Label(pw, text="Side Panel"))

root.mainloop()
