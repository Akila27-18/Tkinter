import sqlite3

dummy_data = [
    ("Alice", 17, "A"), ("Bob", 18, "B"), ("Charlie", 16, "A"),
    ("David", 17, "C"), ("Eva", 19, "B"), ("Frank", 16, "C"),
    ("Grace", 18, "A"), ("Helen", 17, "B"), ("Ian", 16, "C"),
    ("Jane", 19, "A")
]

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", dummy_data)

conn.commit()
conn.close()
print("Dummy data inserted successfully.")
