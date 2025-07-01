import tkinter as tk

root = tk.Tk()
root.title("Frame Border and Relief")
root.geometry("300x200")

# Create a styled Frame
frame = tk.Frame(root, 
                 bd=3,                # Border width
                 relief=tk.SUNKEN,    # Relief style: SUNKEN, RAISED, GROOVE, RIDGE, FLAT
                 bg="lightgray")
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Add a label inside the frame for demo
tk.Label(frame, text="This is a sunken frame!", bg="lightgray").pack(pady=20)

root.mainloop()
