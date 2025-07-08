import tkinter as tk
from tkinter import messagebox

class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard")
        self.root.geometry("800x500")

        self.create_menu()
        self.create_toolbar()
        self.create_layout()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        manage_menu = tk.Menu(menubar, tearoff=0)
        manage_menu.add_command(label="Users", command=lambda: self.update_content("Users"))
        manage_menu.add_command(label="Roles", command=lambda: self.update_content("Roles"))
        manage_menu.add_command(label="Reports", command=lambda: self.update_content("Reports"))
        menubar.add_cascade(label="Manage", menu=manage_menu)
        self.root.config(menu=menubar)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED)
        for action in ["Add", "Edit", "Delete"]:
            btn = tk.Button(toolbar, text=action, width=10, command=lambda a=action: self.handle_action(a))
            btn.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

    def create_layout(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Left Navigation Menu
        nav_frame = tk.Frame(main_frame, width=200, bg="#dfe6e9")
        nav_frame.pack(side=tk.LEFT, fill=tk.Y)
        nav_items = ["Dashboard", "Users", "Roles", "Settings"]
        for item in nav_items:
            btn = tk.Button(nav_frame, text=item, width=20, anchor="w",
                            command=lambda i=item: self.update_content(i))
            btn.pack(pady=5, padx=10, anchor="w")

        # Right Content Area
        self.content_frame = tk.Frame(main_frame, bg="white")
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.content_label = tk.Label(self.content_frame, text="Welcome to the Admin Panel",
                                      font=("Arial", 16), bg="white")
        self.content_label.pack(pady=50)

    def update_content(self, section):
        self.content_label.config(text=f"Currently Viewing: {section}")

    def handle_action(self, action):
        if action == "Add":
            self.open_add_user_dialog()
        else:
            messagebox.showinfo(action, f"{action} action triggered.")

    def open_add_user_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add New User")
        dialog.geometry("300x250")

        tk.Label(dialog, text="Username:").grid(row=0, column=0, pady=10, padx=10, sticky="e")
        username_entry = tk.Entry(dialog)
        username_entry.grid(row=0, column=1, padx=10)

        tk.Label(dialog, text="Email:").grid(row=1, column=0, pady=10, padx=10, sticky="e")
        email_entry = tk.Entry(dialog)
        email_entry.grid(row=1, column=1, padx=10)

        tk.Label(dialog, text="Role:").grid(row=2, column=0, pady=10, padx=10, sticky="e")
        role_entry = tk.Entry(dialog)
        role_entry.grid(row=2, column=1, padx=10)

        def submit_user():
            user = username_entry.get()
            email = email_entry.get()
            role = role_entry.get()
            if not user or not email or not role:
                messagebox.showwarning("Missing Info", "Please fill all fields.")
                return
            messagebox.showinfo("User Added", f"Added {user} with role {role}")
            dialog.destroy()

        submit_btn = tk.Button(dialog, text="Add User", command=submit_user)
        submit_btn.grid(row=3, column=1, pady=20, sticky="e")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminDashboard(root)
    root.mainloop()
