import tkinter as tk
from tkinter import ttk
import json

class CanvasWhiteboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Whiteboard with Shapes")

        # Main canvas
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack(pady=5)

        # Frame for controls
        control_frame = tk.Frame(root)
        control_frame.pack()

        # Shape Listbox
        tk.Label(control_frame, text="Shapes:").grid(row=0, column=0)
        self.shape_listbox = tk.Listbox(control_frame, height=4, exportselection=False)
        for shape in ["Circle", "Rectangle"]:
            self.shape_listbox.insert(tk.END, shape)
        self.shape_listbox.grid(row=0, column=1, padx=5)
        self.shape_listbox.selection_set(0)

        # Color Combobox
        tk.Label(control_frame, text="Color:").grid(row=0, column=2)
        self.color_var = tk.StringVar()
        self.color_cb = ttk.Combobox(control_frame, textvariable=self.color_var, 
                                     values=["Red", "Green", "Blue", "Black", "Orange"], state="readonly", width=10)
        self.color_cb.grid(row=0, column=3, padx=5)
        self.color_cb.set("Black")

        # Action Buttons
        tk.Button(control_frame, text="Delete Selected", command=self.delete_selected).grid(row=0, column=4, padx=5)
        tk.Button(control_frame, text="Undo", command=self.undo).grid(row=0, column=5, padx=5)
        tk.Button(control_frame, text="Redo", command=self.redo).grid(row=0, column=6, padx=5)
        tk.Button(control_frame, text="Save to File", command=self.save_to_file).grid(row=0, column=7, padx=5)

        # Shape tracking
        self.shape_objects = []  # List of (canvas_id, description)
        self.undo_stack = []
        self.redo_stack = []

        # Bind canvas click
        self.canvas.bind("<Button-1>", self.draw_shape)

    def draw_shape(self, event):
        shape = self.shape_listbox.get(tk.ACTIVE)
        color = self.color_var.get().lower()
        size = 50
        x, y = event.x, event.y

        if shape == "Circle":
            item = self.canvas.create_oval(x, y, x+size, y+size, fill=color, outline=color)
        elif shape == "Rectangle":
            item = self.canvas.create_rectangle(x, y, x+size, y+size, fill=color, outline=color)

        desc = f"{shape} ({x},{y}) [{color}]"
        self.shape_objects.append((item, desc))
        self.redo_stack.clear()
        self.undo_stack.append(('draw', item))
        self.update_listbox()

    def update_listbox(self):
        self.shape_listbox.delete(0, tk.END)
        for _, desc in self.shape_objects:
            self.shape_listbox.insert(tk.END, desc)

    def delete_selected(self):
        index = self.shape_listbox.curselection()
        if not index:
            return
        index = index[0]
        item_id, _ = self.shape_objects.pop(index)
        self.canvas.delete(item_id)
        self.undo_stack.append(('delete', item_id))
        self.redo_stack.clear()
        self.update_listbox()

    def undo(self):
        if not self.undo_stack:
            return
        action, item = self.undo_stack.pop()
        if action == 'draw':
            for i, (obj_id, _) in enumerate(self.shape_objects):
                if obj_id == item:
                    self.shape_objects.pop(i)
                    break
            self.canvas.delete(item)
            self.redo_stack.append(('draw', item))
        elif action == 'delete':
            # Not full restore — just store ID to redo
            self.redo_stack.append(('delete', item))
        self.update_listbox()

    def redo(self):
        if not self.redo_stack:
            return
        action, item = self.redo_stack.pop()
        if action == 'draw':
            # We cannot redraw with just ID — skip unless stored
            pass
        elif action == 'delete':
            self.canvas.delete(item)
        self.update_listbox()

    def save_to_file(self):
        data = []
        for item_id, desc in self.shape_objects:
            coords = self.canvas.coords(item_id)
            shape_type = self.canvas.type(item_id)
            color = self.canvas.itemcget(item_id, "fill")
            data.append({
                "type": shape_type,
                "coords": coords,
                "color": color
            })
        with open("canvas_shapes.json", "w") as f:
            json.dump(data, f)
        print("Canvas saved to canvas_shapes.json")
def draw_shape(self, event):
    shape = self.shape_listbox.get(tk.ACTIVE)
    color = self.color_var.get().lower()
    size = 50
    x, y = event.x, event.y

    item = None  # Define item at the top

    if shape == "Circle":
        item = self.canvas.create_oval(x, y, x+size, y+size, fill=color, outline=color)
    elif shape == "Rectangle":
        item = self.canvas.create_rectangle(x, y, x+size, y+size, fill=color, outline=color)
    else:
        return  # Unknown shape selected — exit safely

    if item:  # Only append if a shape was drawn
        desc = f"{shape} ({x},{y}) [{color}]"
        self.shape_objects.append((item, desc))
        self.redo_stack.clear()
        self.undo_stack.append(('draw', item))
        self.update_listbox()

    

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = CanvasWhiteboard(root)
    root.mainloop()
