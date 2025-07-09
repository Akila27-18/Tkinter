import tkinter as tk
from tkinter import messagebox

class PanelControlApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Resizable Panel with State Controls")
        self.master.geometry("400x300")

        # State flag
        self.panel_enabled = True

        # Toggle Button
        self.toggle_btn = tk.Button(master, text="Disable Panel", command=self.toggle_panel)
        self.toggle_btn.pack(pady=10)

        # Frame Panel
        self.panel = tk.LabelFrame(master, text="User Panel", padx=10, pady=10)
        self.panel.pack(padx=10, pady=10, fill="both", expand=True)

        # Panel Content
        self.entry1 = tk.Entry(self.panel)
        self.entry1.pack(pady=5, fill="x")

        self.entry2 = tk.Entry(self.panel)
        self.entry2.pack(pady=5, fill="x")

        self.submit_btn = tk.Button(self.panel, text="Submit", command=self.submit_form)
        self.submit_btn.pack(pady=5)

        self.clear_btn = tk.Button(self.panel, text="Clear", command=self.clear_form)
        self.clear_btn.pack(pady=5)

    def toggle_panel(self):
        self.panel_enabled = not self.panel_enabled
        new_state = "normal" if self.panel_enabled else "disabled"
        self.toggle_btn.config(text="Disable Panel" if self.panel_enabled else "Enable Panel")
        self.set_panel_state(new_state)

    def set_panel_state(self, state):
        for widget in self.panel.winfo_children():
            try:
                widget.config(state=state)
            except tk.TclError:
                pass  # Some widgets may not support 'state'

    def submit_form(self):
        val1 = self.entry1.get()
        val2 = self.entry2.get()
        messagebox.showinfo("Form Submitted", f"Value 1: {val1}\nValue 2: {val2}")

    def clear_form(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PanelControlApp(root)
    root.mainloop()
