import tkinter as tk
from tkinter import ttk

def submit_feedback():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    comment = text_comment.get("1.0", tk.END).strip()
    rating = spin_rating.get()

    if not name or not email or not comment:
        thank_you_label.config(text="Please fill in all fields.", foreground="red")
        return

    feedback = f"{name} ({email}) | Rating: {rating} | Comment: {comment}"
    listbox_feedback.insert(tk.END, feedback)

    # Clear inputs
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    text_comment.delete("1.0", tk.END)
    spin_rating.delete(0, tk.END)
    spin_rating.insert(0, "5")

    thank_you_label.config(text="Thank you for your feedback!", foreground="green")

# Main window
root = tk.Tk()
root.title("Feedback Form")
root.geometry("600x400")

# Name and Email
ttk.Label(root, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_name = ttk.Entry(root, width=30)
entry_name.grid(row=0, column=1, pady=5)

ttk.Label(root, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_email = ttk.Entry(root, width=30)
entry_email.grid(row=1, column=1, pady=5)

# Comments
ttk.Label(root, text="Comments:").grid(row=2, column=0, sticky="ne", padx=5, pady=5)
text_comment = tk.Text(root, width=30, height=5)
text_comment.grid(row=2, column=1, pady=5)

# Rating
ttk.Label(root, text="Rating (1-10):").grid(row=3, column=0, sticky="e", padx=5, pady=5)
spin_rating = tk.Spinbox(root, from_=1, to=10, width=5)
spin_rating.grid(row=3, column=1, sticky="w")
spin_rating.delete(0, tk.END)
spin_rating.insert(0, "5")

# Submit Button
submit_btn = ttk.Button(root, text="Submit Feedback", command=submit_feedback)
submit_btn.grid(row=4, column=1, pady=10, sticky="w")

# Thank you label
thank_you_label = ttk.Label(root, text="")
thank_you_label.grid(row=5, column=1, sticky="w", pady=5)

# Feedback Listbox + Scrollbar
ttk.Label(root, text="All Feedback:").grid(row=0, column=2, padx=10, pady=5)
frame_listbox = ttk.Frame(root)
frame_listbox.grid(row=1, column=2, rowspan=5, padx=10, pady=5)

scrollbar = ttk.Scrollbar(frame_listbox)
listbox_feedback = tk.Listbox(frame_listbox, width=40, height=15, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_feedback.yview)

listbox_feedback.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()
