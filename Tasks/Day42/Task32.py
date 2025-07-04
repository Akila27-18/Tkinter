import tkinter as tk

def show_selected():
    selected = listbox.curselection()
    if selected:
        value = listbox.get(selected[0])
        print("Selected (via button):", value)

def on_select(event):
    selected = listbox.curselection()
    if selected:
        value = listbox.get(selected[0])
        print("Selected (via callback):", value)

root = tk.Tk()
root.title("Listbox Selection Example")

listbox = tk.Listbox(root)
for item in ["Red", "Green", "Blue", "Yellow"]:
    listbox.insert(tk.END, item)
listbox.pack()

# Bind selection change callback
listbox.bind("<<ListboxSelect>>", on_select)

# Button to print selected item
btn = tk.Button(root, text="Show Selected", command=show_selected)
btn.pack(pady=5)

root.mainloop()
