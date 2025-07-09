import tkinter as tk
import re

def validate_email(event=None):
    email = email_entry.get()
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.fullmatch(pattern, email):
        submit_button.config(state='normal')
    else:
        submit_button.config(state='disabled')

def submit():
    tk.messagebox.showinfo("Success", f"Email submitted: {email_entry.get()}")

# Main window
root = tk.Tk()
root.title("Email Validator")
root.geometry("400x200")

tk.Label(root, text="Enter your Email:", font=('Arial', 12)).pack(pady=10)

email_entry = tk.Entry(root, width=30, font=('Arial', 12))
email_entry.pack()
email_entry.bind('<KeyRelease>', validate_email)

submit_button = tk.Button(root, text="Submit", state='disabled', command=submit)
submit_button.pack(pady=20)

# Optional: for messagebox
import tkinter.messagebox

root.mainloop()
