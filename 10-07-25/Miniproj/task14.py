import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("700x500")

        self.db_init()

        # Input Frame
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Category:").grid(row=0, column=0, padx=5)
        self.category_entry = tk.Entry(input_frame)
        self.category_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Amount:").grid(row=0, column=2, padx=5)
        self.amount_entry = tk.Entry(input_frame)
        self.amount_entry.grid(row=0, column=3, padx=5)

        tk.Button(input_frame, text="Add", command=self.add_expense).grid(row=0, column=4, padx=5)
        tk.Button(input_frame, text="Update", command=self.update_expense).grid(row=0, column=5, padx=5)
        tk.Button(input_frame, text="Delete", command=self.delete_expense).grid(row=0, column=6, padx=5)

        # Filter
        filter_frame = tk.Frame(root)
        filter_frame.pack(pady=5)

        tk.Label(filter_frame, text="Filter by Category:").pack(side="left")
        self.filter_var = tk.StringVar()
        self.filter_combo = ttk.Combobox(filter_frame, textvariable=self.filter_var, state="readonly")
        self.filter_combo.pack(side="left", padx=5)
        self.filter_combo.bind("<<ComboboxSelected>>", lambda e: self.load_expenses())

        tk.Button(filter_frame, text="Export Report", command=self.export_report).pack(side="right", padx=5)

        # Treeview
        self.tree = ttk.Treeview(root, columns=("ID", "Category", "Amount"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Amount", text="Amount")
        self.tree.column("ID", width=50)
        self.tree.column("Category", width=200)
        self.tree.column("Amount", width=100)
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.fill_form)

        # Total Label
        self.total_label = tk.Label(root, text="Total: ₹0", font=("Arial", 12, "bold"))
        self.total_label.pack()

        self.load_expenses()

    def db_init(self):
        self.conn = sqlite3.connect("expenses.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                amount REAL NOT NULL
            )
        """)
        self.conn.commit()

    def add_expense(self):
        category = self.category_entry.get().strip()
        amount = self.amount_entry.get().strip()
        if not category or not amount or not amount.replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "Enter valid category and numeric amount.")
            return
        self.cursor.execute("INSERT INTO expenses (category, amount) VALUES (?, ?)", (category, float(amount)))
        self.conn.commit()
        self.clear_form()
        self.load_expenses()

    def update_expense(self):
        selected = self.tree.selection()
        if not selected:
            return
        expense_id = self.tree.item(selected[0])['values'][0]
        category = self.category_entry.get().strip()
        amount = self.amount_entry.get().strip()
        if not category or not amount or not amount.replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "Enter valid category and numeric amount.")
            return
        self.cursor.execute("UPDATE expenses SET category=?, amount=? WHERE id=?", (category, float(amount), expense_id))
        self.conn.commit()
        self.clear_form()
        self.load_expenses()

    def delete_expense(self):
        selected = self.tree.selection()
        if not selected:
            return
        expense_id = self.tree.item(selected[0])['values'][0]
        self.cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
        self.conn.commit()
        self.clear_form()
        self.load_expenses()

    def load_expenses(self):
        self.tree.delete(*self.tree.get_children())
        category_filter = self.filter_var.get()
        if category_filter and category_filter != "All":
            self.cursor.execute("SELECT * FROM expenses WHERE category=?", (category_filter,))
        else:
            self.cursor.execute("SELECT * FROM expenses")
        rows = self.cursor.fetchall()
        total = 0
        categories = set()
        for row in rows:
            self.tree.insert("", "end", values=row)
            total += row[2]
            categories.add(row[1])
        self.total_label.config(text=f"Total: ₹{total:.2f}")
        self.filter_combo["values"] = ["All"] + sorted(categories)
        if not self.filter_var.get():
            self.filter_var.set("All")

    def fill_form(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        item = self.tree.item(selected[0])['values']
        self.category_entry.delete(0, tk.END)
        self.category_entry.insert(0, item[1])
        self.amount_entry.delete(0, tk.END)
        self.amount_entry.insert(0, str(item[2]))

    def clear_form(self):
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.tree.selection_remove(self.tree.selection())

    def export_report(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                self.cursor.execute("SELECT * FROM expenses")
                rows = self.cursor.fetchall()
                total = 0
                f.write("Expense Report\n\n")
                for row in rows:
                    f.write(f"ID: {row[0]}, Category: {row[1]}, Amount: ₹{row[2]:.2f}\n")
                    total += row[2]
                f.write(f"\nTotal Expenses: ₹{total:.2f}")
            messagebox.showinfo("Exported", f"Report saved to:\n{file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
