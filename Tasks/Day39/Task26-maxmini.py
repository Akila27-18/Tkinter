import tkinter as tk

root = tk.Tk()
root.title("Start Maximized")

# Start maximized (Windows/Linux: 'zoomed', macOS may not support this)
root.state('zoomed')

tk.Label(root, text="Window started maximized").pack(pady=50)
root.mainloop()

# import tkinter as tk

# root = tk.Tk()
# root.title("Start Minimized")

# # Start minimized
# root.iconify()

# tk.Label(root, text="Window started minimized").pack(pady=50)
# root.mainloop()

