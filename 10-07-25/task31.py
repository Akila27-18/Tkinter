import tkinter as tk

root = tk.Tk()
root.title("Feedback Form")

tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Rating (1–5):").grid(row=1, column=0)
entry_rating = tk.Entry(root)
entry_rating.grid(row=1, column=1)

tk.Label(root, text="Comment:").grid(row=2, column=0)
entry_comment = tk.Text(root, height=4, width=30)
entry_comment.grid(row=2, column=1)

tk.Button(root, text="Submit Feedback").grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
