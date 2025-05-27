import sqlite3

# conn.execute('''CREATE TABLE Hotels(
    # id INTEGER PRIMARY KEY,
    # nume TEXT NOT NULL,
    # dresa TEXT NOT NULL,
    # email TEXT,
    # telefon TEXT
    # );''')    

conn = sqlite3.connect('hotel_database.db')

# cursor = conn.execute('ALTER TABLE Hotels ADD Rating INTEGER;')
# cursor = conn.execute('ALTER TABLE Hotels ADD Price INTEGER;')
# cursor = conn.execute('ALTER TABLE Hotels ADD Stars INTEGER;')
# cursor = conn.execute('ALTER TABLE Hotels ADD Facilities TEXT;')
# cursor = conn.execute('ALTER TABLE Rezervari ADD email TEXT;')
# cursor = conn.execute('ALTER TABLE Hotels ADD Photo BLOB;')
# cursor = conn.execute('''DROP TABLE Reviews;''')
# cursor = conn.execute('''CREATE TABLE Reviews(
# User_email TEXT NOT NULL,
# Hotel_ID INTEGER NOT NULL,
# Review TEXT,
# FOREIGN KEY (Hotel_ID) REFERENCES Hotels(id),
# FOREIGN KEY (User_email) REFERENCES Users(Email),
# CONSTRAINT UNIQUE_REVIEWS unique(User_email, Hotel_ID));''')
# cursor = conn.execute('''UPDATE Hotels SET Rating = 4.5, Price = 200, Stars = 4, Facilities = 'Wi-Fi, Private Beach, Pool, Breakfeast Included' WHERE id = 1;''')

# cursor = conn.execute('''DELETE FROM Reviews WHERE Hotel_ID = 1''')
# cursor = conn.execute('''INSERT INTO Reviews VALUES('test@gmail.com', 1, 'Amazing views and friendly staff!');''')
# cursor = conn.execute('''INSERT INTO Reviews VALUES('dantunsoiu@gmail.com', 1, 'Loved the food and pool area.');''')
conn.execute('''PRAGMA foreign_keys = ON;''')
# cursor = conn.execute('''INSERT INTO Reviews VALUES('dantunsoiu@gmail.com', 7, 'Loved the food and pool area.');''')
cursor = conn.execute('''SELECT * FROM Hotels;''')

# blobData = 0
# with open("photos/Italy/image1.png", 'rb') as file:
#     blobData = file.read()
# command = f'''INSERT INTO Hotels VALUES(2, "Bella Vista Hotel", "Sicily, Italy", "bella_vista@gmail.com", "0683359359", "4.5", "150", "4", "Wi-Fi, Pool, Private Beach, Breakfast Included", ?);'''
# try:
#     conn.execute('''INSERT INTO Hotels VALUES(2, "Bella Vista Hotel", "Sicily, Italy", "bella_vista@gmail.com", "0683359359", "4.5", "150", "4", "Wi-Fi, Pool, Private Beach, Breakfast Included", 0);''')
# except sqlite3.Error as error:
#     print(error)

# conn.execute('''INSERT INTO Hotels VALUES(3, "Ocean Breeze Hotel", "Madeira, Portugal", "ocean_breeze@gmail.com", "06577359359", "4.2", "180", "4", "Wi-Fi, Pool, Beach Access, Air Conditioning", 0);''')
# conn.execute('''INSERT INTO Hotels VALUES(4, "Aegean Paradise Hotel", "Evia Greece", "aegean_paradise@gmail.com", "01957159359", "4.7", "120", "4", "Wi-Fi, Pool, Private Beach, Breakfast Included, Spa", 0);''')
# conn.execute('''INSERT INTO Rooms VALUES(2, 5, 1, "apartment", 1, "middle");''')
# conn.execute('''INSERT INTO Rooms VALUES(2, 6, 2, "duplex", 1, "middle");''')
# conn.execute('''INSERT INTO Rooms VALUES(3, 7, 1, "apartment", 1, "middle");''')
# conn.execute('''INSERT INTO Rooms VALUES(3, 8, 2, "single", 1, "middle");''')
# conn.execute('''INSERT INTO Rooms VALUES(4, 9, 1, "apartment", 1, "middle");''')
# conn.execute('''INSERT INTO Rooms VALUES(4, 10, 2, "single", 1, "middle");''')

cursor = conn.execute('''SELECT * FROM Hotels;''')
tabel = []
for row in cursor:
    tabel.append({'ID': row[0], 'Nume': row[1], 'Adresa': row[2], 'Email': row[3], 'Numar Telefon': row[4], 'Rating': row[5], 'Price': row[6], 'Stars': row[7], 'Facilities': row[8]})
print(tabel)

tabel = []
cursor = conn.execute('''SELECT * FROM Reviews WHERE Hotel_ID = 1''')
for row in cursor:
    tabel.append({'User Email': row[0], 'Hotel ID': row[1], 'Review': row[2]})
print(tabel)

conn.execute('COMMIT')

print('\n')