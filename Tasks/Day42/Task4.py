import tkinter as tk

def main():
    # Create main window
    root = tk.Tk()
    root.title("Canvas Drawing Tasks")
    root.geometry("500x500")

    # Create Canvas
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack(pady=20)

   

    # 4. Draw a polygon (triangle)
    canvas.create_polygon(100, 250, 150, 200, 200, 250,
                          outline="purple", fill="lavender", width=2)

   
    root.mainloop()

if __name__ == "__main__":
    main()
