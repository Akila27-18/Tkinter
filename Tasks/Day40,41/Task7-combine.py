# import tkinter as tk

# root = tk.Tk()
# root.title("Mixed Geometry Example")
# root.geometry("300x150")

# # This label uses pack()
# title_label = tk.Label(root, text="Login Form", font=("Arial", 16))
# title_label.pack(pady=10)

# # These use grid() — but in the SAME root, which causes an error
# username_label = tk.Label(root, text="Username:")
# username_entry = tk.Entry(root)

# # This will raise an error when run!
# username_label.grid(row=1, column=0, padx=10, pady=5)
# username_entry.grid(row=1, column=1, padx=10, pady=5)

# root.mainloop()

# To avoid the error, use different geometry managers in different containers

import tkinter as tk

root = tk.Tk()
root.title("Proper Mixed Geometry")
root.geometry("300x150")

# Title using pack()
title_label = tk.Label(root, text="Login Form", font=("Arial", 16))
title_label.pack(pady=10)

# Frame to hold the form (uses grid)
form_frame = tk.Frame(root)
form_frame.pack()

username_label = tk.Label(form_frame, text="Username:")
username_entry = tk.Entry(form_frame)

username_label.grid(row=0, column=0, padx=10, pady=5)
username_entry.grid(row=0, column=1, padx=10, pady=5)

root.mainloop()
