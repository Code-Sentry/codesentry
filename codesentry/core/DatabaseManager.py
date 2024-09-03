import sqlite3

class DatabaseManager:
    def __init__(self, db_name='codesentry.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_table()
        
    def insertVulnerability(self, description, severity):
        
        self.cursor.execute('''
            INSERT INTO vulnerabilities (description, severity, createdAt)
            VALUES (?, ?, datetime('now'))
        ''', (description, severity))
        
        self.connection.commit()