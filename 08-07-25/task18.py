import tkinter as tk

root = tk.Tk()
pw = tk.PanedWindow(root, orient=tk.HORIZONTAL)
pw.pack(fill=tk.BOTH, expand=True)

label1 = tk.Label(pw, text="Left Pane", bg="lightblue")
label2 = tk.Label(pw, text="Right Pane", bg="lightgreen")

pw.add(label1)
pw.add(label2)

root.mainloop()
