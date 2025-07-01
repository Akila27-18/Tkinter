import tkinter as tk

def submit_feedback():
    name = name_entry.get().strip()
    comments = comments_box.get("1.0", tk.END).strip()

    if name and comments:
        result_label.config(text=f"Thank you, {name}, for your feedback!", fg="green")
        name_entry.delete(0, tk.END)
        comments_box.delete("1.0", tk.END)
    else:
        result_label.config(text="Please enter both name and comments.", fg="red")

# GUI setup
root = tk.Tk()
root.title("Feedback Collector")
root.geometry("400x350")

# Name Entry
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

# Comments Text Box
tk.Label(root, text="Comments:").pack(pady=5)
comments_box = tk.Text(root, width=40, height=6)
comments_box.pack(pady=5)

# Submit Button
tk.Button(root, text="Submit Feedback", command=submit_feedback).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
