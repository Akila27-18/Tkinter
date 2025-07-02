import tkinter as tk
from tkinter import filedialog

# Function to open and load file content
def load_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_area.delete("1.0", tk.END)  # Clear existing content
            text_area.insert("1.0", content)

# Create main window
root = tk.Tk()
root.title("Load Text File")
root.geometry("500x300")

# Text widget
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both", padx=10, pady=10)

# Load file button
load_button = tk.Button(root, text="Load File", command=load_file)
load_button.pack(pady=5)

# Start the event loop
root.mainloop()
