import sqlite3

conn = sqlite3.connect("transactions.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
token TEXT PRIMARY KEY,
sender TEXT,
receiver TEXT,
amount REAL,
timestamp TEXT
)
""")

conn.commit()
conn.close()

print("Database ready")