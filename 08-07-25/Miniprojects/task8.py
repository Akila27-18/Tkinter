import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PyPDF2 import PdfMerger
import os

def add_file():
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    for f in files:
        if f not in pdf_files:
            pdf_files.append(f)
            listbox.insert(tk.END, os.path.basename(f))
            log_text.set(f"Added: {os.path.basename(f)}")

def remove_file():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        removed_file = pdf_files.pop(index)
        listbox.delete(index)
        log_text.set(f"Removed: {os.path.basename(removed_file)}")
    else:
        log_text.set("No file selected to remove.")

def merge_pdfs():
    if not pdf_files:
        messagebox.showwarning("No Files", "Please add PDF files to merge.")
        return
    
    output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF file", "*.pdf")])
    if not output_file:
        return

    try:
        merger = PdfMerger()
        for pdf in pdf_files:
            merger.append(pdf)
        merger.write(output_file)
        merger.close()
        messagebox.showinfo("Success", f"PDFs merged successfully into:\n{output_file}")
        log_text.set("Merge complete.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to merge PDFs:\n{e}")
        log_text.set("Merge failed.")

# Root window
root = tk.Tk()
root.title("PDF Merger")
root.geometry("600x400")

pdf_files = []
log_text = tk.StringVar()

# Toolbar Frame
toolbar = tk.Frame(root)
toolbar.pack(fill='x', padx=10, pady=5)

tk.Button(toolbar, text="Add File", command=add_file).pack(side='left', padx=5)
tk.Button(toolbar, text="Remove File", command=remove_file).pack(side='left', padx=5)
tk.Button(toolbar, text="Merge", command=merge_pdfs).pack(side='left', padx=5)

# PanedWindow
paned = tk.PanedWindow(root, orient=tk.VERTICAL)
paned.pack(fill='both', expand=True)

# Top: Listbox for files
top_frame = tk.Frame(paned)
listbox = tk.Listbox(top_frame, height=10)
listbox.pack(fill='both', expand=True, padx=10, pady=5)
paned.add(top_frame)

# Bottom: Log
bottom_frame = tk.Frame(paned)
tk.Label(bottom_frame, textvariable=log_text, anchor='w', fg='blue').pack(fill='x', padx=10, pady=5)
paned.add(bottom_frame)

root.mainloop()
