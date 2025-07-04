import tkinter as tk

root = tk.Tk()
root.title("Canvas Animation Examples")
root.geometry("600x500")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack(pady=10)

# Create shapes

slow_rect = canvas.create_rectangle(10, 250, 40, 280, fill="green")  # Task 3


# Velocities
circle_dx, circle_dy = 3, 2
slow_dx = 1
diag_dx, diag_dy = 2, 2
animation_running = True

def animate():
    if not animation_running:
        return
    

    # Task 3: Move slow rectangle at different speed
    canvas.move(slow_rect, slow_dx, 0)
    if canvas.coords(slow_rect)[2] > 500:
        canvas.coords(slow_rect, 10, 250, 40, 280)
 # Repeat animation every 20 ms
    root.after(20, animate)
    


# Start animation initially
animate()
root.mainloop()
