import sqlite3

class DB_Controller:
    conn: sqlite3.Connection
    cursor: sqlite3.Cursor

    def __init__(self, db_name) -> None:
        self.db_name = db_name
    
    def open(self):
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    
    def init_table(self):
        self.open()
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS patient (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, email TEXT, phone TEXT, URL TEXT, symptoms TEXT)''')
        self.close()
    
    def get_data(self):
        self.open()
        self.cursor.execute('''SELECT * FROM patient''')
        data = self.cursor.fetchall()
        self.close()
        return data

    def add_data(self, data):
        self.open()
        self.cursor.execute('''INSERT INTO patient (name, email, phone, URL, symptoms) VALUES (?, ?, ?, ?, ?)''', data)
        self.conn.commit()
        self.close()

    def close(self):
        self.cursor.close()
        self.conn.close()

db = DB_Controller('main.db')
db.init_table()