import tkinter as tk

def main():
    # Create main window
    root = tk.Tk()
    root.title("Canvas Drawing Tasks")
    root.geometry("500x500")

    # Create Canvas
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack(pady=20)

   
    # 5. Fill shapes with different colors
    canvas.create_rectangle(250, 250, 350, 320, outline="brown", fill="orange", width=2)
    canvas.create_oval(60, 300, 140, 380, outline="blue", fill="yellow", width=2)

    root.mainloop()

if __name__ == "__main__":
    main()
