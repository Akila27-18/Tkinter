import tkinter as tk
from tkinter import ttk

# Country to City mapping
country_city = {
    "India": ["Delhi", "Mumbai", "Chennai", "Bangalore"],
    "USA": ["New York", "Los Angeles", "Chicago", "Houston"],
    "UK": ["London", "Manchester", "Liverpool"],
    "Australia": ["Sydney", "Melbourne", "Brisbane"]
}

def update_cities(event):
    selected_country = country_cb.get()
    cities = country_city.get(selected_country, [])
    
    # Clear and update the city combobox
    city_cb['values'] = cities
    city_cb.set('')  # Clear previous selection

def show_selection():
    print(f"Country: {country_cb.get()} | City: {city_cb.get()}")

root = tk.Tk()
root.title("Dependent Dropdown Example")

# Country Combobox
tk.Label(root, text="Select Country:").pack(pady=(10, 0))
country_cb = ttk.Combobox(root, values=list(country_city.keys()), state="readonly")
country_cb.pack()
country_cb.bind("<<ComboboxSelected>>", update_cities)

# City Combobox
tk.Label(root, text="Select City:").pack(pady=(10, 0))
city_cb = ttk.Combobox(root, state="readonly")
city_cb.pack()

# Button to display selection
tk.Button(root, text="Show Selection", command=show_selection).pack(pady=10)

root.mainloop()
