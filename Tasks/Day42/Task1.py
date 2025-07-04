import tkinter as tk

def main():
    # Create main window
    root = tk.Tk()
    root.title("Canvas Drawing Tasks")
    root.geometry("500x500")

    # Create Canvas
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack(pady=20)

    # 1. Draw a rectangle
    canvas.create_rectangle(50, 50, 150, 120, outline="black", fill="skyblue", width=2)

    
    root.mainloop()

if __name__ == "__main__":
    main()
