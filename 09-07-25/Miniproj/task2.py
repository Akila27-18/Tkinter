import tkinter as tk
from tkinter import messagebox

def check_answers(*args):
    if q1_answer.get() != 0 and q2_answer.get() != 0:
        next_button.config(state='normal')
    else:
        next_button.config(state='disabled')

def submit():
    # Optional: Validate again before moving forward
    if q1_answer.get() == 0 or q2_answer.get() == 0:
        messagebox.showwarning("Incomplete", "Please answer all questions.")
    else:
        messagebox.showinfo("Submitted", "Thank you for completing the survey!")
        # Proceed to next step (e.g., open new frame/window)

# Main window
root = tk.Tk()
root.title("Survey Form")
root.geometry("400x300")

# Question 1
tk.Label(root, text="1. How satisfied are you with our service?", font=('Arial', 12)).pack(anchor='w', pady=(10, 0), padx=10)
q1_answer = tk.IntVar(value=0)
q1_answer.trace_add('write', check_answers)

options1 = [("Very Satisfied", 1), ("Satisfied", 2), ("Not Satisfied", 3)]
for text, value in options1:
    tk.Radiobutton(root, text=text, variable=q1_answer, value=value).pack(anchor='w', padx=20)

# Question 2
tk.Label(root, text="2. Would you recommend us to others?", font=('Arial', 12)).pack(anchor='w', pady=(20, 0), padx=10)
q2_answer = tk.IntVar(value=0)
q2_answer.trace_add('write', check_answers)

options2 = [("Yes", 1), ("Maybe", 2), ("No", 3)]
for text, value in options2:
    tk.Radiobutton(root, text=text, variable=q2_answer, value=value).pack(anchor='w', padx=20)

# Next Button
next_button = tk.Button(root, text="Next", state='disabled', command=submit)
next_button.pack(pady=30)

root.mainloop()
