import tkinter as tk

root = tk.Tk()
pw = tk.PanedWindow(root, orient=tk.HORIZONTAL)
pw.pack(fill=tk.BOTH, expand=True)

left_frame = tk.Frame(pw, bg="lightgray", width=100)
center_frame = tk.Frame(pw, bg="white", width=200)
right_frame = tk.Frame(pw, bg="lightblue", width=100)

tk.Label(left_frame, text="Navigation").pack(pady=10)
tk.Text(center_frame).pack(fill=tk.BOTH, expand=True)
tk.Label(right_frame, text="Details").pack(pady=10)

pw.add(left_frame)
pw.add(center_frame)
pw.add(right_frame)

root.mainloop()
