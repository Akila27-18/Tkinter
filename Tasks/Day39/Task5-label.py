import tkinter as tk 
# Create the main window 
root = tk.Tk()
# Set the title of the window 
root.title("Akila") 
# Set the window size 
root.geometry("800x500") 

# Create a Label widget 
label = tk.Label(root, text="Welcome to Tkinter!") 
label.pack()
# Start the Tkinter event loop 
root.mainloop()