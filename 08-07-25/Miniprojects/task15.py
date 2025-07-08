import tkinter as tk
from tkinter import messagebox

def show_settings(category):
    # Clear current contents of the right pane
    for widget in right_frame.winfo_children():
        widget.destroy()

    if category == "General":
        tk.Label(right_frame, text="Auto Save:").grid(row=0, column=0, sticky="w", pady=5, padx=10)
        tk.Checkbutton(right_frame, text="Enable Auto Save").grid(row=0, column=1, sticky="w")

        tk.Label(right_frame, text="Default Timeout (mins):").grid(row=1, column=0, sticky="w", pady=5, padx=10)
        tk.Spinbox(right_frame, from_=1, to=60, width=5).grid(row=1, column=1, sticky="w")

    elif category == "Display":
        tk.Label(right_frame, text="Dark Mode:").grid(row=0, column=0, sticky="w", pady=5, padx=10)
        tk.Checkbutton(right_frame, text="Enable Dark Theme").grid(row=0, column=1, sticky="w")

        tk.Label(right_frame, text="Font Size:").grid(row=1, column=0, sticky="w", pady=5, padx=10)
        tk.Spinbox(right_frame, from_=8, to=32, width=5).grid(row=1, column=1, sticky="w")

    elif category == "Notifications":
        tk.Label(right_frame, text="Pop-up Alerts:").grid(row=0, column=0, sticky="w", pady=5, padx=10)
        tk.Checkbutton(right_frame, text="Enable Popups").grid(row=0, column=1, sticky="w")

        tk.Label(right_frame, text="Check Frequency (mins):").grid(row=1, column=0, sticky="w", pady=5, padx=10)
        tk.Spinbox(right_frame, from_=1, to=120, width=5).grid(row=1, column=1, sticky="w")

    # Save button
    tk.Button(right_frame, text="Save", command=lambda: messagebox.showinfo("Saved", "Settings saved successfully!")).grid(
        row=3, column=0, columnspan=2, pady=15
    )

def create_settings_window():
    win = tk.Toplevel(root)
    win.title("Settings Manager")
    win.geometry("500x300")

    # PanedWindow
    paned = tk.PanedWindow(win, orient=tk.HORIZONTAL)
    paned.pack(fill=tk.BOTH, expand=True)

    # Left pane - category list
    left_frame = tk.Frame(paned, bg="#f0f0f0", width=150)
    paned.add(left_frame)

    categories = ["General", "Display", "Notifications"]
    for cat in categories:
        tk.Button(left_frame, text=cat, width=20, anchor="w",
                  command=lambda c=cat: show_settings(c)).pack(pady=5, padx=5, anchor="w")

    # Right pane - dynamic content
    global right_frame
    right_frame = tk.Frame(paned)
    paned.add(right_frame)

    # Default view
    show_settings("General")

# Main app window
root = tk.Tk()
root.title("Main App")
root.geometry("300x150")

tk.Button(root, text="Open Settings", command=create_settings_window).pack(pady=40)

root.mainloop()
