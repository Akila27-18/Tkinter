import tkinter as tk

root = tk.Tk()
root.title("Click to Show Coordinates")
root.geometry("600x500")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack(pady=10)

def show_coordinates(event):
    x, y = event.x, event.y
    # Display coordinates near the clicked point
    canvas.create_text(x + 40, y, text=f"({x}, {y})", fill="black", font=("Arial", 10))

# Bind left click to show coordinates
canvas.bind("<Button-1>", show_coordinates)

root.mainloop()
