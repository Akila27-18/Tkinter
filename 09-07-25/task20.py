# task20_tooltip_label.py
import tkinter as tk

def show_tooltip(e): tooltip.place(x=e.x_root - root.winfo_rootx(), y=e.y_root - root.winfo_rooty() + 20)
def hide_tooltip(e): tooltip.place_forget()

root = tk.Tk()
label = tk.Label(root, text="Hover for Info")
label.pack(pady=30)

tooltip = tk.Label(root, text="This is a tooltip", bg="yellow", relief="solid", bd=1)
label.bind("<Enter>", show_tooltip)
label.bind("<Leave>", hide_tooltip)
root.mainloop()
