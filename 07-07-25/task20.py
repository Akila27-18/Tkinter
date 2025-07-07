import tkinter as tk
from tkinter import ttk, messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        self.root.geometry("300x250")

        # --- Number 1 ---
        tk.Label(root, text="Enter first number:").pack(pady=5)
        self.num1_var = tk.StringVar()
        tk.Entry(root, textvariable=self.num1_var).pack()

        # --- Number 2 ---
        tk.Label(root, text="Enter second number:").pack(pady=5)
        self.num2_var = tk.StringVar()
        tk.Entry(root, textvariable=self.num2_var).pack()

        # --- Operator ---
        tk.Label(root, text="Select operator:").pack(pady=5)
        self.operator_var = tk.StringVar()
        self.operator_combo = ttk.Combobox(root, values=["+", "-", "*", "/"], textvariable=self.operator_var, state="readonly")
        self.operator_combo.pack()
        self.operator_combo.current(0)

        # --- Calculate Button ---
        tk.Button(root, text="Calculate", command=self.calculate_result).pack(pady=10)

        # --- Result Label ---
        self.result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

    def calculate_result(self):
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            op = self.operator_var.get()

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2
            else:
                raise ValueError("Invalid operator")

            self.result_label.config(text=f"Result: {result:.2f}")

        except ZeroDivisionError:
            messagebox.showerror("Math Error", "Cannot divide by zero.")
            self.result_label.config(text="Result: Error")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            self.result_label.config(text="Result: Error")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
