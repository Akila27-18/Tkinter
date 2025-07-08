import tkinter as tk

def open_dialog():
    def submit():
        print("Submitted:", entry.get())
        dialog.destroy()

    def cancel():
        print("Cancelled")
        dialog.destroy()

    dialog = tk.Toplevel(root)
    dialog.title("User Input")

    tk.Label(dialog, text="Enter data:").pack(padx=10, pady=5)
    entry = tk.Entry(dialog)
    entry.pack(padx=10, pady=5)

    btn_frame = tk.Frame(dialog)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Submit", command=submit).pack(side="left", padx=5)
    tk.Button(btn_frame, text="Cancel", command=cancel).pack(side="left", padx=5)

root = tk.Tk()
tk.Button(root, text="Open Dialog", command=open_dialog).pack(pady=20)
root.mainloop()
