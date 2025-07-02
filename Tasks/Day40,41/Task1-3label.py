import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Three Vertical Labels")
root.geometry("300x200")  # Set window size (optional)

# Create three labels
label1 = tk.Label(root, text="Label 1", bg="lightblue", font=("Arial", 14))
label2 = tk.Label(root, text="Label 2", bg="lightgreen", font=("Arial", 14))
label3 = tk.Label(root, text="Label 3", bg="lightcoral", font=("Arial", 14))

# Stack labels vertically using pack()
label1.pack(fill='x', pady=5)
label2.pack(fill='x', pady=5)
label3.pack(fill='x', pady=5)

# Start the Tkinter event loop
root.mainloop()
