import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Custom Icon Example")
root.geometry("300x150")

# Set custom icon (must be .ico format)
root.iconbitmap("C:/Users/sharm/Desktop/Tkinter/favicon.ico")  # Replace with your actual .ico file path

# Label (optional)
label = tk.Label(root, text="Window with custom icon", font=("Arial", 12))
label.pack(pady=40)

# Start the event loop
root.mainloop()
