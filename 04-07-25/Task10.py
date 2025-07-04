import tkinter as tk
from tkinter import messagebox

def generate_card():
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    email = entry_email.get().strip()

    # --- Validation ---
    if not name:
        messagebox.showerror("Input Error", "Name cannot be empty.")
        return
    if not age.isdigit() or int(age) <= 0:
        messagebox.showerror("Input Error", "Age must be a positive number.")
        return
    if '@' not in email or '.' not in email:
        messagebox.showerror("Input Error", "Invalid email address.")
        return

    # --- Draw Profile Card ---
    canvas.delete("all")
    canvas.create_rectangle(20, 20, 280, 180, fill="#f0f8ff", outline="#4682b4", width=2)
    canvas.create_oval(30, 30, 90, 90, fill="#87cefa", outline="")

    canvas.create_text(160, 40, text=f"Name: {name}", anchor="w", font=("Helvetica", 12, "bold"))
    canvas.create_text(160, 70, text=f"Age: {age}", anchor="w", font=("Helvetica", 12))
    canvas.create_text(160, 100, text=f"Email: {email}", anchor="w", font=("Helvetica", 12))

# --- Main Window ---
root = tk.Tk()
root.title("User Profile Card Generator")
root.geometry("320x320")

# --- Input Frame ---
input_frame = tk.Frame(root)
input_frame.pack(pady=10, fill="x", padx=10)

tk.Label(input_frame, text="Name:").pack(anchor="w")
entry_name = tk.Entry(input_frame)
entry_name.pack(fill="x")

tk.Label(input_frame, text="Age:").pack(anchor="w")
entry_age = tk.Entry(input_frame)
entry_age.pack(fill="x")

tk.Label(input_frame, text="Email:").pack(anchor="w")
entry_email = tk.Entry(input_frame)
entry_email.pack(fill="x")

tk.Button(input_frame, text="Generate Profile Card", command=generate_card).pack(pady=10)

# --- Canvas Frame ---
canvas_frame = tk.Frame(root)
canvas_frame.pack(padx=10)

canvas = tk.Canvas(canvas_frame, width=300, height=200, bg="white")
canvas.pack()

root.mainloop()
