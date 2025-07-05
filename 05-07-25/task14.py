import tkinter as tk
from tkinter import ttk
from tkinter import font

def apply_formatting(style):
    text = input_text.get("1.0", tk.END).strip()
    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)

    # Clear previous tags
    output_text.tag_delete("bold")
    output_text.tag_delete("italic")
    output_text.tag_delete("font_size")

    output_text.insert("1.0", text)

    # Apply formatting tags
    size = int(font_size_combo.get())
    output_text.tag_add("font_size", "1.0", "end")
    output_text.tag_config("font_size", font=("Arial", size))

    if style == "bold":
        output_text.tag_add("bold", "1.0", "end")
        output_text.tag_config("bold", font=("Arial", size, "bold"))

    elif style == "italic":
        output_text.tag_add("italic", "1.0", "end")
        output_text.tag_config("italic", font=("Arial", size, "italic"))

    elif style == "both":
        output_text.tag_add("bold", "1.0", "end")
        output_text.tag_config("bold", font=("Arial", size, "bold italic"))

    output_text.config(state="disabled")

# GUI Setup
root = tk.Tk()
root.title("Text Formatter")
root.geometry("600x400")

# Input Text Widget
tk.Label(root, text="Enter Text:").pack(anchor="w", padx=10, pady=(10, 0))
input_text = tk.Text(root, height=6, width=70)
input_text.pack(padx=10)

# Font size selector
size_frame = tk.Frame(root)
size_frame.pack(pady=5)

tk.Label(size_frame, text="Font Size:").pack(side="left")
font_size_combo = ttk.Combobox(size_frame, values=[10, 12, 14, 16, 18, 20], width=5)
font_size_combo.set("12")
font_size_combo.pack(side="left", padx=5)

# Formatting buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Bold", width=10, command=lambda: apply_formatting("bold")).pack(side="left", padx=5)
tk.Button(btn_frame, text="Italic", width=10, command=lambda: apply_formatting("italic")).pack(side="left", padx=5)
tk.Button(btn_frame, text="Bold + Italic", width=12, command=lambda: apply_formatting("both")).pack(side="left", padx=5)

# Output Text Widget
tk.Label(root, text="Formatted Output:").pack(anchor="w", padx=10, pady=(10, 0))
output_text = tk.Text(root, height=6, width=70, state="disabled")
output_text.pack(padx=10)

root.mainloop()
