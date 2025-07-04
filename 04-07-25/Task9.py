import tkinter as tk
from tkinter import ttk

# Quiz Data
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Pacific", "Arctic"],
        "answer": "Pacific"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
        "answer": "William Shakespeare"
    },
    {
        "question": "Which gas do plants absorb?",
        "options": ["Oxygen", "Carbon Dioxide", "Hydrogen", "Nitrogen"],
        "answer": "Carbon Dioxide"
    }
]

# Global variables
current_q = 0
score = 0

# Functions
def load_question():
    """Loads current question and options"""
    q = questions[current_q]
    question_label.config(text=f"Q{current_q+1}: {q['question']}")
    selected_option.set(None)
    for i, option in enumerate(q["options"]):
        radio_buttons[i].config(text=option, value=option, state=tk.NORMAL)
    next_button.config(state=tk.DISABLED)

def on_option_selected():
    """Disables options and enables Next button"""
    chosen = selected_option.get()
    correct = questions[current_q]["answer"]
    if chosen == correct:
        global score
        score += 1
    for rb in radio_buttons:
        rb.config(state=tk.DISABLED)
    next_button.config(state=tk.NORMAL)

def next_question():
    """Moves to the next question or ends quiz"""
    global current_q
    current_q += 1
    if current_q < len(questions):
        load_question()
    else:
        show_result()

def show_result():
    """Displays the final score"""
    question_label.config(text=f"Quiz Completed!\nYour Score: {score} / {len(questions)}")
    for rb in radio_buttons:
        rb.grid_forget()
    next_button.grid_forget()

# UI Setup
root = tk.Tk()
root.title("Quiz App")
root.geometry("500x300")

# Question Label
question_label = ttk.Label(root, text="", wraplength=400, font=("Arial", 14))
question_label.grid(row=0, column=0, columnspan=2, pady=20)

# Selected option
selected_option = tk.StringVar()

# Radio Buttons for options
radio_buttons = []
for i in range(4):
    rb = ttk.Radiobutton(root, text="", variable=selected_option, value="", command=on_option_selected)
    rb.grid(row=i+1, column=0, sticky='w', padx=40, pady=2)
    radio_buttons.append(rb)

# Next Button
next_button = ttk.Button(root, text="Next", command=next_question, state=tk.DISABLED)
next_button.grid(row=6, column=0, pady=20)

# Load first question
load_question()

# Run the app
root.mainloop()
