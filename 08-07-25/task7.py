import tkinter as tk

root = tk.Tk()

header = tk.Frame(root, bg="lightblue", height=50)
content = tk.Frame(root, bg="white", height=150)
footer = tk.Frame(root, bg="lightgray", height=30)

header.pack(fill="x")
content.pack(fill="both", expand=True)
footer.pack(fill="x")

tk.Label(header, text="Header").pack()
tk.Label(content, text="Main Content").pack()
tk.Label(footer, text="Footer").pack()

root.mainloop()
