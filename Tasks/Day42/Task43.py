import tkinter as tk

def show_value():
    value = spin.get()
    print("Selected value:", value)

root = tk.Tk()
root.title("Spinbox Value Example")

# Create Spinbox
spin = tk.Spinbox(root, from_=1, to=10)
spin.pack(padx=10, pady=10)

# Button to get Spinbox value
btn = tk.Button(root, text="Get Value", command=show_value)
btn.pack(pady=10)

root.mainloop()
