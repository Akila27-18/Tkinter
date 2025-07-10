import tkinter as tk
import threading
import time
import random
from datetime import datetime

class RealTimeLoggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Logger")
        self.root.geometry("500x400")

        self.text_widget = tk.Text(root, wrap=tk.WORD, state='disabled')
        self.text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.start_btn = tk.Button(root, text="Start Logging", command=self.start_logging)
        self.start_btn.pack(side=tk.LEFT, padx=20, pady=10)

        self.stop_btn = tk.Button(root, text="Stop Logging", command=self.stop_logging, state='disabled')
        self.stop_btn.pack(side=tk.RIGHT, padx=20, pady=10)

        self.logging = False
        self.log_thread = None

    def start_logging(self):
        if not self.logging:
            self.logging = True
            self.start_btn.config(state='disabled')
            self.stop_btn.config(state='normal')
            self.log_thread = threading.Thread(target=self.generate_logs, daemon=True)
            self.log_thread.start()

    def stop_logging(self):
        self.logging = False
        self.start_btn.config(state='normal')
        self.stop_btn.config(state='disabled')

    def generate_logs(self):
        while self.logging:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = random.choice([
                "INFO: Task completed successfully.",
                "WARNING: Low memory warning.",
                "ERROR: Failed to connect to server.",
                "DEBUG: Variable x = 42.",
                "INFO: Scheduled job started."
            ])
            log_line = f"[{timestamp}] {message}\n"
            self.root.after(0, self.append_log, log_line)
            time.sleep(1)

    def append_log(self, log_line):
        self.text_widget.config(state='normal')
        self.text_widget.insert(tk.END, log_line)
        self.text_widget.see(tk.END)
        self.text_widget.config(state='disabled')

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = RealTimeLoggerApp(root)
    root.mainloop()
