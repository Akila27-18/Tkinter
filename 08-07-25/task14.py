import tkinter as tk

root = tk.Tk()
styled_frame = tk.Frame(root, bg="lightyellow", borderwidth=4, relief="groove", padx=20, pady=20)
styled_frame.pack(padx=30, pady=30)

tk.Label(styled_frame, text="Styled Frame Content").pack()

root.mainloop()
