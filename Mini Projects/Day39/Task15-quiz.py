import tkinter as tk

# Hardcoded quiz question and answer
question_text = "What is the capital of France?"
correct_answer = "Paris"

def check_answer():
    user_answer = answer_entry.get().strip()
    if user_answer.lower() == correct_answer.lower():
        result_label.config(text="✅ Correct!", fg="green")
    else:
        result_label.config(text="❌ Incorrect. Try again.", fg="red")

# GUI setup
root = tk.Tk()
root.title("Basic Quiz App")
root.geometry("400x250")

# Question Label
question_label = tk.Label(root, text=question_text, font=("Arial", 14), wraplength=350)
question_label.pack(pady=20)

# Answer Entry
answer_entry = tk.Entry(root, width=40)
answer_entry.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=check_answer)
submit_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
