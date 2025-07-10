import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if path:
        img = Image.open(path)
        img.thumbnail((400, 400))
        img_tk = ImageTk.PhotoImage(img)
        canvas.image = img_tk  # Store reference
        canvas.create_image(200, 200, image=img_tk)

root = tk.Tk()
root.title("Open and Display Image")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

tk.Button(root, text="Open Image", command=open_image).pack(pady=10)

root.mainloop()
