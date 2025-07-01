import tkinter as tk

# Main window
root = tk.Tk()
root.title("Multiple Frames Example")
root.geometry("400x300")

# ----- Frame 1 -----
frame1 = tk.Frame(root, bg="lightyellow", bd=2, relief=tk.RIDGE)
frame1.pack(padx=10, pady=10, fill="x")

tk.Label(frame1, text="Frame 1: User Info", bg="lightyellow", font=("Arial", 12, "bold")).pack(pady=5)
tk.Label(frame1, text="Name:").pack(side="left", padx=5)
tk.Entry(frame1, width=20).pack(side="left", padx=5)

# ----- Frame 2 -----
frame2 = tk.Frame(root, bg="lightgray", bd=2, relief=tk.GROOVE)
frame2.pack(padx=10, pady=10, fill="both", expand=True)

tk.Label(frame2, text="Frame 2: Actions", bg="lightgray", font=("Arial", 12, "bold")).pack(pady=5)
tk.Button(frame2, text="Submit").pack(pady=5)
tk.Button(frame2, text="Reset").pack(pady=5)

# Run the app
root.mainloop()
