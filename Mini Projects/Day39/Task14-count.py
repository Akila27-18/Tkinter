import tkinter as tk

def count_words():
    text = text_box.get("1.0", tk.END)  # Get all text from the Text widget
    words = text.strip().split()
    word_count = len(words)
    result_label.config(text=f"Word Count: {word_count}")

# GUI setup
root = tk.Tk()
root.title("Word Counter")
root.geometry("400x300")

# Instructions
tk.Label(root, text="Type or paste your text below:").pack(pady=5)

# Multi-line Text Box
text_box = tk.Text(root, wrap='word', height=10)
text_box.pack(padx=10, pady=5, fill='both', expand=True)

# Count Button
tk.Button(root, text="Count Words", command=count_words).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Word Count: 0", font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()
