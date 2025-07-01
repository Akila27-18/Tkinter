import tkinter as tk

root = tk.Tk()
root.title("pack(side=...) Example")
root.geometry("300x150")

# Button on the left side
btn_left = tk.Button(root, text="Left")
btn_left.pack(side=tk.LEFT, padx=10, pady=10)

# Button on the right side
btn_right = tk.Button(root, text="Right")
btn_right.pack(side=tk.RIGHT, padx=10, pady=10)

# Button in the center (top by default)
btn_center = tk.Button(root, text="Top (default)")
btn_center.pack(pady=10)

root.mainloop()
