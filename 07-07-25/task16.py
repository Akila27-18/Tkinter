import tkinter as tk

def update_counts(event=None):
    text = input_text.get("1.0", tk.END).strip()
    char_count = len(text)
    word_count = len(text.split())

    char_label.config(text=f"Characters: {char_count}")
    word_label.config(text=f"Words: {word_count}")

def clear_text():
    input_text.delete("1.0", tk.END)
    update_counts()

def reset_all():
    clear_text()
    char_label.config(text="Characters: 0")
    word_label.config(text="Words: 0")

# Main window
root = tk.Tk()
root.title("Live Character & Word Counter")
root.geometry("500x350")

# Text widget
input_text = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
input_text.place(x=20, y=20, width=460, height=200)
input_text.bind("<KeyRelease>", update_counts)

# Labels
char_label = tk.Label(root, text="Characters: 0", font=("Arial", 10))
char_label.place(x=20, y=230)

word_label = tk.Label(root, text="Words: 0", font=("Arial", 10))
word_label.place(x=150, y=230)

# Buttons
clear_button = tk.Button(root, text="Clear", command=clear_text, bg="orange", width=10)
clear_button.place(x=300, y=225)

reset_button = tk.Button(root, text="Reset", command=reset_all, bg="red", fg="white", width=10)
reset_button.place(x=390, y=225)

root.mainloop()
