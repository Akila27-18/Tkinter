import tkinter as tk
from tkinter import filedialog, messagebox

def save_file():
    if messagebox.askyesno("Confirm Save", "Do you want to save the file?"):
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if path:
            with open(path, "w") as f:
                f.write(text.get("1.0", tk.END))
            messagebox.showinfo("Saved", "File saved successfully!")
    else:
        messagebox.showinfo("Cancelled", "Save cancelled.")

root = tk.Tk()
root.title("Save Confirmation")

text = tk.Text(root, width=60, height=20)
text.pack(padx=10, pady=10)

tk.Button(root, text="Save", command=save_file).pack(pady=10)

root.mainloop()
