import tkinter as tk
from tkinter import messagebox, filedialog

contacts = []

def refresh_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, contact['name'])

def clear_form():
    name_var.set("")
    phone_var.set("")
    email_var.set("")

def add_contact():
    name = name_var.get().strip()
    phone = phone_var.get().strip()
    email = email_var.get().strip()

    if not name:
        messagebox.showwarning("Missing", "Name is required.")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    refresh_list()
    clear_form()

def on_select(event):
    if contact_list.curselection():
        index = contact_list.curselection()[0]
        contact = contacts[index]
        name_var.set(contact["name"])
        phone_var.set(contact["phone"])
        email_var.set(contact["email"])

def edit_contact():
    if not contact_list.curselection():
        messagebox.showwarning("Select", "No contact selected.")
        return

    index = contact_list.curselection()[0]
    contacts[index] = {
        "name": name_var.get().strip(),
        "phone": phone_var.get().strip(),
        "email": email_var.get().strip()
    }
    refresh_list()

def delete_contact():
    if not contact_list.curselection():
        messagebox.showwarning("Select", "No contact selected.")
        return
    if messagebox.askyesno("Confirm", "Delete selected contact?"):
        index = contact_list.curselection()[0]
        contacts.pop(index)
        refresh_list()
        clear_form()

def export_contacts():
    if not contacts:
        messagebox.showinfo("No Data", "No contacts to export.")
        return

    if messagebox.askyesno("Export", "Export all contacts to file?"):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                for c in contacts:
                    f.write(f"{c['name']} | {c['phone']} | {c['email']}\n")
            messagebox.showinfo("Exported", f"Contacts exported to:\n{file_path}")

def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.quit()

# --- Main Window ---
root = tk.Tk()
root.title("Contact Book")
root.geometry("700x400")

# --- Menu Bar ---
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Export", command=export_contacts)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

# --- Toolbar ---
toolbar = tk.Frame(root, bg="#e0e0e0")
toolbar.pack(side="top", fill="x")

tk.Button(toolbar, text="Add", width=8, command=add_contact).pack(side="left", padx=2, pady=2)
tk.Button(toolbar, text="Edit", width=8, command=edit_contact).pack(side="left", padx=2, pady=2)
tk.Button(toolbar, text="Delete", width=8, command=delete_contact).pack(side="left", padx=2, pady=2)

# --- PanedWindow Layout ---
paned = tk.PanedWindow(root, orient=tk.HORIZONTAL)
paned.pack(fill=tk.BOTH, expand=True)

# --- Left Pane: Contact List ---
left_frame = tk.Frame(paned)
tk.Label(left_frame, text="Contacts").pack()
contact_list = tk.Listbox(left_frame)
contact_list.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
contact_list.bind("<<ListboxSelect>>", on_select)
paned.add(left_frame, minsize=200)

# --- Right Pane: Form ---
right_frame = tk.Frame(paned, padx=10, pady=10)
tk.Label(right_frame, text="Name:").grid(row=0, column=0, sticky="e")
tk.Label(right_frame, text="Phone:").grid(row=1, column=0, sticky="e")
tk.Label(right_frame, text="Email:").grid(row=2, column=0, sticky="e")

name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()

tk.Entry(right_frame, textvariable=name_var, width=30).grid(row=0, column=1, pady=5)
tk.Entry(right_frame, textvariable=phone_var, width=30).grid(row=1, column=1, pady=5)
tk.Entry(right_frame, textvariable=email_var, width=30).grid(row=2, column=1, pady=5)

paned.add(right_frame)

root.mainloop()
