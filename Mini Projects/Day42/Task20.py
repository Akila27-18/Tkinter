import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime

# ---- Setup root window ----
root = tk.Tk()
root.title("Interactive Calendar Picker")
root.geometry("600x500")

# ---- Variables ----
month_var = tk.StringVar()
year_var = tk.IntVar(value=datetime.now().year)
selected_info = tk.StringVar(value="Select a date")

# ---- Dummy Notes (can be extended to file/db) ----
event_notes = {
    "2025-07-04": "Independence Day (USA)",
    "2025-07-10": "Team Meeting",
    "2025-07-21": "Project Deadline"
}

# ---- Month Selector ----
months = list(calendar.month_name)[1:]  # Exclude empty first item
month_var.set(months[datetime.now().month - 1])
tk.Label(root, text="Month:").pack(pady=2)
month_combo = ttk.Combobox(root, textvariable=month_var, values=months, state="readonly", width=15)
month_combo.pack()

# ---- Year Spinbox ----
tk.Label(root, text="Year:").pack(pady=2)
year_spin = tk.Spinbox(root, from_=1900, to=2100, textvariable=year_var, width=10)
year_spin.pack()

# ---- Calendar Canvas ----
canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack(pady=10)

# ---- Label for clicked day info ----
info_label = tk.Label(root, textvariable=selected_info, font=("Arial", 12), fg="blue")
info_label.pack(pady=5)

# ---- Draw Calendar Function ----
cell_width = 70
cell_height = 40
calendar_cells = {}  # Map canvas item ID to (date_str)

def draw_calendar():
    canvas.delete("all")
    calendar_cells.clear()

    year = year_var.get()
    month = months.index(month_var.get()) + 1

    cal = calendar.monthcalendar(year, month)
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    # Draw headers
    for col, day in enumerate(days):
        canvas.create_text(col * cell_width + 35, 20, text=day, font=("Arial", 10, "bold"))

    today = datetime.today()
    for row in range(6):
        for col in range(7):
            try:
                day = cal[row][col]
            except IndexError:
                day = 0

            x1 = col * cell_width
            y1 = row * cell_height + 30
            x2 = x1 + cell_width
            y2 = y1 + cell_height

            if day != 0:
                date_str = f"{year}-{month:02d}-{day:02d}"
                fill_color = "lightyellow"

                # Highlight today
                if (day == today.day and month == today.month and year == today.year):
                    fill_color = "lightgreen"

                rect_id = canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="black")
                text_id = canvas.create_text(x1 + 35, y1 + 20, text=str(day), font=("Arial", 10))
                calendar_cells[rect_id] = date_str
                calendar_cells[text_id] = date_str  # Make text also clickable

# ---- On Click Handler ----
def on_canvas_click(event):
    item = canvas.find_closest(event.x, event.y)[0]
    date_str = calendar_cells.get(item)
    if date_str:
        note = event_notes.get(date_str, "No events.")
        selected_info.set(f"{date_str}: {note}")

# ---- Bindings ----
canvas.bind("<Button-1>", on_canvas_click)
month_combo.bind("<<ComboboxSelected>>", lambda e: draw_calendar())
year_spin.bind("<KeyRelease>", lambda e: draw_calendar())
year_spin.bind("<ButtonRelease-1>", lambda e: draw_calendar())

# ---- Initial Render ----
draw_calendar()

root.mainloop()
