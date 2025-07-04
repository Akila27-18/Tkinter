import tkinter as tk
from tkinter import ttk, filedialog, simpledialog, messagebox
from PIL import Image, ImageTk
import os

# Supported file types
IMAGE_TYPES = {
    "All": (".jpg", ".jpeg", ".png"),
    "JPG": (".jpg", ".jpeg"),
    "PNG": (".png",)
}

# Directory to scan (change this if needed)
IMAGE_DIR = os.getcwd()

# Tkinter app
root = tk.Tk()
root.title("Photo Gallery Viewer")
root.geometry("800x500")

# ---- Widgets Setup ----

# Filter Combobox
filter_var = tk.StringVar()
filter_combo = ttk.Combobox(root, textvariable=filter_var, values=list(IMAGE_TYPES.keys()), state="readonly")
filter_combo.set("All")
filter_combo.pack(pady=5)

# Frame for Listbox + Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

img_listbox = tk.Listbox(list_frame, height=25, width=40, yscrollcommand=scrollbar.set)
img_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar.config(command=img_listbox.yview)

# Canvas for image preview
canvas = tk.Canvas(root, width=500, height=400, bg="lightgray")
canvas.pack(pady=10)

# ---- Image Management ----

image_files = []
current_image = None  # Reference to displayed image (to prevent garbage collection)

def load_images():
    img_listbox.delete(0, tk.END)
    selected_type = filter_var.get()
    extensions = IMAGE_TYPES[selected_type]

    global image_files
    image_files = [f for f in os.listdir(IMAGE_DIR)
                   if f.lower().endswith(extensions) and os.path.isfile(os.path.join(IMAGE_DIR, f))]
    
    for img in image_files:
        img_listbox.insert(tk.END, img)

def show_selected_image(event=None):
    selected = img_listbox.curselection()
    if not selected:
        return
    filename = img_listbox.get(selected[0])
    path = os.path.join(IMAGE_DIR, filename)

    try:
        img = Image.open(path)
        img.thumbnail((500, 400))
        img_tk = ImageTk.PhotoImage(img)

        canvas.delete("all")
        canvas.create_image(250, 200, image=img_tk)
        global current_image
        current_image = img_tk  # Keep reference
    except Exception as e:
        messagebox.showerror("Error", f"Unable to open image:\n{e}")

def delete_image():
    selected = img_listbox.curselection()
    if not selected:
        return
    filename = img_listbox.get(selected[0])
    path = os.path.join(IMAGE_DIR, filename)

    confirm = messagebox.askyesno("Delete", f"Delete {filename}?")
    if confirm:
        try:
            os.remove(path)
            load_images()
            canvas.delete("all")
        except Exception as e:
            messagebox.showerror("Error", f"Unable to delete image:\n{e}")

def rename_image():
    selected = img_listbox.curselection()
    if not selected:
        return
    old_name = img_listbox.get(selected[0])
    old_path = os.path.join(IMAGE_DIR, old_name)

    new_name = simpledialog.askstring("Rename", "Enter new file name (with extension):", initialvalue=old_name)
    if new_name:
        new_path = os.path.join(IMAGE_DIR, new_name)
        try:
            os.rename(old_path, new_path)
            load_images()
        except Exception as e:
            messagebox.showerror("Error", f"Unable to rename file:\n{e}")

# ---- Buttons ----
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Delete Image", command=delete_image).pack(side=tk.LEFT, padx=10)
tk.Button(btn_frame, text="Rename Image", command=rename_image).pack(side=tk.LEFT, padx=10)

# ---- Bindings ----
img_listbox.bind("<<ListboxSelect>>", show_selected_image)
filter_combo.bind("<<ComboboxSelected>>", lambda e: load_images())

# Initial load
load_images()

root.mainloop()
