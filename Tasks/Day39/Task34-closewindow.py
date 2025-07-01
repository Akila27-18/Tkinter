import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Close Window Example")
root.geometry("250x150")

# Close function
def close_window():
    root.destroy()

# Close Button
close_btn = tk.Button(root, text="Close Window", command=close_window)
close_btn.pack(pady=40)

root.mainloop()
