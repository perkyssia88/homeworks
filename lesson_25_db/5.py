import sqlite3

connect = sqlite3.connect("hw.db")
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS text_tab(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS int_tab(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)""")
connect.commit()

lst = [192, 168, "Python", 0, 1, "world", 255, 255, 0, 0]

for i in lst:
    if isinstance(i, int):
        if i % 2 == 0:
            cursor.execute("""INSERT INTO int_tab(col_1) VALUES (?)""", (i,))
            connect.commit()
        else:
            cursor.execute("""INSERT INTO int_tab(col_1) VALUES (?)""", ("нечетное",))
            connect.commit()
    if isinstance(i, str):
        cursor.execute("""INSERT INTO text_tab(col_1) VALUES (?)""", (i,))
        connect.commit()
        cursor.execute("""INSERT INTO int_tab(col_1) VALUES (?)""", (len(i),))
        connect.commit()

cursor.execute("""SELECT*FROM int_tab""")
int_result = cursor.fetchall()
if len(int_result) > 5:
    cursor.execute('''DELETE FROM text_tab WHERE id=1''')
    connect.commit()
else:
    cursor.execute('''UPDATE text_tab SET col_1='hello' FROM id=1''')
    connect.commit()
