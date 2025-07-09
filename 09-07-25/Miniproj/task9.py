import tkinter as tk

def on_enter_label(event):
    event.widget.config(fg='blue', bg='lightgray')

def on_leave_label(event):
    event.widget.config(fg='black', bg='SystemButtonFace')

def on_enter_button(event):
    event.widget.config(bg='darkgreen', fg='white')

def on_leave_button(event):
    event.widget.config(bg='SystemButtonFace', fg='black')

# Main window
root = tk.Tk()
root.title("Mouse Hover UI Effects")
root.geometry("300x200")

# Label with hover effect
hover_label = tk.Label(root, text="Hover Over Me (Label)", font=("Arial", 12), pady=10)
hover_label.pack(pady=20)
hover_label.bind("<Enter>", on_enter_label)
hover_label.bind("<Leave>", on_leave_label)

# Button with hover effect
hover_button = tk.Button(root, text="Hover Over Me (Button)", font=("Arial", 12), padx=10)
hover_button.pack(pady=10)
hover_button.bind("<Enter>", on_enter_button)
hover_button.bind("<Leave>", on_leave_button)

root.mainloop()
