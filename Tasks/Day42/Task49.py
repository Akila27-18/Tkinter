import tkinter as tk

root = tk.Tk()
root.title("Animation Speed Control")

# Create Canvas
canvas = tk.Canvas(root, width=400, height=200, bg="white")
canvas.pack(pady=10)

# Create a moving object (circle)
ball = canvas.create_oval(10, 80, 30, 100, fill="blue")

# Variable to hold speed (in milliseconds)
speed_var = tk.IntVar(value=50)

# Spinbox to control speed (delay between moves)
spinbox = tk.Spinbox(root, from_=10, to=500, increment=10, textvariable=speed_var)
spinbox.pack(pady=5)
tk.Label(root, text="Speed (lower is faster)").pack()

# Animation function
x_velocity = 5
def animate():
    canvas.move(ball, x_velocity, 0)
    pos = canvas.coords(ball)
    if pos[2] >= 400 or pos[0] <= 0:
        global x_velocity
        x_velocity = -x_velocity
    delay = speed_var.get()
    root.after(delay, animate)

animate()  # Start animation

root.mainloop()
