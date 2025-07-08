import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("800x600")

        self.image_path = None
        self.original_image = None
        self.display_image = None
        self.zoom_level = 1.0

        # ==== Menu Bar ====
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open_image)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu=menubar)

        # ==== Toolbar Frame ====
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#f0f0f0")
        open_btn = ttk.Button(toolbar, text="Open Image", command=self.open_image)
        zoom_in_btn = ttk.Button(toolbar, text="Zoom In", command=self.zoom_in)
        zoom_out_btn = ttk.Button(toolbar, text="Zoom Out", command=self.zoom_out)
        open_btn.pack(side=tk.LEFT, padx=5, pady=5)
        zoom_in_btn.pack(side=tk.LEFT, padx=5, pady=5)
        zoom_out_btn.pack(side=tk.LEFT, padx=5, pady=5)
        toolbar.pack(fill=tk.X)

        # ==== Canvas for Image Display ====
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    # ==== Image Operations ====
    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")])
        if file_path:
            try:
                self.original_image = Image.open(file_path)
                self.zoom_level = 1.0
                self.display_image_on_canvas()
                self.root.title(f"Image Viewer - {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Unable to open image.\n{e}")

    def display_image_on_canvas(self):
        if self.original_image:
            # Resize image based on zoom level
            width, height = self.original_image.size
            new_size = (int(width * self.zoom_level), int(height * self.zoom_level))
            resized_image = self.original_image.resize(new_size, Image.ANTIALIAS)
            self.display_image = ImageTk.PhotoImage(resized_image)

            self.canvas.delete("all")  # Clear previous image
            self.canvas.create_image(self.canvas.winfo_width()//2,
                                     self.canvas.winfo_height()//2,
                                     anchor=tk.CENTER,
                                     image=self.display_image)

    def zoom_in(self):
        if self.original_image:
            self.zoom_level *= 1.1
            self.display_image_on_canvas()

    def zoom_out(self):
        if self.original_image:
            self.zoom_level /= 1.1
            self.display_image_on_canvas()

# ==== Run App ====
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()
