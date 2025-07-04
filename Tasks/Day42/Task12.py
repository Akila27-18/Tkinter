import tkinter as tk

root = tk.Tk()
root.title("Canvas Animation Examples")
root.geometry("600x500")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack(pady=10)

# Create shapes

circle = canvas.create_oval(100, 150, 150, 200, fill="red")        # Task 2


# Velocities
circle_dx, circle_dy = 3, 2
slow_dx = 1
diag_dx, diag_dy = 2, 2
animation_running = True

def animate():
    if not animation_running:
        return

 

    # Task 2: Bounce circle
    global circle_dx, circle_dy
    x1, y1, x2, y2 = canvas.coords(circle)
    if x1 <= 0 or x2 >= 500:
        circle_dx *= -1
    if y1 <= 0 or y2 >= 400:
        circle_dy *= -1
    canvas.move(circle, circle_dx, circle_dy)

   
 # Repeat animation every 20 ms
    root.after(20, animate)


# Start animation initially
animate()
root.mainloop()
