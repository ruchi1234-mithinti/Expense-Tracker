import sqlite3

DB_NAME = "tracker.db"

def get_connection():
    """Returns a connection to the SQLite database."""
    return sqlite3.connect(DB_NAME)

def initialize_db():
    """Creates the income and expenses tables if they do not exist."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create income table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS income (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            source TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    
    # Create expenses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()