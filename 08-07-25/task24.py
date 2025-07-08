import tkinter as tk

root = tk.Tk()
pw = tk.PanedWindow(root, orient=tk.HORIZONTAL)
pw.pack(fill=tk.BOTH, expand=True)

pw.add(tk.Entry(pw))
pw.add(tk.Listbox(pw))
pw.add(tk.Canvas(pw, bg="white"))

root.mainloop()
