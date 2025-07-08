import tkinter as tk
from tkinter import messagebox

def submit_form():
    if messagebox.askyesno("Confirm", "Do you want to submit the data?"):
        print("Data submitted!")

root = tk.Tk()

tk.Label(root, text="Name:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Submit", command=submit_form).pack(pady=10)
root.mainloop()
