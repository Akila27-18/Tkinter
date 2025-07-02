import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Horizontal Button Layout")
root.geometry("300x100")  # Optional size

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)  # Center vertically with padding

# Create and pack buttons horizontally
btn1 = tk.Button(button_frame, text="Button 1")
btn2 = tk.Button(button_frame, text="Button 2")
btn3 = tk.Button(button_frame, text="Button 3")

btn1.pack(side="left", padx=10)
btn2.pack(side="left", padx=10)
btn3.pack(side="left", padx=10)

# Start the Tkinter event loop
root.mainloop()
