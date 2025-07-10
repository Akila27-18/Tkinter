import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import threading
import time

def browse_source(source_var):
    folder = filedialog.askdirectory()
    if folder:
        source_var.set(folder)

def browse_target(target_var):
    folder = filedialog.askdirectory()
    if folder:
        target_var.set(folder)

def copy_txt_files(source, target, update_callback, done_callback):
    copied = 0
    try:
        for file in os.listdir(source):
            if file.endswith(".txt"):
                src_path = os.path.join(source, file)
                dst_path = os.path.join(target, file)
                shutil.copy2(src_path, dst_path)
                copied += 1
                time.sleep(0.5)  # Simulate delay
                update_callback(copied)
    except Exception as e:
        messagebox.showerror("Error", f"Copy failed: {e}")
    finally:
        done_callback()

def start_copy(source_var, target_var, counter_label, copy_btn, root):
    source = source_var.get()
    target = target_var.get()

    if not os.path.isdir(source) or not os.path.isdir(target):
        messagebox.showerror("Error", "Please select valid source and target folders.")
        return

    copy_btn.config(state='disabled')
    counter_label.config(text="Copied: 0")

    def update_count(count):
        root.after(0, lambda: counter_label.config(text=f"Copied: {count}"))

    def on_done():
        root.after(0, lambda: copy_btn.config(state='normal'))

    thread = threading.Thread(target=copy_txt_files, args=(source, target, update_count, on_done))
    thread.start()

def main():
    root = tk.Tk()
    root.title("Directory Backup Utility")
    root.geometry("500x300")

    source_var = tk.StringVar()
    target_var = tk.StringVar()

    # Source Folder
    tk.Label(root, text="Source Folder:").pack(anchor='w', padx=10, pady=(10, 0))
    source_frame = tk.Frame(root)
    source_frame.pack(fill='x', padx=10)
    tk.Entry(source_frame, textvariable=source_var).pack(side='left', fill='x', expand=True)
    tk.Button(source_frame, text="Browse", command=lambda: browse_source(source_var)).pack(side='right', padx=5)

    # Target Folder
    tk.Label(root, text="Target (Backup) Folder:").pack(anchor='w', padx=10, pady=(10, 0))
    target_frame = tk.Frame(root)
    target_frame.pack(fill='x', padx=10)
    tk.Entry(target_frame, textvariable=target_var).pack(side='left', fill='x', expand=True)
    tk.Button(target_frame, text="Browse", command=lambda: browse_target(target_var)).pack(side='right', padx=5)

    # Copy Button & Status
    counter_label = tk.Label(root, text="Copied: 0", font=('Arial', 12))
    counter_label.pack(pady=10)

    copy_btn = tk.Button(root, text="Start Backup", font=('Arial', 12, 'bold'),
                         command=lambda: start_copy(source_var, target_var, counter_label, copy_btn, root))
    copy_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
