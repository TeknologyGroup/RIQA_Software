import sqlite3
from sqlite3 import Error

DB_PATH = 'riqa_data.db'  # Percorso relativo al file

def init_db():
    conn = sqlite3.connect(DB_PATH)  # Crea/collegati al database
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS experiments
                      (id INTEGER PRIMARY KEY, input TEXT, result TEXT)''')
    conn.commit()
    conn.close()
