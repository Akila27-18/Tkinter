import tkinter as tk

root = tk.Tk()
pw = tk.PanedWindow(root, orient=tk.HORIZONTAL)
pw.pack(fill=tk.BOTH, expand=True)

pw.add(tk.Frame(pw, bg="lightcoral", width=100))
pw.add(tk.Frame(pw, bg="lightseagreen", width=100))
pw.add(tk.Frame(pw, bg="khaki", width=100))

root.mainloop()
