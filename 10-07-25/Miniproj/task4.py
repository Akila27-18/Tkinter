import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

def select_folder():
    folder = filedialog.askdirectory(title="Select Image Folder")
    if not folder:
        return

    image_list.clear()
    listbox.delete(0, tk.END)
    for file in os.listdir(folder):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_list.append(os.path.join(folder, file))
            listbox.insert(tk.END, file)

def show_image(event):
    if not listbox.curselection():
        return

    index = listbox.curselection()[0]
    image_path = image_list[index]

    try:
        img = Image.open(image_path)
        img.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(img)
        canvas.delete("all")
        canvas.image = photo  # Keep reference
        canvas.create_image(150, 150, image=photo)

        dimensions = f"{img.width} x {img.height} pixels"
        label_info.config(text=f"Image: {os.path.basename(image_path)}\nSize: {dimensions}")
    except Exception as e:
        messagebox.showerror("Error", f"Unable to load image:\n{e}")

# GUI Setup
root = tk.Tk()
root.title("Image Organizer App")
root.geometry("600x500")

image_list = []

tk.Button(root, text="Select Image Folder", command=select_folder).pack(pady=10)

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

listbox = tk.Listbox(frame, width=30)
listbox.pack(side=tk.LEFT, fill=tk.Y, padx=10)
listbox.bind("<<ListboxSelect>>", show_image)

canvas = tk.Canvas(frame, width=300, height=300, bg="lightgray")
canvas.pack(side=tk.LEFT, padx=10)

label_info = tk.Label(root, text="Select an image to view details.", font=("Arial", 10))
label_info.pack(pady=10)

root.mainloop()
