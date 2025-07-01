import tkinter as tk
from tkinter import messagebox
import pandas as pd

def load_excel_file():
    file_path = entry.get()
    try:
        df = pd.read_excel(file_path)  # Use pandas to read Excel
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, df.to_string(index=False))
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# GUI setup
root = tk.Tk()
root.title("Excel File Viewer")
root.geometry("600x500")

entry = tk.Entry(root, width=60)
entry.insert(0, r"C:\Users\sharm\Desktop\Akila_Project_links.xlsx")  # You can modify this path
entry.pack(pady=10)

button = tk.Button(root, text="Load Excel File", command=load_excel_file)
button.pack(pady=5)

text_box = tk.Text(root, wrap='word')
text_box.pack(padx=10, pady=10, fill='both', expand=True)

root.mainloop()
