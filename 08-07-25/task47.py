import tkinter as tk

def open_dialog():
    def submit():
        name = entry.get()
        label.config(text=f"Hello, {name}!")
        dialog.destroy()

    dialog = tk.Toplevel(root)
    dialog.title("Enter Name")
    entry = tk.Entry(dialog)
    entry.pack(padx=10, pady=10)
    tk.Button(dialog, text="Submit", command=submit).pack(pady=5)

root = tk.Tk()
label = tk.Label(root, text="Name will appear here")
label.pack(pady=10)
tk.Button(root, text="Enter Name", command=open_dialog).pack()
root.mainloop()
