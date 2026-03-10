from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/sync")
def sync():

    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")
    data = cursor.fetchall()

    conn.close()

    return {"transactions": data}

if __name__ == "__main__":
    app.run(port=5000)