import tkinter as tk

def open_dialog():
    dialog = tk.Toplevel(root)
    dialog.title("Enter Name")

    tk.Label(dialog, text="Name:").pack(padx=10, pady=5)
    tk.Entry(dialog).pack(padx=10, pady=5)
    tk.Button(dialog, text="OK", command=dialog.destroy).pack(pady=10)

root = tk.Tk()
tk.Button(root, text="Open Dialog", command=open_dialog).pack(pady=20)
root.mainloop()
