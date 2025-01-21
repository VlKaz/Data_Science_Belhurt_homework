import sqlite3

def clear_table(filedb):
    # Подключение к базе данных SQLite
    conn = sqlite3.connect(filedb)
    cursor = conn.cursor()
    # Удаление строк, где в столбце horsepower есть значение "?" 
    cursor.execute('DELETE FROM auto WHERE "horsepower" = "?"') 
    # Сохранение изменений 
    conn.commit()
    # Отключаемся от DB
    conn.close()