import sqlite3

# conn.execute('''CREATE TABLE Hotels(
    # id INTEGER PRIMARY KEY,
    # nume TEXT NOT NULL,
    # dresa TEXT NOT NULL,
    # email TEXT,
    # telefon TEXT
    # );''')    

conn = sqlite3.connect('hotel_database.db')
cursor = conn.execute('''SELECT * FROM Hotels;''')
tabel = []
for row in cursor:
    tabel.append({'ID': row[0], 'Nume': row[1], 'Adresa': row[2], 'Email': row[3], 'Numar Telefon': row[4]})
print(tabel)

print('\n')