import sqlite3

# Connect and create table
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        grade TEXT
    )
""")

conn.commit()
conn.close()
print("Table 'students' created successfully.")
