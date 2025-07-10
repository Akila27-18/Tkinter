import tkinter as tk
from tkinter import messagebox, filedialog

class ResumeBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Resume Builder")
        self.root.geometry("500x500")
        
        # Name
        tk.Label(root, text="Name:", font=("Arial", 12)).pack(pady=5)
        self.name_entry = tk.Entry(root, width=50)
        self.name_entry.pack(pady=5)

        # Skills
        tk.Label(root, text="Skills:", font=("Arial", 12)).pack(pady=5)
        self.skills_text = tk.Text(root, height=5, width=50)
        self.skills_text.pack(pady=5)

        # Experience
        tk.Label(root, text="Experience:", font=("Arial", 12)).pack(pady=5)
        self.exp_text = tk.Text(root, height=10, width=50)
        self.exp_text.pack(pady=5)

        # Save Button
        tk.Button(root, text="Export as .txt", command=self.save_resume, bg="green", fg="white").pack(pady=15)

    def save_resume(self):
        name = self.name_entry.get().strip()
        skills = self.skills_text.get("1.0", "end-1c").strip()
        experience = self.exp_text.get("1.0", "end-1c").strip()

        if not name or not skills or not experience:
            messagebox.showwarning("Missing Fields", "Please fill out all fields.")
            return

        resume_text = f"Resume\n=======\n\nName: {name}\n\nSkills:\n{skills}\n\nExperience:\n{experience}\n"

        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")],
                                                 title="Save Resume As")
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(resume_text)
                messagebox.showinfo("Success", "Resume saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeBuilder(root)
    root.mainloop()
