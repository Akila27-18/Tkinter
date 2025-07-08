import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

frame = tk.Frame(root, bg="lightblue", width=150, height=100)
frame.place(x=100, y=100)

tk.Label(frame, text="Placed Frame").pack()

root.mainloop()
