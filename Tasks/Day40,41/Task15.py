import tkinter as tk

# Function to display entered text
def display_text():
    entered = entry.get()
    result_label.config(text=f"You entered: {entered}")

# Create main window
root = tk.Tk()
root.title("Entry Display Example")
root.geometry("300x150")

# Entry field
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

# Button to trigger display
btn = tk.Button(root, text="Show Text", command=display_text)
btn.pack(pady=5)

# Label to show result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the event loop
root.mainloop()
