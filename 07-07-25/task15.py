import tkinter as tk
from tkinter import ttk, messagebox

class MultiStepForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Step Registration Form")
        self.root.geometry("400x350")

        self.user_data = {
            'name': tk.StringVar(),
            'age': tk.StringVar(),
            'course': tk.StringVar(),
            'skills': tk.StringVar()
        }

        # Create all 3 frames
        self.frame1 = tk.Frame(root)
        self.frame2 = tk.Frame(root)
        self.frame3 = tk.Frame(root)

        self.create_frame1()
        self.create_frame2()
        self.create_frame3()

        self.frame1.pack(fill='both', expand=True)

    # ---------------- Frame 1 ----------------
    def create_frame1(self):
        tk.Label(self.frame1, text="Step 1: Personal Info", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame1, text="Name:").pack()
        tk.Entry(self.frame1, textvariable=self.user_data['name']).pack(pady=5)

        tk.Label(self.frame1, text="Age:").pack()
        tk.Entry(self.frame1, textvariable=self.user_data['age']).pack(pady=5)

        tk.Button(self.frame1, text="Next", command=self.goto_frame2).pack(pady=20)

    # ---------------- Frame 2 ----------------
    def create_frame2(self):
        tk.Label(self.frame2, text="Step 2: Course & Skills", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame2, text="Select Course:").pack()
        courses = ["Python", "Java", "Web Development", "Data Science"]
        ttk.Combobox(self.frame2, values=courses, textvariable=self.user_data['course'], state='readonly').pack(pady=5)

        tk.Label(self.frame2, text="Your Skills:").pack()
        tk.Entry(self.frame2, textvariable=self.user_data['skills']).pack(pady=5)

        nav_frame = tk.Frame(self.frame2)
        nav_frame.pack(pady=20)
        tk.Button(nav_frame, text="Back", command=self.goto_frame1).grid(row=0, column=0, padx=10)
        tk.Button(nav_frame, text="Next", command=self.goto_frame3).grid(row=0, column=1, padx=10)

    # ---------------- Frame 3 ----------------
    def create_frame3(self):
        tk.Label(self.frame3, text="Step 3: Summary & Submit", font=("Arial", 14)).pack(pady=10)

        self.summary_label = tk.Label(self.frame3, text="", justify="left", font=("Arial", 10))
        self.summary_label.pack(pady=10)

        nav_frame = tk.Frame(self.frame3)
        nav_frame.pack(pady=20)
        tk.Button(nav_frame, text="Back", command=self.goto_frame2).grid(row=0, column=0, padx=10)
        tk.Button(nav_frame, text="Submit", command=self.submit).grid(row=0, column=1, padx=10)

    # ---------------- Navigation Functions ----------------
    def goto_frame1(self):
        self.switch_frame(self.frame1)

    def goto_frame2(self):
        if not self.user_data['name'].get().strip() or not self.user_data['age'].get().isdigit():
            messagebox.showerror("Validation Error", "Enter valid Name and numeric Age.")
            return
        self.switch_frame(self.frame2)

    def goto_frame3(self):
        if not self.user_data['course'].get():
            messagebox.showerror("Validation Error", "Please select a course.")
            return
        self.update_summary()
        self.switch_frame(self.frame3)

    def switch_frame(self, frame):
        for f in [self.frame1, self.frame2, self.frame3]:
            f.pack_forget()
        frame.pack(fill='both', expand=True)

    def update_summary(self):
        summary = (
            f"Name: {self.user_data['name'].get()}\n"
            f"Age: {self.user_data['age'].get()}\n"
            f"Course: {self.user_data['course'].get()}\n"
            f"Skills: {self.user_data['skills'].get()}"
        )
        self.summary_label.config(text=summary)

    def submit(self):
        messagebox.showinfo("Submitted", "Registration Successful!")
        self.root.destroy()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MultiStepForm(root)
    root.mainloop()
