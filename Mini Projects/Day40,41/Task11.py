import tkinter as tk

def change_color(color):
    root.config(bg=color)
    color_label.config(text=f"Selected Color: {color}", bg=color)

# --- GUI Setup ---
root = tk.Tk()
root.title("Color Picker")
root.geometry("400x200")

# Color display label
color_label = tk.Label(root, text="Selected Color: None", font=("Arial", 14))
color_label.pack(pady=20)

# Frame to hold color buttons
button_frame = tk.Frame(root)
button_frame.pack()

# List of colors
colors = ["red", "green", "blue", "yellow", "orange", "purple"]

# Create color buttons
for color in colors:
    tk.Button(button_frame, text=color.capitalize(), bg=color, fg="white",
              width=10, command=lambda c=color: change_color(c)).pack(side="left", padx=5)

root.mainloop()
