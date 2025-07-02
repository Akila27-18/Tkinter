import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Notepad")
root.geometry("600x400")  # Initial size

# Make window resizable in both directions (default, but for clarity)
root.resizable(True, True)

# Create a Text widget that fills the window
text_area = tk.Text(root, wrap="word", font=("Consolas", 12))
text_area.pack(fill="both", expand=True)

# Start the event loop
root.mainloop()
