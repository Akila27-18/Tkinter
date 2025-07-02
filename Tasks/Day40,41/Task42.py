import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Text Insert Example")
root.geometry("400x300")

# Create a Text widget
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both", padx=10, pady=10)

# Insert sample paragraph using insert()
sample_text = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
)
text_area.insert("1.0", sample_text)  # Insert at the beginning (line 1, character 0)

# Run the application
root.mainloop()
