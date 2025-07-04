import tkinter as tk

root = tk.Tk()
root.title("Canvas Animation Examples")
root.geometry("600x500")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack(pady=10)

# Create shapes
rect = canvas.create_rectangle(10, 50, 60, 100, fill="blue")       # Task 1


# Velocities
circle_dx, circle_dy = 3, 2
slow_dx = 1
diag_dx, diag_dy = 2, 2
animation_running = True

def animate():
    if not animation_running:
        return

    # Task 1: Move rect (left to right)
    canvas.move(rect, 2, 0)
    x1, _, x2, _ = canvas.coords(rect)
    if x2 > 500:
        canvas.coords(rect, 10, 50, 60, 100)
 # Repeat animation every 20 ms
    root.after(20, animate)
    
# Start animation initially
animate()
root.mainloop()
