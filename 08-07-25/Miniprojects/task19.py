import tkinter as tk

class LayoutDemo:
    def __init__(self, root):
        self.root = root
        self.root.title("Responsive Layout Demo")
        self.root.geometry("900x300")

        self.setup_layout()

    def setup_layout(self):
        # Main container frame
        container = tk.Frame(self.root)
        container.pack(fill=tk.BOTH, expand=True)

        # --- Section 1: pack() layout ---
        frame1 = tk.Frame(container, bd=2, relief="groove", padx=10, pady=10)
        frame1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Label(frame1, text="pack() Layout", font=("Arial", 12, "bold")).pack(pady=5)
        tk.Button(frame1, text="Button 1").pack(fill=tk.X, pady=5)
        tk.Button(frame1, text="Button 2").pack(fill=tk.X, pady=5)
        tk.Button(frame1, text="Button 3").pack(fill=tk.X, pady=5)

        # --- Section 2: grid() layout ---
        frame2 = tk.Frame(container, bd=2, relief="groove", padx=10, pady=10)
        frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Label(frame2, text="grid() Layout", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

        tk.Label(frame2, text="Name:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(frame2).grid(row=1, column=1, pady=5)

        tk.Label(frame2, text="Email:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(frame2).grid(row=2, column=1, pady=5)

        tk.Label(frame2, text="Phone:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(frame2).grid(row=3, column=1, pady=5)

        # --- Section 3: place() layout ---
        frame3 = tk.Frame(container, bd=2, relief="groove", width=300, height=250, bg="#f1f2f6")
        frame3.pack_propagate(False)
        frame3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Label(frame3, text="place() Layout", font=("Arial", 12, "bold"), bg="#f1f2f6").place(x=80, y=10)
        tk.Button(frame3, text="Top Left").place(x=10, y=50)
        tk.Button(frame3, text="Center").place(x=100, y=100)
        tk.Button(frame3, text="Bottom Right").place(x=180, y=180)

if __name__ == "__main__":
    root = tk.Tk()
    app = LayoutDemo(root)
    root.mainloop()
