# task40_calculator_row.py
import tkinter as tk

class CalculatorRow(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.num1 = tk.Entry(self, width=5)
        self.num2 = tk.Entry(self, width=5)
        self.operator = tk.Label(self, text="+")
        self.result = tk.Label(self, text="=")
        tk.Button(self, text="=", command=self.calculate).pack(side="right")
        self.num1.pack(side="left"), self.operator.pack(side="left")
        self.num2.pack(side="left"), self.result.pack(side="left")

    def calculate(self):
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            self.result.config(text=f"= {a + b}")
        except ValueError:
            self.result.config(text="Error")

root = tk.Tk()
widget = CalculatorRow(root)
widget.pack(pady=10)
root.mainloop()
