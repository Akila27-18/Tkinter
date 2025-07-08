import tkinter as tk

def show_result():
    name = entry.get()
    result_label.config(text=f"Hello, {name}!")

root = tk.Tk()

form_frame = tk.Frame(root)
form_frame.pack(side="left", padx=10, pady=10)

result_frame = tk.Frame(root)
result_frame.pack(side="right", padx=10, pady=10)

tk.Label(form_frame, text="Enter Name:").pack()
entry = tk.Entry(form_frame)
entry.pack()
tk.Button(form_frame, text="Submit", command=show_result).pack()

result_label = tk.Label(result_frame, text="Result will appear here.")
result_label.pack()

root.mainloop()
