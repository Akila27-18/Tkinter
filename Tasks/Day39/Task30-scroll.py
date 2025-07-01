import tkinter as tk

# Main window
root = tk.Tk()
root.title("Text Widget with Scrollbar")
root.geometry("400x250")

# Frame to hold both Text and Scrollbar
frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Create Text widget
text_box = tk.Text(frame, wrap="word", width=40, height=10)
text_box.pack(side="left", fill="both", expand=True)

# Create Scrollbar and link to Text
scrollbar = tk.Scrollbar(frame, command=text_box.yview)
scrollbar.pack(side="right", fill="y")

# Connect Text to Scrollbar
text_box.config(yscrollcommand=scrollbar.set)

# Sample text to fill space
sample_text = "\n".join([f"Line {i}" for i in range(1, 51)])
text_box.insert("1.0", sample_text)

root.mainloop()
