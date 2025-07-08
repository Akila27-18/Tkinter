import tkinter as tk

def toggle_toolbar():
    if toolbar.winfo_ismapped():
        toolbar.pack_forget()
        toggle_btn.config(text="Show Toolbar")
    else:
        toolbar.pack(side="top", fill="x")
        toggle_btn.config(text="Hide Toolbar")

root = tk.Tk()

toolbar = tk.Frame(root, bg="lightgray")
tk.Button(toolbar, text="Open").pack(side="left", padx=2)
tk.Button(toolbar, text="Save").pack(side="left", padx=2)
toolbar.pack(side="top", fill="x")

toggle_btn = tk.Button(root, text="Hide Toolbar", command=toggle_toolbar)
toggle_btn.pack(pady=10)

root.mainloop()
