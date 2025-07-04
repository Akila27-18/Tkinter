import tkinter as tk
from tkinter import ttk

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")

        # Temperature Spinbox
        tk.Label(root, text="Temperature:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.temp_spin = tk.Spinbox(root, from_=-100, to=212, width=10, command=self.convert)
        self.temp_spin.grid(row=0, column=1, padx=5, pady=5)
        self.temp_spin.delete(0, tk.END)
        self.temp_spin.insert(0, "0")

        # Unit Combobox
        tk.Label(root, text="Unit:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.unit_var = tk.StringVar()
        self.unit_cb = ttk.Combobox(root, textvariable=self.unit_var, values=["Celsius", "Fahrenheit"], state="readonly", width=10)
        self.unit_cb.grid(row=0, column=3, padx=5, pady=5)
        self.unit_cb.set("Celsius")
        self.unit_cb.bind("<<ComboboxSelected>>", lambda e: self.convert())

        # Convert Button
        convert_btn = tk.Button(root, text="Convert", command=self.convert)
        convert_btn.grid(row=0, column=4, padx=10, pady=5)

        # Result Label
        self.result_label = tk.Label(root, text="Result: ")
        self.result_label.grid(row=1, column=0, columnspan=5, pady=10)

        # Dynamic update on key release in Spinbox
        self.temp_spin.bind("<KeyRelease>", lambda e: self.convert())

    def convert(self):
        try:
            temp = float(self.temp_spin.get())
            unit = self.unit_var.get()

            if unit == "Celsius":
                result = temp * 9/5 + 32
                self.result_label.config(text=f"{temp:.2f}°C = {result:.2f}°F")
            elif unit == "Fahrenheit":
                result = (temp - 32) * 5/9
                self.result_label.config(text=f"{temp:.2f}°F = {result:.2f}°C")
        except ValueError:
            self.result_label.config(text="Enter a valid temperature.")

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()
