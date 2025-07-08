import tkinter as tk

root = tk.Tk()
pw = tk.PanedWindow(root, orient=tk.HORIZONTAL)
pw.pack(fill=tk.BOTH, expand=True)

file_explorer = tk.Listbox(pw)
file_explorer.insert(1, "file1.txt")
file_explorer.insert(2, "file2.txt")
file_explorer.insert(3, "folder/")

main_view = tk.Text(pw)

pw.add(file_explorer, minsize=100)
pw.add(main_view)

root.mainloop()
