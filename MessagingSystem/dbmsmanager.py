import sqlite3

def connect():
    conn = sqlite3.connect('text_messenger.db')
    cursor = conn.cursor()
    return conn, cursor

def disconnect(conn):

    conn.commit()
    conn.close()

def create_tables():

    conn, cursor = connect()
    # Create users table

    # Create contacts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    carrier TEXT
    ) """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL) """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL)""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS group_contact (
    group_id INTEGER,
    contact_id INTEGER,
    PRIMARY KEY(group_id, contact_id),
    FOREIGN KEY(contact_id) REFERENCES contacts(id),
    FOREIGN KEY(group_id) REFERENCES groups(id))""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS event_contact (
    event_id INTEGER,
    contact_id INTEGER,
    PRIMARY KEY(event_id, contact_id),
    FOREIGN KEY(contact_id) REFERENCES contacts(id),
    FOREIGN KEY(event_id) REFERENCES event(id))""")

    disconnect(conn)

def display_tables():
    conn,cursor = connect()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        print(f"Table: {table[0]}")
        cursor.execute(f"PRAGMA table_info({table[0]});")
        columns = cursor.fetchall()
        for column in columns:
            print(column)

    conn.close()

def display_data():
    conn,cursor = connect()

    cursor.execute("SELECT * FROM contacts;")
    print("Contacts:", cursor.fetchall())

    cursor.execute("SELECT * FROM groups;")
    print("Groups:", cursor.fetchall())

    cursor.execute("SELECT * FROM events;")
    print("Events:", cursor.fetchall())

    cursor.execute("SELECT * FROM group_contact;")
    print("Group Contacts:", cursor.fetchall())

    cursor.execute("SELECT * FROM event_contact;")
    print("Event Contacts:", cursor.fetchall())

    conn.close()

def store_contacts(contact_info):
    """
        Stores a contact in the database.

        Parameters:
        - conn: SQLite3 connection object
        - contact_info: Dictionary with keys ['name', 'phone', 'carrier']

        Example:
        contact_data = {"name": "John Doe", "phone": "555-1234", "carrier": "Verizon"}
        store_contact(conn, contact_data)
        """
    conn,cursor = connect()
    cursor.executemany("""
            INSERT INTO contacts (name, phone, carrier) 
            VALUES (?, ?, ?)
        """, (contact_info["name"], contact_info["phone"], contact_info.get("carrier", None)))
    disconnect(conn)

    return None

def store_event(event_info):
    return None

if __name__ == '__main__':
    create_tables()
    display_tables()
    display_data()