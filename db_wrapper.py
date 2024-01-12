import sqlite3

class DB():
    def __init__(self, name):
        
        self.create_db(name)
    
    def create_db(self, name):

        self.conn = sqlite3.connect(f'{name}.db')
        self.cursor = self.conn.cursor()
        self.conn.commit()

    def creat_table(self, name):

        self.cursor = self.conn.cursor()
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                User TEXT,
                Text TEXT
            )
        ''')

        self.conn.commit()
        print(f"{name} created")

    def get_table(self, table_name):

        self.cursor = self.conn.cursor()
        self.cursor.execute(f'SELECT * FROM {table_name}')
        return self.cursor.fetchall()
    
    def get_table_items(self, table_name, start, stop):

        self.cursor = self.conn.cursor()
        table = self.cursor.execute(f'SELECT * FROM {table_name}')

        items = table.fetchall()
        return items[start: stop]
    
    def get_table_last_ten(self, table_name):

        self.cursor = self.conn.cursor()
        table = self.cursor.execute(f'SELECT * FROM {table_name}')

        items = table.fetchall()
        return items[-10 : ]
    
    def insert(self, item):

        print(item[0], item[1])
        user, text = item[0], item[1]

        self.cursor = self.conn.cursor()
        self.cursor.execute('INSERT INTO Chats (User, Text) VALUES (?, ?)', (user, text))
        self.conn.commit()
        print(f"{item} inserted")