import tkinter as tk

# Function to print all content from the Text widget
def print_text():
    content = text_area.get("1.0", tk.END).strip()
    print("Text Content:")
    print(content)

# Create main window
root = tk.Tk()
root.title("Text Get Example")
root.geometry("400x300")

# Text widget
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both", padx=10, pady=10)

# Button to get and print content
btn = tk.Button(root, text="Print Text", command=print_text)
btn.pack(pady=10)

# Insert some sample text for testing
text_area.insert("1.0", "Type something here...\nOr use the print button to see what's typed.")

# Start the event loop
root.mainloop()
