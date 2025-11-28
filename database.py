import sqlite3

conn = sqlite3.connect('survey.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    facility TEXT,
    rating INTEGER,
    comment TEXT
)
''')

conn.commit()
conn.close()
