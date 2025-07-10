import tkinter as tk
from tkinter import messagebox
import sqlite3
import threading
import time

# Database setup
def init_db():
    conn = sqlite3.connect("feedback.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            rating INTEGER,
            comments TEXT
        )
    """)
    conn.commit()
    conn.close()

# Function to insert feedback (runs in thread)
def insert_feedback(name, rating, comments):
    time.sleep(2)  # Simulated delay
    conn = sqlite3.connect("feedback.db")
    c = conn.cursor()
    c.execute("INSERT INTO feedback (name, rating, comments) VALUES (?, ?, ?)", (name, rating, comments))
    conn.commit()
    conn.close()
    # Refresh listbox in main thread
    root.after(0, load_feedback)

# Threaded submission
def submit_feedback():
    name = entry_name.get()
    rating = entry_rating.get()
    comments = entry_comments.get("1.0", tk.END).strip()

    if not name or not rating or not comments:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    try:
        rating_val = int(rating)
        if rating_val < 1 or rating_val > 5:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Input Error", "Rating must be a number between 1 and 5.")
        return

    threading.Thread(target=insert_feedback, args=(name, rating_val, comments), daemon=True).start()
    messagebox.showinfo("Submitted", "Feedback is being submitted...")
    entry_name.delete(0, tk.END)
    entry_rating.delete(0, tk.END)
    entry_comments.delete("1.0", tk.END)

# Load feedback into Listbox
def load_feedback():
    listbox_feedback.delete(0, tk.END)
    conn = sqlite3.connect("feedback.db")
    c = conn.cursor()
    c.execute("SELECT name, rating, comments FROM feedback ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    for row in rows:
        listbox_feedback.insert(tk.END, f"{row[0]} | Rating: {row[1]} | {row[2]}")

# GUI setup
root = tk.Tk()
root.title("Customer Feedback Collector")
root.geometry("500x550")
root.resizable(False, False)

tk.Label(root, text="Customer Feedback Form", font=("Arial", 16, "bold")).pack(pady=10)

frame_form = tk.Frame(root)
frame_form.pack(pady=5)

tk.Label(frame_form, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_name = tk.Entry(frame_form, width=40)
entry_name.grid(row=0, column=1, padx=5)

tk.Label(frame_form, text="Rating (1-5):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_rating = tk.Entry(frame_form, width=40)
entry_rating.grid(row=1, column=1, padx=5)

tk.Label(frame_form, text="Comments:").grid(row=2, column=0, sticky="ne", padx=5, pady=5)
entry_comments = tk.Text(frame_form, width=30, height=5)
entry_comments.grid(row=2, column=1, padx=5, pady=5)

tk.Button(root, text="Submit Feedback", command=submit_feedback, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)

tk.Label(root, text="All Feedbacks:", font=("Arial", 14, "bold")).pack(pady=5)
listbox_feedback = tk.Listbox(root, width=70, height=10)
listbox_feedback.pack(pady=5)

tk.Button(root, text="Refresh Feedback", command=load_feedback, bg="#2196F3", fg="white").pack(pady=10)

# Run
init_db()
load_feedback()
root.mainloop()
