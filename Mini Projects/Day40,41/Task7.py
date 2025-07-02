import tkinter as tk
import re

def check_strength():
    password = entry_password.get()
    strength = "Weak"
    color = "red"

    # Regex patterns
    length = len(password) >= 8
    upper = re.search(r'[A-Z]', password)
    lower = re.search(r'[a-z]', password)
    digit = re.search(r'[0-9]', password)
    symbol = re.search(r'[^A-Za-z0-9]', password)

    if all([length, upper, lower, digit, symbol]):
        strength = "Strong"
        color = "green"
    elif length and ((upper and lower) or (digit and symbol)):
        strength = "Medium"
        color = "orange"

    label_result.config(text=f"Password Strength: {strength}", fg=color)

# --- GUI Setup ---
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")

tk.Label(root, text="Enter Password:").pack(pady=10)
entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack()

tk.Button(root, text="Check Strength", command=check_strength).pack(pady=10)
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=10)

root.mainloop()
