# task41_login_widget.py
import tkinter as tk

class LoginWidget(tk.Frame):
    def __init__(self, master, on_submit, **kwargs):
        super().__init__(master, **kwargs)
        self.username = tk.Entry(self)
        self.password = tk.Entry(self, show="*")
        tk.Label(self, text="Username:").pack()
        self.username.pack()
        tk.Label(self, text="Password:").pack()
        self.password.pack()
        tk.Button(self, text="Submit", command=lambda: on_submit(self.username.get(), self.password.get())).pack()

def submit(u, p): print(f"Login: {u}, Pass: {p}")

root = tk.Tk()
widget = LoginWidget(root, on_submit=submit)
widget.pack(pady=10)
root.mainloop()
