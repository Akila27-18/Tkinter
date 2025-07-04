import tkinter as tk
from tkinter import ttk

class LiveScoreboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Scoreboard")

        self.team_a_name = tk.StringVar(value="Team A")
        self.team_b_name = tk.StringVar(value="Team B")
        self.score_a = tk.IntVar(value=0)
        self.score_b = tk.IntVar(value=0)

        # Team Names Comboboxes
        name_frame = tk.Frame(root)
        name_frame.pack(pady=5)

        tk.Label(name_frame, text="Team A:").grid(row=0, column=0)
        self.combo_a = ttk.Combobox(name_frame, textvariable=self.team_a_name, values=["Team A", "Lions", "Tigers", "Sharks"], state="readonly")
        self.combo_a.grid(row=0, column=1, padx=5)
        self.combo_a.bind("<<ComboboxSelected>>", self.update_canvas)

        tk.Label(name_frame, text="Team B:").grid(row=0, column=2)
        self.combo_b = ttk.Combobox(name_frame, textvariable=self.team_b_name, values=["Team B", "Eagles", "Wolves", "Dragons"], state="readonly")
        self.combo_b.grid(row=0, column=3, padx=5)
        self.combo_b.bind("<<ComboboxSelected>>", self.update_canvas)

        # Score Spinboxes
        score_frame = tk.Frame(root)
        score_frame.pack()

        tk.Label(score_frame, text="Score A:").grid(row=0, column=0)
        self.spin_a = tk.Spinbox(score_frame, from_=0, to=999, width=5, textvariable=self.score_a, command=self.update_canvas)
        self.spin_a.grid(row=0, column=1, padx=10)

        tk.Label(score_frame, text="Score B:").grid(row=0, column=2)
        self.spin_b = tk.Spinbox(score_frame, from_=0, to=999, width=5, textvariable=self.score_b, command=self.update_canvas)
        self.spin_b.grid(row=0, column=3, padx=10)

        # Canvas for scoreboard
        self.canvas = tk.Canvas(root, width=400, height=200, bg="black")
        self.canvas.pack(pady=10)

        # Reset button
        self.reset_btn = tk.Button(root, text="Reset Scores", command=self.reset_scores)
        self.reset_btn.pack()

        # Draw initial scoreboard
        self.update_canvas()

    def update_canvas(self, event=None):
        self.canvas.delete("all")

        # Background
        self.canvas.create_rectangle(0, 0, 400, 200, fill="black")

        # Team A name & score
        self.canvas.create_text(100, 60, text=self.team_a_name.get(), font=("Arial", 20, "bold"), fill="white")
        self.canvas.create_text(100, 120, text=str(self.score_a.get()), font=("Arial", 36, "bold"), fill="red")

        # Team B name & score
        self.canvas.create_text(300, 60, text=self.team_b_name.get(), font=("Arial", 20, "bold"), fill="white")
        self.canvas.create_text(300, 120, text=str(self.score_b.get()), font=("Arial", 36, "bold"), fill="blue")

        # Divider
        self.canvas.create_line(200, 20, 200, 180, fill="white", width=2)

    def reset_scores(self):
        self.team_a_name.set("Team A")
        self.team_b_name.set("Team B")
        self.score_a.set(0)
        self.score_b.set(0)
        self.update_canvas()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = LiveScoreboard(root)
    root.mainloop()
