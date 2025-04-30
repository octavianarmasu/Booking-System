import sqlite3

def add_rezervare(id_camera, id_hotel, data_cazare, data_eliberare):
    conn = sqlite3.connect('hotel_database.db')
    cursor = conn.execute('''SELECT MAX(id) FROM Rezervari;''')
    conn.execute('''PRAGMA foreign_keys = ON;''')

    command = f'INSERT INTO Rezervari VALUES({max + 1}, {data_cazare}, {data_eliberare}, {id_hotel}, {id_camera});'
    
    try:
        conn.execute(command)
    except sqlite3.Error as error:
        print('Error occurred - ', error)
        return -1

    cursor.close()
    conn.execute('COMMIT')
    conn.close()
    return max + 1

def check_rooms_etaj_tip(nume_hotel, etaj, data_cazare, data_eliberare, tip):
    conn = sqlite3.connect('hotel_database.db')

    try:
        cursor = conn.execute(f'''SELECT *
        FROM Rooms
        WHERE id_hotel IN (SELECT id FROM Hotels WHERE nume LIKE '{nume_hotel}') AND etaj == {etaj} AND tip LIKE '{tip}' AND
        id_camera NOT IN (SELECT id_camera FROM Rezervari WHERE data_cazare < {data_cazare} AND data_eliberare > {data_eliberare});''')
    except sqlite3.Error as error:
        print('Error occurred - ', error)
        return []

    tabel = []
    for row in cursor:
        tabel.append({'ID Hotel': row[0], 'ID Camera': row[1], 'Numar Camera': row[2], 'Tip Camera': row[3], 'Etaj': row[4], 'Pozitionare camera': row[5]})
   
    cursor.close()
    conn.close()
    return tabel

def check_rooms_etaj(nume_hotel, etaj, data_cazare, data_eliberare):
    conn = sqlite3.connect('hotel_database.db')
    try:
        cursor = conn.execute(f'''SELECT *
        FROM Rooms
        WHERE id_hotel IN (SELECT id FROM Hotels WHERE nume LIKE '{nume_hotel}') AND etaj == {etaj} AND
        id_camera NOT IN (SELECT id_camera FROM Rezervari WHERE data_cazare < {data_cazare} AND data_eliberare > {data_eliberare});''')
    except sqlite3.Error as error:
        print('Error occurred - ', error)
        return []

    tabel = []
    for row in cursor:
        tabel.append({'ID Hotel': row[0], 'ID Camera': row[1], 'Numar Camera': row[2], 'Tip Camera': row[3], 'Etaj': row[4], 'Pozitionare camera': row[5]})
   
    cursor.close()
    conn.close()
    return tabel

def check_rooms_tip(nume_hotel, data_cazare, data_eliberare, tip):
    conn = sqlite3.connect('hotel_database.db')
    try:
        cursor = conn.execute(f'''SELECT *
        FROM Rooms
        WHERE id_hotel IN (SELECT id FROM Hotels WHERE nume LIKE '{nume_hotel}') AND tip LIKE '{tip}' AND
        id_camera NOT IN (SELECT id_camera FROM Rezervari WHERE data_cazare < {data_cazare} AND data_eliberare > {data_eliberare});''')
    except sqlite3.Error as error:
        print('Error occurred - ', error)
        return []

    tabel = []
    for row in cursor:
        tabel.append({'ID Hotel': row[0], 'ID Camera': row[1], 'Numar Camera': row[2], 'Tip Camera': row[3], 'Etaj': row[4], 'Pozitionare camera': row[5]})
   
    cursor.close()
    conn.close()
    return tabel

def chech_rezervare(id):
    conn = sqlite3.connect('hotel_database.db')
    try:
        cursor = conn.execute(f'''SELECT * FROM Rezervari WHERE id == {id}''')
    except sqlite3.Error as error:
        print('Error occurred - ', error)
        return []

    tabel = []
    for row in cursor:
        tabel.append({'ID': row[0], 'Data Cazare': row[1], 'Data Eliberare': row[2], 'ID Hotel': row[3], 'ID Camera': row[4]})
    
    cursor.close()
    conn.close()
    return tabel

print(chech_rezervare(0))
