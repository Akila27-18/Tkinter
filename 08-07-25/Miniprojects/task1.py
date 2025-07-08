import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os

def populate_tree(path, parent=""):
    tree.delete(*tree.get_children(parent))
    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                node = tree.insert(parent, "end", text=item, open=False, values=[full_path])
                tree.insert(node, "end")  # Dummy child to show expand arrow
    except PermissionError:
        pass

def on_tree_expand(event):
    node = tree.focus()
    path = tree.item(node, "values")[0]
    populate_tree(path, node)

def on_tree_select(event):
    node = tree.focus()
    if node:
        path = tree.item(node, "values")[0]
        show_files(path)

def show_files(path):
    file_list.delete(0, tk.END)
    if os.path.isdir(path):
        try:
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                if os.path.isfile(full_path):
                    file_list.insert(tk.END, item)
        except PermissionError:
            messagebox.showinfo("Access Denied", "You do not have permission to access this folder.")

def open_folder():
    path = filedialog.askdirectory()
    if path:
        populate_tree(path)
        show_files(path)

def confirm_exit():
    if messagebox.askquestion("Exit", "Are you sure you want to exit?") == "yes":
        root.quit()

# Main window
root = tk.Tk()
root.title("File Manager")
root.geometry("800x500")

# Menu bar
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open", command=open_folder)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=confirm_exit)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

# Toolbar
toolbar = tk.Frame(root, bg="lightgray")
toolbar.pack(side="top", fill="x")

tk.Button(toolbar, text="Refresh", command=lambda: populate_tree(os.getcwd())).pack(side="left", padx=2, pady=2)
tk.Button(toolbar, text="Open Folder", command=open_folder).pack(side="left", padx=2, pady=2)

# PanedWindow
paned = tk.PanedWindow(root, orient=tk.HORIZONTAL, sashrelief=tk.RAISED)
paned.pack(fill=tk.BOTH, expand=True)

# Left pane: directory tree
tree_frame = tk.Frame(paned)
tree = ttk.Treeview(tree_frame)
tree.heading("#0", text="Directory Tree", anchor="w")
tree.pack(fill=tk.BOTH, expand=True)
tree.bind("<<TreeviewOpen>>", on_tree_expand)
tree.bind("<<TreeviewSelect>>", on_tree_select)
paned.add(tree_frame, minsize=200)

# Right pane: file list
file_frame = tk.Frame(paned)
file_list = tk.Listbox(file_frame)
file_list.pack(fill=tk.BOTH, expand=True)
paned.add(file_frame, minsize=300)

# Populate initial tree with current directory
start_dir = os.getcwd()
root_node = tree.insert("", "end", text=start_dir, open=True, values=[start_dir])
populate_tree(start_dir, root_node)
show_files(start_dir)

root.mainloop()
