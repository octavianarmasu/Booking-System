import sqlite3

def add_rezervare(id_camera, id_hotel, data_cazare, data_eliberare, email):
    conn = sqlite3.connect('hotel_database.db')
    conn.execute('''PRAGMA foreign_keys = ON;''')
    
    cursor = conn.execute('''SELECT MAX(id) FROM Rezervari;''')
    max_id = cursor.fetchone()[0]
    next_id = 1 if max_id is None else max_id + 1

    try:
        conn.execute('''INSERT INTO Rezervari VALUES(?, ?, ?, ?, ?, ?);''',
                    (next_id, data_cazare, data_eliberare, id_hotel, id_camera, email))
        conn.execute('COMMIT')
        return next_id
    except sqlite3.Error as error:
        print('Error occurred - ', error)
        return -1
    finally:
        conn.close()

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

def check_available_room(nume_hotel, tip, pozitionare, data_cazare, data_eliberare):
    conn = sqlite3.connect('hotel_database.db')
    conn.execute('PRAGMA foreign_keys = ON;')

    try:
        cursor = conn.execute(f'''
            SELECT *
            FROM Rooms
            WHERE id_hotel IN (SELECT id FROM Hotels WHERE nume LIKE ?) 
            AND tip LIKE ?
            AND pozitionare LIKE ?
            AND id_camera NOT IN (
                SELECT id_camera 
                FROM Rezervari 
                WHERE data_cazare < ? AND data_eliberare > ?
            )
            ORDER BY etaj;
        ''', (nume_hotel, tip, pozitionare, data_eliberare, data_cazare))
        
        result = cursor.fetchone()
        if result:
            return {
                'ID Hotel': result[0],
                'ID Camera': result[1],
                'Numar Camera': result[2],
                'Tip Camera': result[3],
                'Etaj': result[4],
                'Pozitionare camera': result[5]
            }
        return None
        
    except sqlite3.Error as error:
        print('Error occurred - ', error)
        return None
    finally:
        conn.close()


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
    try:
        # Search for the email in the Users table
        cursor = conn.execute('SELECT Password FROM Users WHERE Email = ?;', (email,))
        result = cursor.fetchone() 

        if result is None:
            # No user found with that email
            return False

        # Check if the password matches
        db_password = result[0]
        return db_password == password
    except sqlite3.Error as error:
        print('Error occurred - ', error)
        return False
    finally:
        conn.close()

def get_hotels():
    conn = sqlite3.connect('hotel_database.db')
    cursor = conn.execute('''SELECT * FROM Hotels;''')

    tabel = []
    for row in cursor:
        tabel.append({'ID': row[0], 'Nume': row[1], 'Adresa': row[2], 'Email': row[3], 'Numar Telefon': row[4], 'Rating': row[5], 'Price': row[6], 'Stars': row[7], 'Facilities': row[8]})

    cursor.close()
    conn.close()
    return tabel

def check_reviews_for_hotel(id):
    conn = sqlite3.connect('hotel_database.db')

    tabel = []
    cursor = conn.execute(f'''SELECT * FROM Reviews WHERE Hotel_ID = {id};''')
    for row in cursor:
        tabel.append({'User Email': row[0], 'Hotel ID': row[1], 'Review': row[2]})

    cursor.close()
    conn.close()
    return tabel

def check_reviews_for_user(email):
    conn = sqlite3.connect('hotel_database.db')

    tabel = []
    cursor = conn.execute(f'''SELECT * FROM Reviews WHERE User_email = '{email}';''')
    for row in cursor:
        tabel.append({'User Email': row[0], 'Hotel ID': row[1], 'Review': row[2]})

    cursor.close()
    conn.close()
    return tabel

def get_user_information(email):
    conn = sqlite3.connect('hotel_database.db')

    tabel = []
    cursor = conn.execute(f'''SELECT * FROM Users WHERE Email = '{email}';''')
    for row in cursor:
        tabel.append({'User Email': row[0], 'First Name': row[1], 'Last Name': row[2], 'Phone': row[3]})

    cursor.close()
    conn.close()
    return tabel

def add_review(email, hotel_id, review):
    conn.execute('''PRAGMA foreign_keys = ON;''')
    conn = sqlite3.connect('hotel_database.db')
    command = f'''INSERT INTO Reviews VALUES('{email}', {hotel_id}, '{review}');'''

    try:
        conn.execute(command)
    except sqlite3.Error as error:
        print('Error occurred - ', error)
        return -1

    conn.execute('COMMIT')
    conn.close()
    return 0

def check_email_exists(email):
    conn = sqlite3.connect('hotel_database.db')
    try:
        cursor = conn.execute('SELECT 1 FROM Users WHERE Email = ?;', (email,))
        return cursor.fetchone() is not None
    except sqlite3.Error as error:
        print('Error occurred - ', error)
        return False
    finally:
        conn.close()

def update_user_password(email, new_password):
    conn = sqlite3.connect('hotel_database.db')
    try:
        cursor = conn.execute('UPDATE Users SET Password = ? WHERE Email = ?;', (new_password, email))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as error:
        print('Error occurred - ', error)
        return False
    finally:
        conn.close()


def get_rezervari_for_user(email):
    conn = sqlite3.connect('hotel_database.db')
    cursor = conn.execute(f'''SELECT * FROM Rezervari WHERE email = '{email}';''')

    table = []
    for row in cursor:
        table.append({"ID_Rezervare": row[0], "ID_Hotel": row[3], "ID_Camera": row[4], "Data_cazare": row[1], "Data_eliberare": row[2], "Email_user": row[5]})
    
    cursor.close()
    conn.close()
    return table


