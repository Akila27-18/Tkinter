import tkinter as tk

# Function to clear the text area
def clear_text():
    text_area.delete("1.0", tk.END)  # Delete from beginning to end

# Create main window
root = tk.Tk()
root.title("Clear Text Example")
root.geometry("400x300")

# Text widget
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both", padx=10, pady=10)

# Insert some sample text
text_area.insert("1.0", "This is some sample text. Click the button to clear it.")

# Button to clear the text
clear_btn = tk.Button(root, text="Clear Text", command=clear_text)
clear_btn.pack(pady=10)

# Start the event loop
root.mainloop()
