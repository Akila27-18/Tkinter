import tkinter as tk

class GridGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Grid Game")

        self.cell_size = 80
        self.rows = 5
        self.cols = 5
        self.marked_cells = {}

        # Canvas for grid
        self.canvas = tk.Canvas(root, width=self.cols * self.cell_size,
                                      height=self.rows * self.cell_size,
                                      bg="white")
        self.canvas.grid(row=0, column=0, padx=10, pady=10)
        self.draw_grid()

        # Bind cell click
        self.canvas.bind("<Button-1>", self.mark_cell)

        # Listbox with scrollbar
        log_frame = tk.Frame(root)
        log_frame.grid(row=0, column=1, sticky="ns")

        tk.Label(log_frame, text="Clicked Cells:").pack()
        self.listbox = tk.Listbox(log_frame, width=25, height=10)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar = tk.Scrollbar(log_frame, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Reset button
        self.reset_btn = tk.Button(root, text="Reset", command=self.reset)
        self.reset_btn.grid(row=1, column=0, columnspan=2, pady=10)

    def draw_grid(self):
        self.cell_rects = []
        for row in range(self.rows):
            row_rects = []
            for col in range(self.cols):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
                row_rects.append(rect)
            self.cell_rects.append(row_rects)

    def mark_cell(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size

        if row < self.rows and col < self.cols:
            rect = self.cell_rects[row][col]
            current_fill = self.canvas.itemcget(rect, "fill")

            if current_fill == "white":
                self.canvas.itemconfig(rect, fill="lightblue")
                self.listbox.insert(tk.END, f"Marked: Row {row+1}, Col {col+1}")
                self.marked_cells[(row, col)] = rect
            else:
                self.canvas.itemconfig(rect, fill="white")
                self.listbox.insert(tk.END, f"Unmarked: Row {row+1}, Col {col+1}")
                self.marked_cells.pop((row, col), None)

    def reset(self):
        for row in range(self.rows):
            for col in range(self.cols):
                rect = self.cell_rects[row][col]
                self.canvas.itemconfig(rect, fill="white")
        self.listbox.delete(0, tk.END)
        self.marked_cells.clear()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = GridGame(root)
    root.mainloop()
