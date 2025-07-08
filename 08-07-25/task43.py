import tkinter as tk
from tkinter import messagebox

def confirm_action():
    result = messagebox.askquestion("Confirm", "Do you want to proceed?")
    if result == 'yes':
        print("User chose Yes")
    else:
        print("User chose No")

root = tk.Tk()
tk.Button(root, text="Ask Question", command=confirm_action).pack(pady=20)
root.mainloop()
