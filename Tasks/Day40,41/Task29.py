import tkinter as tk

# Function to show main window after splash screen
def show_main_window():
    splash.destroy()  # Close splash screen

    # Create main application window
    main = tk.Tk()
    main.title("Main App")
    main.geometry("400x300")
    
    tk.Label(main, text="Welcome to the Main App", font=("Arial", 16)).pack(expand=True)
    
    main.mainloop()

# Create splash screen window
splash = tk.Tk()
splash.title("Splash Screen")
splash.geometry("300x150")
splash.overrideredirect(True)  # Hide window borders/title bar

# Center splash screen
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()
x = (screen_width // 2) - 150
y = (screen_height // 2) - 75
splash.geometry(f"300x150+{x}+{y}")

# Splash content
tk.Label(splash, text="Loading...", font=("Arial", 14)).pack(expand=True)

# Schedule splash to close after 3 seconds (3000 ms)
splash.after(3000, show_main_window)

# Start splash screen event loop
splash.mainloop()
