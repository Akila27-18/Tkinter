import tkinter as tk

# Color mapping for each arrow key
DIRECTION_COLORS = {
    'Left': 'lightblue',
    'Right': 'lightgreen',
    'Up': 'lightyellow',
    'Down': 'lightcoral'
}

def update_color(event):
    key = event.keysym

    if key in DIRECTION_COLORS:
        color = DIRECTION_COLORS[key]
        color_frame.config(bg=color)
        color_label.config(text=f"Current Color: {color}", bg=color)
    else:
        # Optional: handle invalid keys or log
        pass

# Main window setup
root = tk.Tk()
root.title("Dynamic Color Picker")
root.geometry("400x300")

# Frame to display background color
color_frame = tk.Frame(root, width=300, height=200, bg='white', relief='ridge', borderwidth=2)
color_frame.pack(pady=40)

# Label to show current color name
color_label = tk.Label(root, text="Press Arrow Keys to Change Color", font=("Arial", 12))
color_label.pack()

# Bind arrow keys to function
root.bind("<Left>", update_color)
root.bind("<Right>", update_color)
root.bind("<Up>", update_color)
root.bind("<Down>", update_color)

# Start GUI loop
root.mainloop()
