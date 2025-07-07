import tkinter as tk
from tkinter import messagebox

class ContactBookManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book Manager")
        self.root.geometry("400x400")

        # Input Frame
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        # Name Entry
        tk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky="e")
        self.name_var = tk.StringVar()
        self.name_entry = tk.Entry(input_frame, textvariable=self.name_var, width=25)
        self.name_entry.grid(row=0, column=1, padx=5)

        # Phone Entry
        tk.Label(input_frame, text="Phone:").grid(row=1, column=0, sticky="e")
        self.phone_var = tk.StringVar()
        self.phone_entry = tk.Entry(input_frame, textvariable=self.phone_var, width=25)
        self.phone_entry.grid(row=1, column=1, padx=5)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Add Contact", width=12, command=self.add_contact).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Delete Selected", width=12, command=self.delete_selected).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Clear All", width=12, command=self.clear_all).grid(row=0, column=2, padx=5)

        # Listbox with Scrollbar
        list_frame = tk.Frame(root)
        list_frame.pack(pady=10)

        self.scrollbar = tk.Scrollbar(list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.contact_listbox = tk.Listbox(list_frame, height=10, width=45, yscrollcommand=self.scrollbar.set)
        self.contact_listbox.pack()
        self.scrollbar.config(command=self.contact_listbox.yview)

    def add_contact(self):
        name = self.name_var.get().strip()
        phone = self.phone_var.get().strip()

        # Validations
        if not name:
            messagebox.showerror("Validation Error", "Name cannot be empty.")
            return
        if not phone.isdigit():
            messagebox.showerror("Validation Error", "Phone number must contain only digits.")
            return

        contact = f"{name} - {phone}"
        self.contact_listbox.insert(tk.END, contact)
        self.name_var.set("")
        self.phone_var.set("")

    def delete_selected(self):
        selected = self.contact_listbox.curselection()
        if not selected:
            messagebox.showwarning("Delete Contact", "No contact selected.")
            return
        for index in reversed(selected):
            self.contact_listbox.delete(index)

    def clear_all(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to delete all contacts?"):
            self.contact_listbox.delete(0, tk.END)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookManager(root)
    root.mainloop()
