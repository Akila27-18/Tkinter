import tkinter as tk

# Function to update character and word count
def update_count(event=None):
    content = text_area.get("1.0", tk.END).strip()
    char_count = len(content)
    word_count = len(content.split())
    count_label.config(text=f"Characters: {char_count} | Words: {word_count}")

# Create main window
root = tk.Tk()
root.title("Character & Word Counter")
root.geometry("400x300")

# Text widget
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both", padx=10, pady=(10, 0))

# Label to display the count
count_label = tk.Label(root, text="Characters: 0 | Words: 0", font=("Arial", 10))
count_label.pack(pady=5)

# Bind any key release to update the count
text_area.bind("<KeyRelease>", update_count)

# Start the event loop
root.mainloop()
