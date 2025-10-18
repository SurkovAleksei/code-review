
def create_table(cur, conn):
    cur.execute('DROP TABLE IF EXISTS shop')

    cur.execute('''
        CREATE TABLE shop (
            id INTEGER PRIMARY KEY,
            product VARCHAR(255),
            cost VARCHAR(255)
        )
    ''')
    conn.commit()
