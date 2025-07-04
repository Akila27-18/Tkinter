import tkinter as tk
from tkinter import ttk, messagebox

# Sample Poll Data
polls = {
    "Favorite Fruit": ["Apple", "Banana", "Mango", "Grapes", "Orange", "Pineapple", "Strawberry", "Watermelon", "Guava", "Papaya", "Kiwi"],
    "Preferred Language": ["Python", "Java", "C++", "JavaScript", "C#", "Go", "Rust", "Kotlin"],
    "Best Season": ["Summer", "Winter", "Monsoon", "Spring"]
}

# Vote storage {question: {option: count}}
vote_counts = {q: {opt: 0 for opt in options} for q, options in polls.items()}

# Tkinter App
root = tk.Tk()
root.title("Simple Polling App")
root.geometry("500x400")

# ---- Poll Question Selector ----
tk.Label(root, text="Choose Poll Question:").pack(pady=5)
question_var = tk.StringVar()
question_combo = ttk.Combobox(root, textvariable=question_var, values=list(polls.keys()), state="readonly", width=40)
question_combo.pack(pady=5)
question_combo.set("Favorite Fruit")

# ---- Listbox with Scrollbar ----
list_frame = tk.Frame(root)
list_frame.pack(pady=10, fill="both", expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

option_listbox = tk.Listbox(list_frame, height=10, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
option_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=option_listbox.yview)

# ---- Load Options ----
def load_options(event=None):
    option_listbox.delete(0, tk.END)
    selected_question = question_var.get()
    for opt, count in vote_counts[selected_question].items():
        option_listbox.insert(tk.END, f"{opt} ({count} votes)")

question_combo.bind("<<ComboboxSelected>>", load_options)

# ---- Submit Vote ----
def submit_vote():
    question = question_var.get()
    selection = option_listbox.curselection()
    if not selection:
        messagebox.showwarning("No selection", "Please select an option to vote.")
        return
    index = selection[0]
    selected_line = option_listbox.get(index)
    selected_option = selected_line.split(" (")[0]

    # Increment vote
    vote_counts[question][selected_option] += 1
    load_options()

    messagebox.showinfo("Vote Recorded", f"You voted for: {selected_option}")

# ---- Submit Button ----
vote_btn = tk.Button(root, text="Submit Vote", command=submit_vote)
vote_btn.pack(pady=10)

# Initial Load
load_options()

# Run app
root.mainloop()
