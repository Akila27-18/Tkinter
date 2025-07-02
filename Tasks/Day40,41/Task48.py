import tkinter as tk

# List of keywords to highlight
KEYWORDS = ["def", "import", "return", "class", "from"]

# Function to highlight keywords
def highlight_keywords():
    # Remove previous highlights
    for tag in KEYWORDS:
        text_area.tag_remove(tag, "1.0", tk.END)

    content = text_area.get("1.0", tk.END)

    for keyword in KEYWORDS:
        start = "1.0"
        while True:
            pos = text_area.search(rf"\m{keyword}\M", start, tk.END, regexp=True)
            if not pos:
                break
            end = f"{pos}+{len(keyword)}c"
            text_area.tag_add(keyword, pos, end)
            start = end

# Create main window
root = tk.Tk()
root.title("Keyword Highlighter")
root.geometry("500x300")

# Text widget
text_area = tk.Text(root, wrap="word", font=("Consolas", 12))
text_area.pack(expand=True, fill="both", padx=10, pady=10)

# Tag configurations (colors for keywords)
text_area.tag_config("def", foreground="blue")
text_area.tag_config("import", foreground="purple")
text_area.tag_config("return", foreground="green")
text_area.tag_config("class", foreground="darkorange")
text_area.tag_config("from", foreground="red")

# Highlight when text is changed (key release)
text_area.bind("<KeyRelease>", lambda e: highlight_keywords())

# Insert sample text
text_area.insert("1.0", "def my_function():\n    import os\n    return 'Done'\n")

# Start the event loop
root.mainloop()
