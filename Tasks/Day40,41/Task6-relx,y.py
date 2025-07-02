import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Place Example")
root.geometry("300x200")

# Label at fixed position (50, 50)
label1 = tk.Label(root, text="Top Left", bg="lightblue")
label1.place(x=50, y=50)

# Label centered using relx/rely
label2 = tk.Label(root, text="Centered", bg="lightgreen")
label2.place(relx=0.5, rely=0.5, anchor='center')

# Start the Tkinter event loop
root.mainloop()
