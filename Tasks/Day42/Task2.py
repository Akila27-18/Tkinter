import tkinter as tk

def main():
    # Create main window
    root = tk.Tk()
    root.title("Canvas Drawing Tasks")
    root.geometry("500x500")

    # Create Canvas
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack(pady=20)

   
    # 2. Draw a circle (oval)
    canvas.create_oval(200, 50, 280, 130, outline="green", fill="lightgreen", width=2)

    
    root.mainloop()

if __name__ == "__main__":
    main()
