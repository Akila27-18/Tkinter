import tkinter as tk

def main():
    # Create main window
    root = tk.Tk()
    root.title("Canvas Drawing Tasks")
    root.geometry("500x500")

    # Create Canvas
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack(pady=20)

    

    # 3. Draw a line between two points
    canvas.create_line(50, 200, 300, 200, fill="red", width=3)

   
    root.mainloop()

if __name__ == "__main__":
    main()
