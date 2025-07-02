import tkinter as tk

# Function to change the window background color
def change_bg():
    root.configure(bg="lightblue")

# Create the main window
root = tk.Tk()
root.title("Change Background Color")
root.geometry("300x150")

# Create button
btn = tk.Button(root, text="Change Background", command=change_bg)
btn.pack(pady=40)

# Start the event loop
root.mainloop()
