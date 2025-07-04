import tkinter as tk
from tkinter import ttk

class ColorPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Picker App")

        # Color selection
        color_frame = tk.Frame(root)
        color_frame.pack(pady=5)

        tk.Label(color_frame, text="Select Color:").pack(side=tk.LEFT, padx=5)
        self.color_var = tk.StringVar()
        self.color_cb = ttk.Combobox(color_frame, textvariable=self.color_var,
                                     values=["Red", "Green", "Blue", "Yellow", "Orange", "Purple", "Black"], state="readonly")
        self.color_cb.pack(side=tk.LEFT)
        self.color_cb.set("Red")

        # Canvas
        self.canvas = tk.Canvas(root, width=500, height=400, bg="white")
        self.canvas.pack(pady=10)

        # Status label
        self.status_label = tk.Label(root, text="Click on canvas to paint")
        self.status_label.pack()

        # Grid setup
        self.rect_size = 20
        self.rect_ids = {}  # (row, col) -> rect_id

        rows = self.canvas.winfo_reqheight() // self.rect_size
        cols = self.canvas.winfo_reqwidth() // self.rect_size

        for i in range(rows):
            for j in range(cols):
                x1 = j * self.rect_size
                y1 = i * self.rect_size
                x2 = x1 + self.rect_size
                y2 = y1 + self.rect_size
                rect_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="gray")
                self.rect_ids[(i, j)] = rect_id

        # Bind events
        self.canvas.bind("<Button-1>", self.paint_cell)
        self.canvas.bind("<Button-3>", self.erase_cell)

    def get_cell(self, x, y):
        row = y // self.rect_size
        col = x // self.rect_size
        return row, col

    def paint_cell(self, event):
        color = self.color_var.get().lower()
        row, col = self.get_cell(event.x, event.y)
        rect_id = self.rect_ids.get((row, col))
        if rect_id:
            self.canvas.itemconfig(rect_id, fill=color)
            self.status_label.config(text=f"Painted ({col}, {row}) with {color.capitalize()}")

    def erase_cell(self, event):
        row, col = self.get_cell(event.x, event.y)
        rect_id = self.rect_ids.get((row, col))
        if rect_id:
            self.canvas.itemconfig(rect_id, fill="white")
            self.status_label.config(text=f"Erased color at ({col}, {row})")

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPickerApp(root)
    root.mainloop()
