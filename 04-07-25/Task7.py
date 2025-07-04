import tkinter as tk

# Global variables
running = False
rect = None
speed = 50  # Default delay in milliseconds
dx, dy = 5, 0  # Horizontal movement

def move():
    global running
    if running:
        canvas.move(rect, dx, dy)
        x1, y1, x2, y2 = canvas.coords(rect)
        label_coords.config(text=f"X: {int(x1)}, Y: {int(y1)}")

        # If rectangle hits right edge, reset to left
        if x2 >= canvas.winfo_width():
            canvas.move(rect, -canvas.winfo_width(), 0)
        root.after(speed, move)

def start_animation():
    global running, speed
    running = True
    speed = int(spin_speed.get())
    move()

def stop_animation():
    global running
    running = False

# Main window
root = tk.Tk()
root.title("Animated Moving Object")
root.geometry("500x300")

# Canvas
canvas = tk.Canvas(root, width=400, height=150, bg="lightblue")
canvas.pack(pady=10)
rect = canvas.create_rectangle(10, 60, 60, 100, fill="red")

# Controls Frame
frame_controls = tk.Frame(root)
frame_controls.pack(pady=10)

# Speed Spinbox
tk.Label(frame_controls, text="Speed (ms):").pack(side=tk.LEFT)
spin_speed = tk.Spinbox(frame_controls, from_=10, to=1000, increment=10, width=5)
spin_speed.pack(side=tk.LEFT)
spin_speed.delete(0, tk.END)
spin_speed.insert(0, str(speed))

# Start Button
btn_start = tk.Button(frame_controls, text="Start", command=start_animation, bg="green", fg="white")
btn_start.pack(side=tk.LEFT, padx=5)

# Stop Button
btn_stop = tk.Button(frame_controls, text="Stop", command=stop_animation, bg="red", fg="white")
btn_stop.pack(side=tk.LEFT, padx=5)

# Label for Coordinates
label_coords = tk.Label(root, text="X: 0, Y: 0", font=("Arial", 12))
label_coords.pack()

root.mainloop()
