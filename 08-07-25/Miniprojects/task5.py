import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def open_preferences():
    pref_win = tk.Toplevel(root)
    pref_win.title("Preferences")
    pref_win.geometry("400x300")

    notebook = ttk.Notebook(pref_win)
    notebook.pack(expand=True, fill='both', padx=10, pady=10)

    # Frame 1: Account Settings
    frame_account = ttk.Frame(notebook)
    notebook.add(frame_account, text='Account')

    ttk.Label(frame_account, text="Username:").grid(row=0, column=0, sticky='w', padx=10, pady=5)
    ttk.Entry(frame_account).grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(frame_account, text="Email:").grid(row=1, column=0, sticky='w', padx=10, pady=5)
    ttk.Entry(frame_account).grid(row=1, column=1, padx=10, pady=5)

    ttk.Checkbutton(frame_account, text="Enable 2FA").grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    # Frame 2: Theme & Appearance
    frame_theme = ttk.Frame(notebook)
    notebook.add(frame_theme, text='Theme')

    ttk.Label(frame_theme, text="Font Size:").grid(row=0, column=0, sticky='w', padx=10, pady=5)
    ttk.Entry(frame_theme).grid(row=0, column=1, padx=10, pady=5)

    ttk.Checkbutton(frame_theme, text="Dark Mode").grid(row=1, column=0, columnspan=2, padx=10, pady=5)
    ttk.Checkbutton(frame_theme, text="High Contrast").grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    # Frame 3: Notifications
    frame_notifications = ttk.Frame(notebook)
    notebook.add(frame_notifications, text='Notifications')

    ttk.Checkbutton(frame_notifications, text="Email Alerts").grid(row=0, column=0, sticky='w', padx=10, pady=5)
    ttk.Checkbutton(frame_notifications, text="Push Notifications").grid(row=1, column=0, sticky='w', padx=10, pady=5)
    ttk.Checkbutton(frame_notifications, text="Show Popups").grid(row=2, column=0, sticky='w', padx=10, pady=5)

    # Optional: Save button
    ttk.Button(pref_win, text="Save", command=lambda: messagebox.showinfo("Saved", "Preferences saved!")).pack(pady=5)

# Main window
root = tk.Tk()
root.title("Settings Panel Example")
root.geometry("300x200")

# Menu
menu_bar = tk.Menu(root)
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Preferences", command=open_preferences)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
root.config(menu=menu_bar)

tk.Label(root, text="Use Edit > Preferences to open settings.").pack(pady=60)

root.mainloop()
