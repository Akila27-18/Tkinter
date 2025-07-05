import tkinter as tk

def update_count(event=None):
    content = text_box.get("1.0", "end-1c")  # exclude final newline
    char_count = len(content)
    count_label.config(text=f"Characters: {char_count}")

def clear_text():
    text_box.delete("1.0", tk.END)
    update_count()

# Main window
root = tk.Tk()
root.title("Live Typing Tracker")
root.geometry("400x300")

# Text widget for typing
text_box = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
text_box.place(x=20, y=20, width=360, height=180)
text_box.bind("<Key>", update_count)

# Character count label
count_label = tk.Label(root, text="Characters: 0", font=("Arial", 10))
count_label.place(x=20, y=210)

# Clear button
clear_button = tk.Button(root, text="Clear", command=clear_text)
clear_button.place(x=320, y=210)

root.mainloop()
