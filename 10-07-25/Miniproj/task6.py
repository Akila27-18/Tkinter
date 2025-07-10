import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
import threading

def search_files(folder, keyword, result_box, search_button):
    result_box.delete('1.0', tk.END)
    found = False

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                        for i, line in enumerate(lines, 1):
                            if keyword.lower() in line.lower():
                                result_box.insert(tk.END, f"{file} [Line {i}]: {line}")
                                found = True
                except Exception as e:
                    result_box.insert(tk.END, f"Error reading {file}: {e}\n")

    if not found:
        result_box.insert(tk.END, "No matches found.\n")
    search_button.config(state='normal')

def start_search(folder_path_var, keyword_entry, result_box, search_button):
    folder = folder_path_var.get()
    keyword = keyword_entry.get().strip()

    if not folder or not os.path.isdir(folder):
        messagebox.showerror("Error", "Please select a valid folder.")
        return

    if not keyword:
        messagebox.showerror("Error", "Please enter a keyword to search.")
        return

    search_button.config(state='disabled')
    thread = threading.Thread(target=search_files, args=(folder, keyword, result_box, search_button))
    thread.start()

def browse_folder(folder_path_var):
    folder = filedialog.askdirectory()
    if folder:
        folder_path_var.set(folder)

def main():
    root = tk.Tk()
    root.title("File Searcher - Keyword in .txt files")
    root.geometry("700x500")

    folder_path_var = tk.StringVar()

    # Folder selection
    tk.Label(root, text="Folder:").pack(anchor='w', padx=10, pady=(10,0))
    folder_frame = tk.Frame(root)
    folder_frame.pack(fill='x', padx=10)
    tk.Entry(folder_frame, textvariable=folder_path_var).pack(side='left', fill='x', expand=True)
    tk.Button(folder_frame, text="Browse", command=lambda: browse_folder(folder_path_var)).pack(side='right', padx=5)

    # Keyword input
    tk.Label(root, text="Keyword:").pack(anchor='w', padx=10, pady=(10,0))
    keyword_entry = tk.Entry(root)
    keyword_entry.pack(fill='x', padx=10)

    # Search button
    search_button = tk.Button(root, text="Search", command=lambda: start_search(folder_path_var, keyword_entry, result_box, search_button))
    search_button.pack(pady=10)

    # Results
    result_box = tk.Text(root, wrap='word')
    result_box.pack(fill='both', expand=True, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
