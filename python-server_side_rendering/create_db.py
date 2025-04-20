import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # 1. Create table if it doesn’t exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id       INTEGER PRIMARY KEY,
            name     TEXT    NOT NULL,
            category TEXT    NOT NULL,
            price    REAL    NOT NULL
        )
    ''')

    # 2. (Re)insert our sample data
    #    We use REPLACE INTO so re‑running this script won’t error if data already exists
    cursor.execute('''
        REPLACE INTO Products (id, name, category, price) VALUES
        (1, 'Laptop',     'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods',  15.99)
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    print("products.db created/updated with sample data.")
