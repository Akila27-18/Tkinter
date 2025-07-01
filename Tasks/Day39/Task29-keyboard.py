import tkinter as tk

def on_submit(event=None):  # `event` is optional for button and key binding
    text = entry.get()
    result_label.config(text=f"You entered: {text}")

# GUI setup
root = tk.Tk()
root.title("Button with Keyboard Shortcut")
root.geometry("300x150")

# Entry widget
entry = tk.Entry(root)
entry.pack(pady=10)

# Submit button
submit_btn = tk.Button(root, text="Submit", command=on_submit)
submit_btn.pack(pady=5)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Bind Enter key to on_submit function
root.bind('<Return>', on_submit)  # Enter key binding

root.mainloop()
