import tkinter as tk
from tkinter import messagebox

def send_message():
    msg = message_entry.get()
    if msg:
        chat_display.config(state='normal')
        chat_display.insert(tk.END, f"You: {msg}\n")
        chat_display.config(state='disabled')
        chat_display.see(tk.END)
        message_entry.delete(0, tk.END)

def clear_chat():
    if messagebox.askokcancel("Confirm", "Clear chat history?"):
        chat_display.config(state='normal')
        chat_display.delete(1.0, tk.END)
        chat_display.config(state='disabled')

def connect():
    messagebox.showinfo("Connect", "Connected to server!")

def disconnect():
    messagebox.showinfo("Disconnect", "Disconnected from server.")

def exit_app():
    root.quit()

# Main window
root = tk.Tk()
root.title("Chat UI")
root.geometry("500x400")

# Menu
menu_bar = tk.Menu(root)
chat_menu = tk.Menu(menu_bar, tearoff=0)
chat_menu.add_command(label="Clear", command=clear_chat)
chat_menu.add_separator()
chat_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="Chat", menu=chat_menu)
root.config(menu=menu_bar)

# Toolbar frame
toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
toolbar.pack(side=tk.TOP, fill=tk.X)

btn_connect = tk.Button(toolbar, text="Connect", command=connect)
btn_connect.pack(side=tk.LEFT, padx=2, pady=2)

btn_disconnect = tk.Button(toolbar, text="Disconnect", command=disconnect)
btn_disconnect.pack(side=tk.LEFT, padx=2, pady=2)

# Chat display (top frame)
chat_frame = tk.Frame(root)
chat_frame.pack(fill=tk.BOTH, expand=True)

chat_display = tk.Text(chat_frame, state='disabled', wrap='word')
chat_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Bottom input area
input_frame = tk.Frame(root)
input_frame.pack(fill=tk.X, padx=5, pady=5)

message_entry = tk.Entry(input_frame)
message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
message_entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(input_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)

root.mainloop()
