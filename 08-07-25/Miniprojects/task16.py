import tkinter as tk

# Theme definitions
THEMES = {
    "Light": {
        "bg": "#FFFFFF",
        "fg": "#000000",
        "toolbar": "#E0E0E0",
        "button": "#F0F0F0",
        "frame": "#FAFAFA"
    },
    "Dark": {
        "bg": "#2E2E2E",
        "fg": "#FFFFFF",
        "toolbar": "#444444",
        "button": "#555555",
        "frame": "#3A3A3A"
    }
}

current_theme = "Light"

def apply_theme(theme_name):
    global current_theme
    current_theme = theme_name
    theme = THEMES[theme_name]

    root.config(bg=theme["bg"])
    toolbar.config(bg=theme["toolbar"])
    content_frame.config(bg=theme["frame"])
    theme_button.config(bg=theme["button"], fg=theme["fg"])
    label.config(bg=theme["frame"], fg=theme["fg"])

    menubar.config(bg=theme["toolbar"], fg=theme["fg"])
    view_menu.entryconfig(0, label="Light Theme")
    view_menu.entryconfig(1, label="Dark Theme")

def toggle_theme():
    new_theme = "Dark" if current_theme == "Light" else "Light"
    apply_theme(new_theme)

# Main window
root = tk.Tk()
root.title("Theme Switcher App")
root.geometry("600x400")

# Menu bar
menubar = tk.Menu(root)
view_menu = tk.Menu(menubar, tearoff=0)
view_menu.add_command(label="Light Theme", command=lambda: apply_theme("Light"))
view_menu.add_command(label="Dark Theme", command=lambda: apply_theme("Dark"))
menubar.add_cascade(label="View", menu=view_menu)
root.config(menu=menubar)

# Toolbar
toolbar = tk.Frame(root)
toolbar.pack(side="top", fill="x")

theme_button = tk.Button(toolbar, text="Toggle Theme", command=toggle_theme)
theme_button.pack(side="left", padx=5, pady=5)

# Main content frame
content_frame = tk.Frame(root, padx=20, pady=20)
content_frame.pack(fill="both", expand=True)

label = tk.Label(content_frame, text="Welcome to the Theme Switcher App", font=("Arial", 16))
label.pack(pady=50)

# Apply default theme
apply_theme(current_theme)

root.mainloop()
