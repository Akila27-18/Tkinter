import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3

class DatabaseViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Viewer")
        self.root.geometry("800x600")
        self.conn = None
        self.cursor = None
        self.table_name = "students"  # Change to match your DB table

        # ==== Menu ====
        menubar = tk.Menu(self.root)
        datamenu = tk.Menu(menubar, tearoff=0)
        datamenu.add_command(label="Load DB", command=self.load_db)
        datamenu.add_separator()
        datamenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="Data", menu=datamenu)
        self.root.config(menu=menubar)

        # ==== Toolbar ====
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#f0f0f0")
        refresh_btn = ttk.Button(toolbar, text="Refresh", command=self.refresh_data)
        filter_btn = ttk.Button(toolbar, text="Filter", command=self.apply_filter)
        refresh_btn.pack(side=tk.LEFT, padx=5, pady=5)
        filter_btn.pack(side=tk.LEFT, padx=5, pady=5)
        toolbar.pack(fill=tk.X)

        # ==== Paned Window ====
        paned = ttk.PanedWindow(self.root, orient=tk.VERTICAL)
        paned.pack(fill=tk.BOTH, expand=True)

        # ==== Filter Frame (Top Panel) ====
        top_frame = tk.Frame(paned, height=50)
        tk.Label(top_frame, text="Search:").pack(side=tk.LEFT, padx=5)
        self.search_entry = ttk.Entry(top_frame, width=40)
        self.search_entry.pack(side=tk.LEFT, padx=5)
        paned.add(top_frame, weight=1)

        # ==== Table Frame (Bottom Panel) ====
        bottom_frame = tk.Frame(paned)
        self.tree = ttk.Treeview(bottom_frame, columns=[], show="headings")
        self.tree.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        scroll = ttk.Scrollbar(bottom_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.config(yscrollcommand=scroll.set)

        paned.add(bottom_frame, weight=4)

    # ==== Load DB ====
    def load_db(self):
        db_path = filedialog.askopenfilename(filetypes=[("SQLite Database", "*.db")])
        if db_path:
            try:
                self.conn = sqlite3.connect(db_path)
                self.cursor = self.conn.cursor()
                messagebox.showinfo("Success", "Database loaded successfully.")
                self.refresh_data()
            except Exception as e:
                messagebox.showerror("Error", f"Could not load database.\n{e}")

    # ==== Refresh ====
    def refresh_data(self):
        if not self.cursor:
            return
        try:
            self.cursor.execute(f"SELECT * FROM {self.table_name}")
            rows = self.cursor.fetchall()
            columns = [desc[0] for desc in self.cursor.description]

            # Update Treeview
            self.tree.config(columns=columns)
            for col in columns:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=100)

            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Could not fetch data.\n{e}")

    # ==== Filter ====
    def apply_filter(self):
        if not self.cursor:
            return
        keyword = self.search_entry.get().strip()
        try:
            query = f"SELECT * FROM {self.table_name} WHERE name LIKE ?"  # Modify for your table
            self.cursor.execute(query, ('%' + keyword + '%',))
            rows = self.cursor.fetchall()

            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Could not apply filter.\n{e}")

# ==== Run App ====
if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseViewer(root)
    root.mainloop()
