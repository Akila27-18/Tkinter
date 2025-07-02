import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Text with Scrollbar")
root.geometry("400x300")

# Create a Frame to hold Text and Scrollbar together
frame = tk.Frame(root)
frame.pack(expand=True, fill="both", padx=10, pady=10)

# Create Text widget
text_area = tk.Text(frame, wrap="word", font=("Arial", 12))
text_area.pack(side="left", fill="both", expand=True)

# Create Scrollbar and link it to the Text widget
scrollbar = tk.Scrollbar(frame, command=text_area.yview)
scrollbar.pack(side="right", fill="y")

# Configure Text widget to use the Scrollbar
text_area.config(yscrollcommand=scrollbar.set)

# Optional: Insert large sample text
sample_text = "\n".join([f"Line {i}" for i in range(1, 51)])
text_area.insert("1.0", sample_text)

# Start the event loop
root.mainloop()
