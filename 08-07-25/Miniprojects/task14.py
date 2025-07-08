import tkinter as tk
from tkinter import messagebox, Menu
import re

class FormValidationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Form Validation App")
        self.root.geometry("400x300")

        self.create_menu()
        self.create_form()

    def create_menu(self):
        menubar = Menu(self.root)
        form_menu = Menu(menubar, tearoff=0)
        form_menu.add_command(label="Reset", command=self.reset_form)
        form_menu.add_separator()
        form_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="Form", menu=form_menu)
        self.root.config(menu=menubar)

    def create_form(self):
        form_frame = tk.Frame(self.root, padx=20, pady=20)
        form_frame.pack(pady=30)

        tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="e", pady=5)
        self.name_entry = tk.Entry(form_frame, width=30)
        self.name_entry.grid(row=0, column=1)

        tk.Label(form_frame, text="Email:").grid(row=1, column=0, sticky="e", pady=5)
        self.email_entry = tk.Entry(form_frame, width=30)
        self.email_entry.grid(row=1, column=1)

        tk.Label(form_frame, text="Phone:").grid(row=2, column=0, sticky="e", pady=5)
        self.phone_entry = tk.Entry(form_frame, width=30)
        self.phone_entry.grid(row=2, column=1)

        submit_btn = tk.Button(form_frame, text="Submit", command=self.validate_form)
        submit_btn.grid(row=3, column=1, pady=20, sticky="e")

    def validate_form(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if not name:
            messagebox.showerror("Validation Error", "Name is required.")
            return

        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        if not re.match(email_pattern, email):
            messagebox.showerror("Validation Error", "Invalid email format.")
            return

        if not phone.isdigit() or len(phone) != 10:
            messagebox.showerror("Validation Error", "Phone must be 10 digits.")
            return

        messagebox.showinfo("Success", f"Form submitted:\nName: {name}\nEmail: {email}\nPhone: {phone}")

    def reset_form(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = FormValidationApp(root)
    root.mainloop()
