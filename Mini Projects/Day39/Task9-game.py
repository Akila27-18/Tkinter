import tkinter as tk
import random

def check_guess():
    try:
        guess = int(guess_entry.get())
        if guess < number_to_guess:
            hint_label.config(text="Too low! Try again.", fg="blue")
        elif guess > number_to_guess:
            hint_label.config(text="Too high! Try again.", fg="blue")
        else:
            hint_label.config(text=f"🎉 Correct! The number was {number_to_guess}", fg="green")
    except ValueError:
        hint_label.config(text="Please enter a valid number.", fg="red")

def reset_game():
    global number_to_guess
    number_to_guess = random.randint(1, 100)
    hint_label.config(text="Guess a number between 1 and 100", fg="black")
    guess_entry.delete(0, tk.END)

# Initial number
number_to_guess = random.randint(1, 100)

# GUI setup
root = tk.Tk()
root.title("Guess the Number")
root.geometry("350x250")

tk.Label(root, text="Enter your guess (1–100):").pack(pady=10)
guess_entry = tk.Entry(root, width=25)
guess_entry.pack(pady=5)

submit_btn = tk.Button(root, text="Submit Guess", command=check_guess)
submit_btn.pack(pady=5)

hint_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 12))
hint_label.pack(pady=10)

reset_btn = tk.Button(root, text="Reset Game", command=reset_game)
reset_btn.pack(pady=5)

root.mainloop()
