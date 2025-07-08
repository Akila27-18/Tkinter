import tkinter as tk

root = tk.Tk()

pw_main = tk.PanedWindow(root, orient=tk.HORIZONTAL)
pw_main.pack(fill=tk.BOTH, expand=True)

left = tk.Label(pw_main, text="Left Pane", bg="lightblue")
pw_main.add(left)

pw_nested = tk.PanedWindow(pw_main, orient=tk.VERTICAL)
center = tk.Label(pw_nested, text="Top Center", bg="lightgreen")
bottom = tk.Label(pw_nested, text="Bottom Center", bg="lightyellow")

pw_nested.add(center)
pw_nested.add(bottom)

pw_main.add(pw_nested)

root.mainloop()
