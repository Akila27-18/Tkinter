import tkinter as tk

expression = ""

def press(value):
    global expression
    expression += str(value)
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, expression)

def clear():
    global expression
    expression = ""
    input_field.delete(0, tk.END)
    result_label.config(text="")

def calculate():
    global expression
    try:
        # Replace × and ÷ with * and /
        expr = expression.replace("×", "*").replace("÷", "/")
        result = eval(expr)
        result_label.config(text=f"Result: {result}")
        expression = str(result)
    except Exception as e:
        result_label.config(text="Error")
        expression = ""

# GUI setup
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")

# Entry field
input_field = tk.Entry(root, font=("Arial", 16), bd=5, relief=tk.RIDGE, justify='right')
input_field.pack(padx=10, pady=10, fill='x')

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack()

# Button layout
buttons = [
    ['7', '8', '9', '÷'],
    ['4', '5', '6', '×'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill='both')
    for char in row:
        if char == '=':
            btn = tk.Button(frame, text=char, font=("Arial", 14), command=calculate)
        elif char == 'C':
            btn = tk.Button(frame, text=char, font=("Arial", 14), command=clear)
        else:
            btn = tk.Button(frame, text=char, font=("Arial", 14), command=lambda ch=char: press(ch))
        btn.pack(side='left', expand=True, fill='both', padx=2, pady=2)

root.mainloop()
