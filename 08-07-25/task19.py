import tkinter as tk

root = tk.Tk()
pw = tk.PanedWindow(root, orient=tk.HORIZONTAL)
pw.pack(fill=tk.BOTH, expand=True)

frame = tk.Frame(pw)
text = tk.Text(frame, wrap="word")
scroll = tk.Scrollbar(frame, command=text.yview)
text.config(yscrollcommand=scroll.set)

text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
pw.add(frame)

pw.add(tk.Label(pw, text="Right Pane"))

root.mainloop()
