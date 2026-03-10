import sqlite3

conn = sqlite3.connect("transactions.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
id TEXT,
token TEXT,
sender TEXT,
receiver TEXT,
amount INTEGER
)
""")

conn.commit()
conn.close()

print("Database Ready")