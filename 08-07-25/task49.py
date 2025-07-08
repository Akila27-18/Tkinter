import tkinter as tk

def open_dialog():
    dialog = tk.Toplevel(root)
    dialog.title("Centered Dialog")
    dialog.geometry("250x120")

    # Center it manually
    dialog.update_idletasks()
    w = dialog.winfo_width()
    h = dialog.winfo_height()
    ws = dialog.winfo_screenwidth()
    hs = dialog.winfo_screenheight()
    x = (ws // 2) - (w // 2)
    y = (hs // 2) - (h // 2)
    dialog.geometry(f"+{x}+{y}")

    tk.Label(dialog, text="This dialog is centered").pack(pady=30)

root = tk.Tk()
tk.Button(root, text="Show Dialog", command=open_dialog).pack(pady=20)
root.mainloop()
