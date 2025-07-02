import tkinter as tk
from tkinter import messagebox

total_expense = 0.0

def add_expense():
    global total_expense
    item = entry_item.get().strip()
    amount = entry_amount.get().strip()

    if not item or not amount:
        messagebox.showwarning("Input Error", "Both fields are required.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Invalid Amount", "Amount must be a number.")
        return

    total_expense += amount
    text_log.insert(tk.END, f"{item:<20} ₹{amount:.2f}\n")
    label_total.config(text=f"Total: ₹{total_expense:.2f}")

    entry_item.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("450x400")

# Input Form
tk.Label(root, text="Item:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_item = tk.Entry(root, width=30)
entry_item.grid(row=0, column=1, pady=5, padx=5)

tk.Label(root, text="Amount (₹):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_amount = tk.Entry(root, width=30)
entry_amount.grid(row=1, column=1, pady=5, padx=5)

tk.Button(root, text="Add Expense", command=add_expense).grid(row=2, column=0, columnspan=2, pady=10)

# Text log (item list)
text_log = tk.Text(root, width=50, height=10)
text_log.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
text_log.insert(tk.END, f"{'Item':<20}Amount\n{'-'*30}\n")

# Total display label
label_total = tk.Label(root, text="Total: ₹0.00", font=("Arial", 12, "bold"))
label_total.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
