import sqlite3

def main():
    conn = sqlite3.connect('hotel_database.db')
    cursor = conn.cursor()

    # conn.execute('''CREATE TABLE Hotels(
    # id INTEGER,
    # nume TEXT NOT NULL,
    # dresa TEXT NOT NULL,
    # email TEXT,
    # telefon TEXT,
    # CONSTRAINT pk_hotel PRIMARY KEY (id)
    # );''')

    # conn.execute('''CREATE TABLE Rooms(
    # id_hotel INTEGER,
    # id_camera INTEGER,
    # numar_camera INTEGER NOT NULL,
    # tip TEXT NOT NULL,
    # etaj INTEGER NOT NULL,
    # pozitionare TEXT NOT NULL,
    # CONSTRAINT pk_camera PRIMARY KEY (id_camera),
    # CONSTRAINT fk_camera_hotel FOREIGN KEY (id_hotel) REFERENCES Hotels(id)
    # );''')

    conn.execute('''CREATE TABLE Rezervari(
    id INTEGER,
    data_cazare INTEGER NOT NULL,
    data_eliberare INTEGER NOT NULL,
    id_hotel INTEGER,
    id_camera INTEGER,
    CONSTRAINT pk_rezervare PRIMARY KEY (id),
    CONSTRAINT fk_rezervare__hotel FOREIGN KEY (id_hotel) REFERENCES Hotels(id),
    CONSTRAINT fk_rezervare__camera FOREIGN KEY (id_camera) REFERENCES Rooms(id_camera)
    );''')

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

    cursor = conn.execute('''SELECT * FROM Hotels;''')
    tabel = []
    for row in cursor:
        tabel.append({'ID': row[0], 'Nume': row[1], 'Adresa': row[2], 'Email': row[3], 'Numar Telefon': row[4]})
    print(tabel)

    print('\n')

    cursor = conn.execute('''SELECT * FROM Rooms;''')
    tabel = []
    for row in cursor:
        tabel.append({'ID Hotel': row[0], 'ID Camera': row[1], 'Numar Camera': row[2], 'Tip Camera': row[3], 'Etaj': row[4], 'Pozitionare camera': row[5]})
    for row in tabel:
        print(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()