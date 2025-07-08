import tkinter as tk
from tkinter import ttk, messagebox

# Sample user list
users = ["Alice", "Bob", "Charlie", "Diana"]

# ----- Main App Window -----
root = tk.Tk()
root.title("Multi-User Login Panel")
root.geometry("400x200")

# Create StringVar AFTER root
current_user = tk.StringVar(value="Not logged in")

# ----- Switch User Dialog -----
def open_switch_user_dialog():
    def login():
        selected = user_var.get()
        if selected:
            current_user.set(selected)
            dialog.destroy()
            messagebox.showinfo("Login Successful", f"Logged in as {selected}")
        else:
            messagebox.showwarning("Select User", "Please select a username.")

    dialog = tk.Toplevel(root)
    dialog.title("Switch User")
    dialog.geometry("300x150")
    dialog.grab_set()  # Modal

    tk.Label(dialog, text="Select Username:").pack(pady=10)
    user_var = tk.StringVar()
    ttk.Combobox(dialog, textvariable=user_var, values=users, state="readonly").pack()

    tk.Button(dialog, text="Login", command=login).pack(pady=10)

# ----- Menu Actions -----
def logout_user():
    if current_user.get() != "Not logged in":
        confirm = messagebox.askyesno("Confirm Logout", "Do you want to logout?")
        if confirm:
            current_user.set("Not logged in")
            messagebox.showinfo("Logged Out", "User has been logged out.")
    else:
        messagebox.showinfo("No User", "No user is currently logged in.")

# ----- Menu -----
menubar = tk.Menu(root)
user_menu = tk.Menu(menubar, tearoff=0)
user_menu.add_command(label="Logout", command=logout_user)
user_menu.add_separator()
user_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="User", menu=user_menu)
root.config(menu=menubar)

# ----- Main Frame -----
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(expand=True, fill='both')

tk.Label(main_frame, text="Current User:", font=('Arial', 12)).pack(pady=5)
tk.Label(main_frame, textvariable=current_user, font=('Arial', 14, 'bold'), fg="blue").pack()

tk.Button(main_frame, text="Switch User", command=open_switch_user_dialog).pack(pady=20)

root.mainloop()
