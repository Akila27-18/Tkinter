import tkinter as tk

class CounterWidget(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.count = 0  # initial counter value

        # Label to display the current count
        self.label = tk.Label(self, text=f"Count: {self.count}", font=("Arial", 16))
        self.label.pack(pady=10)

        # Button row
        button_frame = tk.Frame(self)
        button_frame.pack(pady=5)

        # Increment button
        inc_btn = tk.Button(button_frame, text="Increment", command=self.increment)
        inc_btn.grid(row=0, column=0, padx=5)

        # Decrement button
        dec_btn = tk.Button(button_frame, text="Decrement", command=self.decrement)
        dec_btn.grid(row=0, column=1, padx=5)

        # Reset button
        reset_btn = tk.Button(button_frame, text="Reset", command=self.reset)
        reset_btn.grid(row=0, column=2, padx=5)

    def increment(self):
        self.count += 1
        self.label.config(text=f"Count: {self.count}")

    def decrement(self):
        self.count -= 1
        self.label.config(text=f"Count: {self.count}")

    def reset(self):
        self.count = 0
        self.label.config(text=f"Count: {self.count}")


# Main window to use the custom widget
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Counter with Custom Widget")
    root.geometry("300x200")

    counter = CounterWidget(root)
    counter.pack(expand=True, fill="both", padx=20, pady=20)

    root.mainloop()
