import tkinter as tk

class Notification(tk.Frame):
    def __init__(self, master, message, bg_color="#f9ed69", icon_text="🔔", duration=5000, **kwargs):
        super().__init__(master, bg=bg_color, pady=5, padx=10, **kwargs)

        # Icon
        self.icon = tk.Label(self, text=icon_text, bg=bg_color, font=("Arial", 14))
        self.icon.pack(side="left", padx=(5, 10))

        # Message
        self.message = tk.Label(self, text=message, bg=bg_color, font=("Arial", 12))
        self.message.pack(side="left", expand=True)

        # Close Button
        self.close_btn = tk.Button(self, text="✕", command=self.destroy, bg=bg_color, bd=0, font=("Arial", 12))
        self.close_btn.pack(side="right", padx=5)

        # Auto-destroy after duration (default 5000ms)
        self.after(duration, self.destroy)

# Demo usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Custom Notification Demo")
    root.geometry("400x250")

    def show_notification():
        notif = Notification(root, "This is a sample notification!", bg_color="#d1e7dd", icon_text="✅")
        notif.pack(pady=10, fill='x')

    tk.Button(root, text="Show Notification", command=show_notification).pack(pady=50)

    root.mainloop()
