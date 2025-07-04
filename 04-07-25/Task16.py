import tkinter as tk

def update_count(event=None):
    content = text_input.get("1.0", tk.END).strip()
    char_count = len(content)
    word_count = len(content.split())
    label_count.config(text=f"Characters: {char_count}   Words: {word_count}")

def reset_text():
    text_input.delete("1.0", tk.END)
    update_count()

# Root window
root = tk.Tk()
root.title("Live Typing Tracker")
root.geometry("400x300")

# Text widget
text_input = tk.Text(root, wrap="word", height=10, width=40)
text_input.pack(pady=10)
text_input.bind("<Key>", update_count)

# Count label
label_count = tk.Label(root, text="Characters: 0   Words: 0", font=("Arial", 12))
label_count.pack(pady=5)

# Reset button
reset_btn = tk.Button(root, text="Reset", command=reset_text, bg="red", fg="white")
reset_btn.pack(pady=10)

root.mainloop()
