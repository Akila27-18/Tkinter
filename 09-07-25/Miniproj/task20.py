import tkinter as tk

class EmojiBar(tk.Frame):
    def __init__(self, parent, target_label, emojis=["😀", "😢", "😠", "❤️"], *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.target_label = target_label
        self.emojis = emojis
        self.create_widgets()

    def create_widgets(self):
        for emoji in self.emojis:
            btn = tk.Button(self, text=emoji, font=("Arial", 14), width=3, command=lambda e=emoji: self.react(e))
            btn.pack(side="left", padx=2)

    def react(self, emoji):
        self.target_label.config(text=f"Reaction: {emoji}")
        print(f"Reacted with: {emoji}")

# App setup
root = tk.Tk()
root.title("Emoji Reaction Panel")
root.geometry("350x300")

# Sample message 1
msg1 = tk.Label(root, text="Message 1: Hello there!", font=("Arial", 12))
msg1.pack(pady=5)

reaction1 = tk.Label(root, text="Reaction: None", font=("Arial", 10), fg="gray")
reaction1.pack()

bar1 = EmojiBar(root, reaction1)
bar1.pack(pady=5)

# Sample message 2
msg2 = tk.Label(root, text="Message 2: How are you?", font=("Arial", 12))
msg2.pack(pady=5)

reaction2 = tk.Label(root, text="Reaction: None", font=("Arial", 10), fg="gray")
reaction2.pack()

bar2 = EmojiBar(root, reaction2)
bar2.pack(pady=5)

root.mainloop()
