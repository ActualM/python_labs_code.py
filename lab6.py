import sqlite3

def lab6(table_txt):
    username = 0
    email = 0
    age = 0
    count = 0
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER
        )
        ''')
    word_count = 0
    for text in table_txt:
        count = 0

        words = text.split()

        for data in words:
            count = count + 1
            if count == 1:
                username = data
            if count == 2:
                email = data
            if count == 3:
                age = data
                cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)',
                   (username, email, age))
                connection.commit()
    for value in cursor.execute("SELECT * FROM users"):
        print(value)




path_to_file = open('test.txt')
lab6(path_to_file)