import tkinter as tk

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_grade.delete(0, tk.END)
    lbl_status.config(text="Fields Cleared", fg="blue")

root = tk.Tk()
root.title("Clear Form")

tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Label(root, text="Age:").grid(row=1, column=0)
tk.Label(root, text="Grade:").grid(row=2, column=0)

entry_name = tk.Entry(root)
entry_age = tk.Entry(root)
entry_grade = tk.Entry(root)

entry_name.grid(row=0, column=1)
entry_age.grid(row=1, column=1)
entry_grade.grid(row=2, column=1)

tk.Button(root, text="Clear", command=clear_fields).grid(row=3, column=0, columnspan=2)

lbl_status = tk.Label(root, text="")
lbl_status.grid(row=4, column=0, columnspan=2)

root.mainloop()
