import tkinter as tk
import random

def roll_dice():
    result = random.randint(1, 6)
    result_label.config(text=f"🎲 You rolled: {result}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Dice Roller Simulator")
root.geometry("300x200")

# Result Label
result_label = tk.Label(root, text="Click to roll the dice", font=("Arial", 14))
result_label.place(relx=0.5, rely=0.4, anchor="center")

# Roll Button
roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 12), command=roll_dice)
roll_button.place(relx=0.5, rely=0.6, anchor="center")

root.mainloop()
