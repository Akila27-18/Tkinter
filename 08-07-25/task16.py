import tkinter as tk

root = tk.Tk()
pw = tk.PanedWindow(root, orient=tk.HORIZONTAL)
pw.pack(fill=tk.BOTH, expand=True)

left = tk.Frame(pw, bg='lightblue')
right = tk.Frame(pw, bg='lightgreen')

pw.add(left)
pw.add(right)

root.mainloop()
