import sqlite3

def main():
    conn = sqlite3.connect('hotel_database.db')
    cursor = conn.cursor()

    # conn.execute('''DROP TABLE Hotels''')
    # conn.execute('''DROP TABLE Rooms''')
    # conn.execute('''DROP TABLE Rezervari''')

    # conn.execute('''CREATE TABLE Hotels(
    # id INTEGER PRIMARY KEY,
    # nume TEXT NOT NULL,
    # dresa TEXT NOT NULL,
    # email TEXT,
    # telefon TEXT
    # );''')

    # conn.execute('''CREATE TABLE Rooms(
    # id_hotel INTEGER,
    # id_camera INTEGER PRIMARY KEY,
    # numar_camera INTEGER NOT NULL,
    # tip TEXT NOT NULL,
    # etaj INTEGER NOT NULL,
    # pozitionare TEXT NOT NULL,
    # FOREIGN KEY (id_hotel) REFERENCES Hotels(id)
    # );''')

    # conn.execute('''CREATE TABLE Rezervari(
    # id INTEGER PRIMARY KEY,
    # data_cazare INTEGER NOT NULL,
    # data_eliberare INTEGER NOT NULL,
    # id_hotel INTEGER,
    # id_camera INTEGER,
    # FOREIGN KEY (id_hotel) REFERENCES Hotels(id),
    # FOREIGN KEY (id_camera) REFERENCES Rooms(id_camera)
    # );''')

    conn.execute('''PRAGMA foreign_keys = ON;''')
    try:
        conn.execute('''INSERT INTO Hotels VALUES(1, 'Hotel Ritzz', 'Bucuresti, Strada Galati Nr.1', 'hotelritzz@gmail.com', '0722061583');''')
    except sqlite3.Error as error:
        print('Error occurred - ', error)

    try:
        conn.execute('''INSERT INTO Rooms VALUES(1, 1, 1, 'Apartament', 1, 'Colt');''')
    except sqlite3.Error as error:
        print('Error occurred - ', error)

    try:
        conn.execute('''INSERT INTO Rooms VALUES(1, 2, 2, 'Single Bed', 1, 'Colt');''')
    except sqlite3.Error as error:
        print('Error occurred - ', error)

    conn.execute('''INSERT INTO Rezervari VALUES(1, 20250420, 20250520, 1, 1);''')
    conn.execute('''INSERT INTO Rezervari VALUES(2, 20250521, 20250620, 1, 2);''')
    conn.execute('''INSERT INTO Rezervari VALUES(3, 20250320, 20250418, 1, 1);''')
    # conn.execute('''INSERT INTO Rezervari VALUES(0, 0, 0, 1, 1);''')

    cursor = conn.execute('''SELECT * FROM Hotels;''')
    tabel = []
    for row in cursor:
        tabel.append({'ID': row[0], 'Nume': row[1], 'Adresa': row[2], 'Email': row[3], 'Numar Telefon': row[4]})
    print(tabel)

    print('\n')

    cursor = conn.execute('''SELECT *
    FROM
    Rooms
    WHERE id_camera NOT IN (SELECT id_camera FROM Rezervari WHERE data_cazare < 20250922 AND data_eliberare > 20250922);''')
    tabel = []
    for row in cursor:
        tabel.append({'ID Hotel': row[0], 'ID Camera': row[1], 'Numar Camera': row[2], 'Tip Camera': row[3], 'Etaj': row[4], 'Pozitionare camera': row[5]})
    for row in tabel:
        print(row)

    cursor = conn.execute('''SELECT MAX(ifnull(id, 0)) FROM Rezervari;''')
    for row in cursor:
        print(row[0])

    # conn.execute('COMMIT')
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()