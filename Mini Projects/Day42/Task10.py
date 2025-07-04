import tkinter as tk
from tkinter import ttk, font, filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk, EpsImagePlugin
EpsImagePlugin.gs_windows_binary = r"C:\Program Files\gs\gs10.02.1\bin\gswin64c.exe"

# EpsImagePlugin.gs_windows_binary = r"gswin64c"  # Required if ghostscript is used for EPS to PNG

# Create main window
root = tk.Tk()
root.title("Font Preview Tool")

# Font family selector
font_var = tk.StringVar()
font_families = list(font.families())
font_families.sort()
font_combo = ttk.Combobox(root, textvariable=font_var, values=font_families, state="readonly", width=30)
font_combo.set("Arial")
font_combo.pack(pady=5)

# Font size spinbox
size_var = tk.IntVar(value=20)
size_spin = tk.Spinbox(root, from_=8, to=72, textvariable=size_var, width=5)
size_spin.pack(pady=5)

# Canvas for preview
canvas = tk.Canvas(root, width=500, height=200, bg="white")
canvas.pack(pady=10)

preview_text = "The quick brown fox jumps over the lazy dog"

# Draw preview text on canvas
def update_preview(*args):
    canvas.delete("all")
    family = font_var.get()
    size = size_var.get()
    try:
        fnt = (family, size)
        canvas.create_text(250, 100, text=preview_text, font=fnt, fill="black", tags="text")
    except tk.TclError:
        pass

# Save as PNG
def save_as_png():
    # Save Canvas as EPS
    canvas.update()
    canvas.postscript(file="preview.eps", colormode='color')

    # Convert EPS to PNG using Pillow
    img = Image.open("preview.eps")
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                              filetypes=[("PNG Image", "*.png")],
                                              title="Save Preview As")
    if save_path:
        img.save(save_path, "PNG")

# Save Button
save_btn = tk.Button(root, text="Save as PNG", command=save_as_png)
save_btn.pack(pady=5)

# Bind events
font_combo.bind("<<ComboboxSelected>>", update_preview)
size_spin.bind("<KeyRelease>", update_preview)
size_spin.bind("<ButtonRelease-1>", update_preview)

# Initial draw
update_preview()

root.mainloop()
