import tkinter as tk
from tkinter import messagebox, Toplevel

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("500x400")
        
        # ==== Questions ====
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Berlin", "Paris", "London", "Madrid"],
                "answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "answer": "Mars"
            },
            {
                "question": "Who wrote 'Hamlet'?",
                "options": ["Shakespeare", "Chaucer", "Dickens", "Wordsworth"],
                "answer": "Shakespeare"
            }
        ]
        self.current_index = 0
        self.score = 0

        # ==== Menu ====
        menubar = tk.Menu(self.root)
        quizmenu = tk.Menu(menubar, tearoff=0)
        quizmenu.add_command(label="Start New", command=self.start_quiz)
        quizmenu.add_separator()
        quizmenu.add_command(label="End", command=self.root.quit)
        menubar.add_cascade(label="Quiz", menu=quizmenu)
        self.root.config(menu=menubar)

        # ==== Main Frame ====
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.question_label = tk.Label(self.main_frame, text="", font=("Arial", 14), wraplength=450, justify="left")
        self.question_label.pack(pady=10)

        self.selected_option = tk.StringVar()

        self.option_buttons = []
        for _ in range(4):
            btn = tk.Radiobutton(self.main_frame, text="", variable=self.selected_option,
                                 value="", font=("Arial", 12), anchor="w", justify="left")
            btn.pack(fill="x", pady=5)
            self.option_buttons.append(btn)

        self.submit_btn = tk.Button(self.main_frame, text="Submit Answer", command=self.submit_answer)
        self.submit_btn.pack(pady=20)

        # Start with disabled state
        self.disable_quiz()

    # ==== Quiz Logic ====
    def start_quiz(self):
        self.current_index = 0
        self.score = 0
        self.enable_quiz()
        self.load_question()

    def load_question(self):
        if self.current_index < len(self.questions):
            q = self.questions[self.current_index]
            self.question_label.config(text=f"Q{self.current_index+1}. {q['question']}")
            self.selected_option.set(None)
            for i, opt in enumerate(q['options']):
                self.option_buttons[i].config(text=opt, value=opt)
        else:
            self.show_score()
            self.disable_quiz()

    def submit_answer(self):
        selected = self.selected_option.get()
        if not selected:
            messagebox.showwarning("No Answer", "Please select an option before submitting.")
            return
        
        confirm = messagebox.askyesno("Confirm", f"Submit '{selected}' as your answer?")
        if confirm:
            correct_answer = self.questions[self.current_index]["answer"]
            if selected == correct_answer:
                self.score += 1
            self.current_index += 1
            self.load_question()

    def show_score(self):
        score_win = Toplevel(self.root)
        score_win.title("Quiz Score")
        score_win.geometry("300x150")
        tk.Label(score_win, text=f"Your Score: {self.score}/{len(self.questions)}",
                 font=("Arial", 16)).pack(pady=40)
        tk.Button(score_win, text="Close", command=score_win.destroy).pack()

    def disable_quiz(self):
        self.question_label.config(text="Start a new quiz from the Quiz menu.")
        self.submit_btn.config(state=tk.DISABLED)
        for btn in self.option_buttons:
            btn.config(state=tk.DISABLED)

    def enable_quiz(self):
        self.submit_btn.config(state=tk.NORMAL)
        for btn in self.option_buttons:
            btn.config(state=tk.NORMAL)

# ==== Run App ====
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
