import tkinter as tk
from tkinter import messagebox
import random

class ScrollingNewsReader:
    def __init__(self, root):
        self.root = root
        self.root.title("Scrolling News Reader")

        # Sample headlines
        self.all_news = [f"Breaking News Headline #{i+1}" for i in range(30)]

        # Listbox + Scrollbar
        frame = tk.Frame(root)
        frame.pack(pady=10)

        self.news_listbox = tk.Listbox(frame, width=60, height=10)
        self.news_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        scroll = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.news_listbox.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.news_listbox.config(yscrollcommand=scroll.set)

        # Populate listbox
        self.populate_news()

        # Bind item click
        self.news_listbox.bind("<<ListboxSelect>>", self.show_details)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Refresh News", command=self.refresh_news).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Start Ticker", command=self.start_autoscroll).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Stop Ticker", command=self.stop_autoscroll).pack(side=tk.LEFT, padx=10)

        # Ticker control
        self.ticker_running = False

    def populate_news(self):
        self.news_listbox.delete(0, tk.END)
        for headline in self.all_news:
            self.news_listbox.insert(tk.END, headline)

    def show_details(self, event):
        selection = self.news_listbox.curselection()
        if not selection:
            return
        index = selection[0]
        headline = self.news_listbox.get(index)
        messagebox.showinfo("News Details", f"Details for:\n\n{headline}")

    def refresh_news(self):
        random.shuffle(self.all_news)
        self.populate_news()

    def start_autoscroll(self):
        self.ticker_running = True
        self.auto_scroll()

    def stop_autoscroll(self):
        self.ticker_running = False

    def auto_scroll(self):
        if not self.ticker_running:
            return
        current = self.news_listbox.yview()
        # If at bottom, scroll to top
        if current[1] >= 1.0:
            self.news_listbox.yview_moveto(0)
        else:
            self.news_listbox.yview_scroll(1, "units")
        self.root.after(1000, self.auto_scroll)  # Adjust delay as needed

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ScrollingNewsReader(root)
    root.mainloop()
