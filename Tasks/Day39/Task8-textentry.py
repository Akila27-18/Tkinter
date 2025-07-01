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

# Create an Entry widget (text input) 
entry = tk.Entry(root) 
entry.pack()

def show_input(): 
    user_input = entry.get() 
    # Get text from Entry widget 
    label.config(text=f"Hello, {user_input}!") 

# Create a Button widget 
button = tk.Button(root, text="Submit", command=show_input)
button.pack()

# Start the Tkinter event loop 
root.mainloop()