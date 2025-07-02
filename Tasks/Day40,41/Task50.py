import tkinter as tk
from tkinter import messagebox
import datetime

# Function to save diary entry
def save_entry():
    content = text_area.get("1.0", tk.END).strip()
    if not content:
        messagebox.showwarning("Empty Entry", "Diary entry is empty.")
        return
    
    today = datetime.date.today().strftime("%Y-%m-%d")
    filename = f"diary_{today}.txt"
    
    try:
        with open(filename, "w") as file:
            file.write(content)
        messagebox.showinfo("Saved", f"Entry saved to {filename}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save: {e}")

# Create main window
root = tk.Tk()
root.title("Mini Diary App")
root.geometry("500x400")

# Heading
tk.Label(root, text="My Diary Entry", font=("Helvetica", 14, "bold")).pack(pady=5)

# Text widget for diary input
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both", padx=10, pady=(0, 10))

# Save button
save_button = tk.Button(root, text="Save Entry", command=save_entry, font=("Arial", 11))
save_button.pack(pady=5)

# Start the event loop
root.mainloop()
