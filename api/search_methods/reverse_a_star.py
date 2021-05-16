import sqlite3

class ReverseAStar:
    def __init__(self, graph, target):
        self.map = graph
        self.target = target
    
    def initialise_db(self):
        connection = sqlite3.connect('reverse.db')
        with open('./api/search_methods/schema.sql') as schema:
            connection.executescript(schema.read())
        connection.commit()
        connection.close()
    
    def connecto_to_db(self):
        db = sqlite3.connect('reverse.db')
        return db