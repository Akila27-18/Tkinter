import tkinter as tk
import time

# Function to auto-save content
def auto_save():
    content = text_area.get("1.0", tk.END).strip()
    if content:
        with open("autosave.txt", "w") as f:
            f.write(content)
        print(f"Auto-saved at {time.strftime('%H:%M:%S')}")
    
    # Schedule next auto-save in 5000 milliseconds (5 seconds)
    root.after(5000, auto_save)

# Create main window
root = tk.Tk()
root.title("Auto-Save Notepad")
root.geometry("400x300")

# Create Text widget
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both", padx=10, pady=10)

# Start the auto-save loop
auto_save()

# Run the event loop
root.mainloop()
