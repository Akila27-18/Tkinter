import tkinter as tk
from tkinter import filedialog, messagebox

class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad with Save Confirmation")
        self.root.geometry("600x400")

        # Track if text is modified
        self.text_modified = False
        self.filename = None

        # Text Area
        self.text = tk.Text(self.root, wrap="word", undo=True)
        self.text.pack(fill="both", expand=True)
        self.text.bind("<<Modified>>", self.on_modified)

        # Menu
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save", command=self.save_file)
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu=menubar)

        # Handle close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_modified(self, event):
        self.text_modified = True
        self.text.edit_modified(False)  # reset flag

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            content = self.text.get("1.0", "end-1c")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            self.filename = file_path
            self.text_modified = False
            messagebox.showinfo("Saved", "File saved successfully.")

    def on_closing(self):
        if self.text_modified:
            save_changes = messagebox.askyesno("Exit", "Do you want to save changes before exiting?")
            if save_changes:
                self.save_file()
        self.root.destroy()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
