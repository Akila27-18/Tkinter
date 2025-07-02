import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")  # Set fixed window size

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.place(x=30, y=40)

username_entry = tk.Entry(root)
username_entry.place(x=110, y=40)

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.place(x=30, y=80)

password_entry = tk.Entry(root, show="*")
password_entry.place(x=110, y=80)

# Login button
login_button = tk.Button(root, text="Login")
login_button.place(x=120, y=130)

# Start the event loop
root.mainloop()
