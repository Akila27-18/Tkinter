import tkinter as tk
from tkinter import ttk
import threading
import time

class DownloadSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Download Simulation Tool")
        self.root.geometry("400x200")

        self.progress = 0
        self.downloading = False
        self.thread = None

        self.label = tk.Label(root, text="Progress: 0%", font=('Arial', 12))
        self.label.pack(pady=10)

        self.progressbar = ttk.Progressbar(root, length=300, mode='determinate', maximum=100)
        self.progressbar.pack(pady=10)

        self.start_btn = tk.Button(root, text="Start Download", command=self.start_download)
        self.start_btn.pack(pady=5)

        self.cancel_btn = tk.Button(root, text="Cancel", state='disabled', command=self.cancel_download)
        self.cancel_btn.pack(pady=5)

    def start_download(self):
        if not self.downloading:
            self.downloading = True
            self.progress = 0
            self.progressbar['value'] = 0
            self.label.config(text="Progress: 0%")
            self.start_btn.config(state='disabled')
            self.cancel_btn.config(state='normal')
            self.thread = threading.Thread(target=self.simulate_download)
            self.thread.start()

    def simulate_download(self):
        while self.progress < 100 and self.downloading:
            time.sleep(0.1)  # Simulate work
            self.progress += 1
            self.root.after(0, self.update_ui)
        if self.progress >= 100:
            self.root.after(0, self.download_complete)

    def update_ui(self):
        self.progressbar['value'] = self.progress
        self.label.config(text=f"Progress: {self.progress}%")

    def cancel_download(self):
        self.downloading = False
        self.progress = 0
        self.progressbar['value'] = 0
        self.label.config(text="Download Cancelled")
        self.start_btn.config(state='normal')
        self.cancel_btn.config(state='disabled')

    def download_complete(self):
        self.label.config(text="Download Complete!")
        self.start_btn.config(state='normal')
        self.cancel_btn.config(state='disabled')
        self.downloading = False

if __name__ == "__main__":
    root = tk.Tk()
    app = DownloadSimulator(root)
    root.mainloop()
