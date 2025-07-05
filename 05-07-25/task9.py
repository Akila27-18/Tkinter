import tkinter as tk
from tkinter import StringVar, messagebox

# --- Answer Check Function with Validation ---
def check_answer():
    selected = answer_var.get()
    
    if selected == "":
        messagebox.showwarning("Validation", "Please select an answer before submitting.")
        result_label.config(text="", fg="black")
        return
    
    if selected == correct_answer:
        result_label.config(text="✅ Correct!", fg="green")
    else:
        result_label.config(text="❌ Wrong answer!", fg="red")

# --- Main App Window ---
root = tk.Tk()
root.title("Quiz App with Validation")
root.geometry("400x250")

# --- Frame for layout ---
frame = tk.Frame(root)
frame.pack(pady=20)

# --- Question Label ---
question = "What is the capital of France?"
question_label = tk.Label(frame, text=question, font=("Arial", 12))
question_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="w")

# --- Options (Radiobuttons) ---
options = ["Berlin", "Madrid", "Paris", "Rome"]
correct_answer = "Paris"

answer_var = StringVar(value="")  # Tracks selected option

for i, option in enumerate(options):
    radio = tk.Radiobutton(
        frame, text=option, variable=answer_var, value=option,
        font=("Arial", 10), anchor="w", justify="left"
    )
    radio.grid(row=i+1, column=0, sticky="w", padx=20)

# --- Submit Button ---
submit_btn = tk.Button(frame, text="Check Answer", command=check_answer)
submit_btn.grid(row=len(options) + 1, column=0, pady=10)

# --- Result Label ---
result_label = tk.Label(frame, text="", font=("Arial", 11, "bold"))
result_label.grid(row=len(options) + 2, column=0, pady=5)

# --- Run App ---
root.mainloop()
