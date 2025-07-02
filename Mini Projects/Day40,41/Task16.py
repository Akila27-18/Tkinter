import tkinter as tk

def toggle_submit():
    if agree_var.get():
        submit_btn.config(state="normal")
    else:
        submit_btn.config(state="disabled")

def submit_form():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    print(f"Name: {name}, Email: {email}")  # You can show a messagebox if needed

# --- GUI Setup ---
root = tk.Tk()
root.title("Terms Agreement Form")
root.geometry("350x200")

# Labels and Entries
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=1, column=1)

# Terms and Conditions Checkbox
agree_var = tk.IntVar()
check_btn = tk.Checkbutton(root, text="I agree to the Terms and Conditions",
                           variable=agree_var, command=toggle_submit)
check_btn.grid(row=2, columnspan=2, pady=10)

# Submit Button (initially disabled)
submit_btn = tk.Button(root, text="Submit", state="disabled", command=submit_form)
submit_btn.grid(row=3, columnspan=2, pady=10)

root.mainloop()
