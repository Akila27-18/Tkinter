import tkinter as tk
from tkinter import ttk, messagebox

# Sample email data
EMAILS = [
    {"from": "alice@example.com", "subject": "Meeting Schedule", "body": "Let's meet at 3 PM tomorrow."},
    {"from": "bob@example.com", "subject": "Project Update", "body": "The project is on track for release."},
    {"from": "carol@example.com", "subject": "Invitation", "body": "You're invited to our annual gala!"},
]

class EmailClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Client")

        self.create_menu()
        self.create_toolbar()
        self.create_split_screen()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Compose", command=self.open_compose_dialog)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu=menubar)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED)
        for text in ["Reply", "Forward", "Delete"]:
            btn = tk.Button(toolbar, text=text, command=lambda t=text: self.toolbar_action(t))
            btn.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

    def toolbar_action(self, action):
        selected = self.inbox_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "No message selected.")
            return
        messagebox.showinfo(action, f"{action} selected message.")

    def create_split_screen(self):
        paned = tk.PanedWindow(self.root, orient=tk.HORIZONTAL, sashrelief=tk.RAISED)
        paned.pack(fill=tk.BOTH, expand=1)

        # Left Pane - Inbox List
        left_frame = tk.Frame(paned, padx=5, pady=5)
        self.inbox_listbox = tk.Listbox(left_frame, width=30)
        self.inbox_listbox.pack(fill=tk.BOTH, expand=True)
        self.inbox_listbox.bind("<<ListboxSelect>>", self.show_message)

        # Populate inbox
        for email in EMAILS:
            self.inbox_listbox.insert(tk.END, f"{email['from']}: {email['subject']}")

        paned.add(left_frame)

        # Right Pane - Message Preview
        right_frame = tk.Frame(paned, padx=5, pady=5)
        self.preview_text = tk.Text(right_frame, wrap=tk.WORD)
        self.preview_text.pack(fill=tk.BOTH, expand=True)
        paned.add(right_frame)

    def show_message(self, event):
        index = self.inbox_listbox.curselection()
        if not index:
            return
        email = EMAILS[index[0]]
        content = f"From: {email['from']}\nSubject: {email['subject']}\n\n{email['body']}"
        self.preview_text.delete(1.0, tk.END)
        self.preview_text.insert(tk.END, content)

    def open_compose_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Compose Email")
        dialog.geometry("400x300")

        # To
        tk.Label(dialog, text="To:").grid(row=0, column=0, sticky="e")
        to_entry = tk.Entry(dialog, width=40)
        to_entry.grid(row=0, column=1, pady=5)

        # Subject
        tk.Label(dialog, text="Subject:").grid(row=1, column=0, sticky="e")
        subject_entry = tk.Entry(dialog, width=40)
        subject_entry.grid(row=1, column=1, pady=5)

        # Body
        tk.Label(dialog, text="Body:").grid(row=2, column=0, sticky="ne")
        body_text = tk.Text(dialog, width=40, height=10)
        body_text.grid(row=2, column=1, pady=5)

        # Send button
        def send_email():
            to = to_entry.get()
            subject = subject_entry.get()
            body = body_text.get("1.0", tk.END).strip()
            if not to or not subject or not body:
                messagebox.showwarning("Incomplete", "All fields are required.")
                return
            messagebox.showinfo("Sent", f"Email sent to {to}")
            dialog.destroy()

        send_btn = tk.Button(dialog, text="Send", command=send_email)
        send_btn.grid(row=3, column=1, pady=10, sticky="e")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailClient(root)
    root.geometry("700x400")
    root.mainloop()
