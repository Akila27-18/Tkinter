import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Diagonal Animation")
root.geometry("600x500")

# Create canvas
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack(pady=10)

# Create a ball (oval) object
ball = canvas.create_oval(10, 10, 40, 40, fill="purple")

# Diagonal movement speed
dx = 3
dy = 2

# Animation control
animation_running = True

def animate_diagonal():
    global dx, dy
    if not animation_running:
        return

    # Move diagonally
    canvas.move(ball, dx, dy)

    # Get current position
    x1, y1, x2, y2 = canvas.coords(ball)

    # Bounce off walls
    if x1 <= 0 or x2 >= 500:
        dx *= -1
    if y1 <= 0 or y2 >= 400:
        dy *= -1

    # Call this function again after 20 ms
    root.after(20, animate_diagonal)

def start():
    global animation_running
    if not animation_running:
        animation_running = True
        animate_diagonal()

def stop():
    global animation_running
    animation_running = False

# Start/Stop buttons
control_frame = tk.Frame(root)
control_frame.pack()

tk.Button(control_frame, text="▶ Start", command=start).pack(side=tk.LEFT, padx=10)
tk.Button(control_frame, text="⏹ Stop", command=stop).pack(side=tk.LEFT, padx=10)

# Start animation automatically
animate_diagonal()

root.mainloop()
