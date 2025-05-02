import sqlite3

def add_rezervare(id_camera, id_hotel, data_cazare, data_eliberare):
    conn = sqlite3.connect('hotel_database.db')
    cursor = conn.execute('''SELECT MAX(id) FROM Rezervari;''')
    for row in cursor:
        max = row[0]
    conn.execute('''PRAGMA foreign_keys = ON;''')

    command = f'INSERT INTO Rezervari VALUES({max + 1}, {data_cazare}, {data_eliberare}, {id_hotel}, {id_camera});'
    
    try:
        conn.execute(command)
    except sqlite3.Error as error:
        print('Error occurred - ', error)
        return -1

    # cursor = conn.execute('''SELECT * FROM Rezervari''')
    # for row in cursor:
    #     print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]))

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

def add_user(email, first_name, last_name, phone, password):
    conn = sqlite3.connect('hotel_database.db')
    command = f'''INSERT INTO Users VALUES('{email}', '{first_name}', '{last_name}', '{phone}', '{password}');'''

    try:
        conn.execute(command)
    except sqlite3.Error as error:
        print('Error occurred - ', error)
        return -1

    conn.execute('COMMIT')
    conn.close()
    return 0

def login_check_info(email, password):
    conn = sqlite3.connect('hotel_database.db')
    cursor = conn.execute('SELECT * FROM Users;')

    tabel = []
    for row in cursor:
        tabel.append({'Email': row[0], 'First Name': row[1], 'Last Name': row[2], 'Phone': row[3], 'Password': row[4]})
    # print(tabel)

    if len(tabel) < 1:
        return False

    if tabel[0]['Password'] == password:
        return True
    else:
        return False

add_user('example@email.com', 'User', 'Example', '000000001', 'example_password')
print(login_check_info('example@email.com', 'example_password'))

