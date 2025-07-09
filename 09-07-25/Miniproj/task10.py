import tkinter as tk

def on_key_press(event):
    current = listbox.curselection()
    if not current:
        index = 0
    else:
        index = current[0]

    if event.keysym == 'Up':
        new_index = max(0, index - 1)
        listbox.select_clear(0, tk.END)
        listbox.select_set(new_index)
        listbox.activate(new_index)

    elif event.keysym == 'Down':
        new_index = min(len(items) - 1, index + 1)
        listbox.select_clear(0, tk.END)
        listbox.select_set(new_index)
        listbox.activate(new_index)

    elif event.keysym == 'Return':
        selected = listbox.get(index)
        selected_label.config(text=f"Selected: {selected}")

# GUI Setup
root = tk.Tk()
root.title("Listbox Navigator")
root.geometry("300x300")

items = ['Apple', 'Banana', 'Cherry', 'Date', 'Fig', 'Grapes']

listbox = tk.Listbox(root, font=("Arial", 12), activestyle='dotbox')
for item in items:
    listbox.insert(tk.END, item)
listbox.pack(pady=20)
listbox.select_set(0)  # Initial selection

selected_label = tk.Label(root, text="Selected: None", font=("Arial", 12))
selected_label.pack()

# Bind key events to the listbox
listbox.bind("<Up>", on_key_press)
listbox.bind("<Down>", on_key_press)
listbox.bind("<Return>", on_key_press)

listbox.focus_set()  # Make sure it captures keyboard input

root.mainloop()
