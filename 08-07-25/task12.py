import tkinter as tk

root = tk.Tk()
root.title("Login")

login_frame = tk.Frame(root, padx=20, pady=20)
login_frame.pack()

tk.Label(login_frame, text="Username:").grid(row=0, column=0)
tk.Entry(login_frame).grid(row=0, column=1)
tk.Label(login_frame, text="Password:").grid(row=1, column=0)
tk.Entry(login_frame, show="*").grid(row=1, column=1)
tk.Button(login_frame, text="Login").grid(row=2, columnspan=2, pady=10)

root.mainloop()
