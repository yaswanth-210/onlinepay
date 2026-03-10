import tkinter as tk
import sqlite3

def show_history():

    win = tk.Toplevel()
    win.title("Transaction History")
    win.geometry("500x400")

    text = tk.Text(win)
    text.pack()

    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")

    rows = cursor.fetchall()

    for r in rows:
        text.insert(tk.END,str(r)+"\n")

    conn.close()