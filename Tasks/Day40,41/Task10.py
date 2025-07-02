import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Sidebar Layout")
root.geometry("600x400")  # Width x Height

# Sidebar Frame (left side)
sidebar = tk.Frame(root, width=150, bg="#4B69A9")
sidebar.pack(side="left", fill="y")

# Add some buttons to sidebar
tk.Button(sidebar, text="Home", fg="white", bg="#4B69A9", relief="flat").pack(pady=10, padx=10, anchor="w")
tk.Button(sidebar, text="Settings", fg="white", bg="#4B69A9", relief="flat").pack(pady=10, padx=10, anchor="w")
tk.Button(sidebar, text="Logout", fg="white", bg="#4B69A9", relief="flat").pack(pady=10, padx=10, anchor="w")

# Main Content Frame (rest of the space)
main_content = tk.Frame(root, bg="#F5F5F5")
main_content.pack(fill="both", expand=True)

# Add content to main area
tk.Label(main_content, text="Welcome to the Dashboard", font=("Arial", 16), bg="#F5F5F5").pack(pady=20)

# Start the event loop
root.mainloop()
