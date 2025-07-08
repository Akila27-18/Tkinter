import tkinter as tk
from tkinter import ttk, messagebox

def show_summary():
    summary_win = tk.Toplevel(root)
    summary_win.title("Registration Summary")
    summary_win.geometry("400x300")
    
    summary_text = f"""
    --- Personal Info ---
    Name: {name_var.get()}
    Age: {age_var.get()}
    Gender: {gender_var.get()}
    
    --- Contact Info ---
    Email: {email_var.get()}
    Phone: {phone_var.get()}
    Country: {country_var.get()}
    
    --- Account Info ---
    Username: {username_var.get()}
    Account Type: {account_type_var.get()}
    """
    
    tk.Label(summary_win, text="Registration Summary", font=('Arial', 14, 'bold')).pack(pady=10)
    tk.Label(summary_win, text=summary_text.strip(), justify='left', font=('Courier', 10)).pack(padx=20)

# Main Window
root = tk.Tk()
root.title("Multi-Section Registration Form")
root.geometry("500x600")
root.resizable(False, False)

# Variables
name_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
country_var = tk.StringVar()
username_var = tk.StringVar()
account_type_var = tk.StringVar()

# ----------------- Personal Info Frame -----------------
frame1 = tk.LabelFrame(root, text="Personal Info", padx=10, pady=10)
frame1.pack(fill="x", padx=20, pady=10)

tk.Label(frame1, text="Full Name").grid(row=0, column=0, sticky='w')
tk.Entry(frame1, textvariable=name_var).grid(row=0, column=1)

tk.Label(frame1, text="Age").grid(row=1, column=0, sticky='w')
tk.Spinbox(frame1, from_=10, to=100, textvariable=age_var).grid(row=1, column=1)

tk.Label(frame1, text="Gender").grid(row=2, column=0, sticky='w')
ttk.Combobox(frame1, textvariable=gender_var, values=["Male", "Female", "Other"]).grid(row=2, column=1)

# ----------------- Contact Info Frame -----------------
frame2 = tk.LabelFrame(root, text="Contact Info", padx=10, pady=10)
frame2.pack(fill="x", padx=20, pady=10)

tk.Label(frame2, text="Email").grid(row=0, column=0, sticky='w')
tk.Entry(frame2, textvariable=email_var).grid(row=0, column=1)

tk.Label(frame2, text="Phone").grid(row=1, column=0, sticky='w')
tk.Entry(frame2, textvariable=phone_var).grid(row=1, column=1)

tk.Label(frame2, text="Country").grid(row=2, column=0, sticky='w')
ttk.Combobox(frame2, textvariable=country_var, values=["India", "USA", "UK", "Canada", "Other"]).grid(row=2, column=1)

# ----------------- Account Info Frame -----------------
frame3 = tk.LabelFrame(root, text="Account Info", padx=10, pady=10)
frame3.pack(fill="x", padx=20, pady=10)

tk.Label(frame3, text="Username").grid(row=0, column=0, sticky='w')
tk.Entry(frame3, textvariable=username_var).grid(row=0, column=1)

tk.Label(frame3, text="Account Type").grid(row=1, column=0, sticky='w')
ttk.Combobox(frame3, textvariable=account_type_var, values=["Standard", "Premium", "Admin"]).grid(row=1, column=1)

# ----------------- Submit Button -----------------
tk.Button(root, text="Submit", font=('Arial', 12), command=show_summary).pack(pady=20)

root.mainloop()
