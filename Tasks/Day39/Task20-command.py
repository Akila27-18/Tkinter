import tkinter as tk

def say_hello():
    print("Button was clicked! Hello from Tkinter!")

# Main window
root = tk.Tk()
root.title("Button Command Example")
root.geometry("250x150")

# Button with command
btn = tk.Button(root, text="Click Me", command=say_hello)
btn.pack(pady=40)

root.mainloop()
