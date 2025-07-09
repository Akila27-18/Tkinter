import tkinter as tk

def update_count(event):
    text = entry.get()
    char_count = len(text)
    count_label.config(text=f"Characters: {char_count}")

# GUI Setup
root = tk.Tk()
root.title("Character Counter")
root.geometry("300x150")

tk.Label(root, text="Type something:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack()

count_label = tk.Label(root, text="Characters: 0", font=("Arial", 12), fg="blue")
count_label.pack(pady=10)

# Bind KeyRelease event
entry.bind("<KeyRelease>", update_count)

root.mainloop()
