import tkinter as tk

root = tk.Tk()
root.title("Hover to Change Shape Color")
root.geometry("600x500")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack(pady=10)

# Create a rectangle with a tag
rect = canvas.create_rectangle(100, 100, 200, 180, fill="skyblue", tags="hoverable")

# Create a circle with a tag
circle = canvas.create_oval(300, 150, 370, 220, fill="lightgreen", tags="hoverable")

# Hover in function
def on_enter(event):
    canvas.itemconfig("current", fill="orange")

# Hover out function
def on_leave(event):
    canvas.itemconfig("current", fill="skyblue" if canvas.type("current") == "rectangle" else "lightgreen")

# Bind hover events to tag
canvas.tag_bind("hoverable", "<Enter>", on_enter)
canvas.tag_bind("hoverable", "<Leave>", on_leave)

root.mainloop()
