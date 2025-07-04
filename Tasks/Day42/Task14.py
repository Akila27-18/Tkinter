import tkinter as tk

root = tk.Tk()
root.title("Canvas Animation Examples")
root.geometry("600x500")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack(pady=10)

# Create shapes
rect = canvas.create_rectangle(10, 50, 60, 100, fill="blue")       # Task 1
circle = canvas.create_oval(100, 150, 150, 200, fill="red")        # Task 2
slow_rect = canvas.create_rectangle(10, 250, 40, 280, fill="green")  # Task 3
diagonal = canvas.create_oval(10, 300, 40, 330, fill="purple")     # Task 5

# Velocities
rect_dx = 2
circle_dx, circle_dy = 3, 2
slow_dx = 1
diag_dx, diag_dy = 2, 2

animation_running = True

def animate():
    if not animation_running:
        return

    # Task 1: Move rect (left to right)
    canvas.move(rect, rect_dx, 0)
    rx1, ry1, rx2, ry2 = canvas.coords(rect)
    if rx2 > 500:
        canvas.coords(rect, 10, 50, 60, 100)

    # Task 2: Circle bouncing
    global circle_dx, circle_dy
    cx1, cy1, cx2, cy2 = canvas.coords(circle)
    if cx1 <= 0 or cx2 >= 500:
        circle_dx *= -1
    if cy1 <= 0 or cy2 >= 400:
        circle_dy *= -1
    canvas.move(circle, circle_dx, circle_dy)

    # Task 3: Slow rectangle
    canvas.move(slow_rect, slow_dx, 0)
    if canvas.coords(slow_rect)[2] > 500:
        canvas.coords(slow_rect, 10, 250, 40, 280)

    # Task 5: Diagonal movement
    global diag_dx, diag_dy
    dx1, dy1, dx2, dy2 = canvas.coords(diagonal)
    if dx1 <= 0 or dx2 >= 500:
        diag_dx *= -1
    if dy1 <= 0 or dy2 >= 400:
        diag_dy *= -1
    canvas.move(diagonal, diag_dx, diag_dy)

    # Repeat animation
    root.after(20, animate)

def stop_animation():
    global animation_running
    animation_running = False

def start_animation():
    global animation_running
    if not animation_running:
        animation_running = True
        animate()

# Buttons for start/stop
btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Start Animation", command=start_animation).pack(side=tk.LEFT, padx=10)
tk.Button(btn_frame, text="Stop Animation", command=stop_animation).pack(side=tk.LEFT, padx=10)

# Start animation initially
animate()

root.mainloop()
