import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

class MiniNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Notepad")
        self.root.geometry("700x500")

        # Track current file path
        self.current_file = None

        # ==== Menu Bar ====
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.confirm_exit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu=menubar)

        # ==== Toolbar Frame ====
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#f0f0f0")
        open_btn = ttk.Button(toolbar, text="Open", command=self.open_file)
        save_btn = ttk.Button(toolbar, text="Save", command=self.save_file)
        open_btn.pack(side=tk.LEFT, padx=5, pady=5)
        save_btn.pack(side=tk.LEFT, padx=5, pady=5)
        toolbar.pack(fill=tk.X)

        # ==== Text Area Frame ====
        text_frame = tk.Frame(self.root)
        text_frame.pack(fill=tk.BOTH, expand=True)

        self.text_area = tk.Text(text_frame, wrap="word", font=("Arial", 12))
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scroll = tk.Scrollbar(text_frame, command=self.text_area.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=scroll.set)

        # ==== Handle Window Close (X) ====
        self.root.protocol("WM_DELETE_WINDOW", self.confirm_exit)

    # ==== File Operations ====
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.root.title("Mini Notepad - New File")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)
            self.current_file = file_path
            self.root.title(f"Mini Notepad - {file_path}")

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            messagebox.showinfo("Saved", "File saved successfully.")
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text Files", "*.txt")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.current_file = file_path
                self.root.title(f"Mini Notepad - {file_path}")
                messagebox.showinfo("Saved", "File saved successfully.")

    def confirm_exit(self):
        if messagebox.askokcancel("Exit", "Do you really want to exit?"):
            self.root.destroy()

# ==== Run App ====
if __name__ == "__main__":
    root = tk.Tk()
    app = MiniNotepad(root)
    root.mainloop()
