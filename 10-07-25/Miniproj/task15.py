import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import os

def open_txt_file():
    file_path = filedialog.askopenfilename(
        title="Open TXT File",
        filetypes=[("Text Files", "*.txt")]
    )
    if not file_path:
        return

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    parsed_data = []
    for line in lines:
        line = line.strip()
        if line:  # Skip empty lines
            # Assume tab, comma, or space delimited
            if ',' in line:
                parsed_data.append(line.split(','))
            elif '\t' in line:
                parsed_data.append(line.split('\t'))
            else:
                parsed_data.append(line.split())

    if not parsed_data:
        messagebox.showwarning("No Data", "The selected file contains no parsable data.")
        return

    save_csv_file(parsed_data)

def save_csv_file(data):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv")],
        title="Save as CSV"
    )
    if not file_path:
        return

    try:
        with open(file_path, "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        messagebox.showinfo("Success", f"File saved successfully:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file:\n{e}")

# GUI Setup
root = tk.Tk()
root.title("TXT to CSV Converter")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="TXT to CSV Converter", font=("Arial", 16, "bold")).pack(pady=20)

tk.Button(
    root,
    text="Open .txt and Convert to .csv",
    command=open_txt_file,
    font=("Arial", 12),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5
).pack(pady=10)

tk.Label(root, text="Supports tab, comma, or space-separated data.", font=("Arial", 9)).pack(pady=5)

root.mainloop()
