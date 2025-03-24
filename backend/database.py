# RIQA_Software/backend/database.py
import sqlite3

def init_db():
    conn = sqlite3.connect('riqa.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS papers
                 (id INTEGER PRIMARY KEY, title TEXT, author TEXT)''')
    conn.commit()
    conn.close()

def fetch_papers():  # Aggiungi questa funzione mancante
    conn = sqlite3.connect('riqa.db')
    c = conn.cursor()
    c.execute("SELECT * FROM papers")
    papers = c.fetchall()
    conn.close()
    return [{"id": p[0], "title": p[1], "author": p[2]} for p in papers]
