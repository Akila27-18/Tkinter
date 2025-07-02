import tkinter as tk

command_count = 0

def log_command():
    global command_count
    command = entry_command.get().strip()
    if command:
        command_count += 1
        text_log.insert(tk.END, f"{command_count}. {command}\n")
        label_count.config(text=f"Commands Logged: {command_count}")
        entry_command.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("Voice Command Logger")
root.geometry("400x300")

# Command Entry
tk.Label(root, text="Simulated Command:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_command = tk.Entry(root, width=30)
entry_command.grid(row=0, column=1, padx=5, pady=10)

# Log Button
tk.Button(root, text="Log Command", command=log_command).grid(row=1, columnspan=2, pady=5)

# Log Output
text_log = tk.Text(root, width=45, height=10)
text_log.grid(row=2, columnspan=2, padx=10, pady=10)

# Command Count Label
label_count = tk.Label(root, text="Commands Logged: 0", font=("Arial", 10))
label_count.grid(row=3, columnspan=2, pady=5)

root.mainloop()
