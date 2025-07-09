import tkinter as tk

class ToggleSwitch(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        self.state = False  # False = OFF, True = ON

        self.label = tk.Label(self, text="OFF", fg="red", font=("Arial", 12, "bold"))
        self.label.pack(side="left", padx=5)

        self.button = tk.Button(self, text="Toggle", command=self.toggle)
        self.button.pack(side="right", padx=5)

    def toggle(self):
        self.state = not self.state
        self.label.config(text="ON" if self.state else "OFF", fg="green" if self.state else "red")

# Main window
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Custom Toggle Switch Widget")
    root.geometry("300x200")

    # Create multiple toggle switch instances
    toggle1 = ToggleSwitch(root)
    toggle1.pack(pady=10)

    toggle2 = ToggleSwitch(root)
    toggle2.pack(pady=10)

    toggle3 = ToggleSwitch(root)
    toggle3.pack(pady=10)

    root.mainloop()
