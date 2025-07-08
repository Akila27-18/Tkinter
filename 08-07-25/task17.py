import tkinter as tk

root = tk.Tk()
pw = tk.PanedWindow(root, orient=tk.VERTICAL)
pw.pack(fill=tk.BOTH, expand=True)

text = tk.Text(pw, height=5)
form = tk.Frame(pw)
tk.Label(form, text="Name:").grid(row=0, column=0)
tk.Entry(form).grid(row=0, column=1)

pw.add(text)
pw.add(form)

root.mainloop()
