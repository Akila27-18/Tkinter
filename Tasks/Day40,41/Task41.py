import tkinter as tk
from tkinter import filedialog

# Function to save text content to file
def save_to_file():
    content = text_area.get("1.0", tk.END).strip()
    if content:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)

# Create main window
root = tk.Tk()
root.title("Note Saver")
root.geometry("400x300")

# Text widget for writing notes
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both", padx=10, pady=10)

# Save button
save_button = tk.Button(root, text="Save Notes", command=save_to_file)
save_button.pack(pady=5)

# Start the event loop
root.mainloop()
