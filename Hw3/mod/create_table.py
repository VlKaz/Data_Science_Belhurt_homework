import pandas as pd
import sqlite3

def create_table(filename,filedb):
    # Загрузка данных из CSV
    df = pd.read_csv(filename)
    
    # Выбор определенных столбцов
    selected_columns = df[['make', 'fuel-type', 'aspiration','body-style','drive-wheels','horsepower','price']]
    
    # Подключение к базе данных SQLite
    conn = sqlite3.connect(filedb)
    cursor = conn.cursor()

    # Удаление таблицы, если она уже существует 
    cursor.execute('DROP TABLE IF EXISTS auto')
    
    # Создание таблицы в базе данных
    cursor.execute('''
    CREATE TABLE auto (
        id INTEGER PRIMARY KEY,
        make TEXT,
        "fuel-type" TEXT,
        aspiration TEXT,
        "body-style" TEXT,
        "drive-wheels" TEXT,
        horsepower INTEGER,
        price INTEGER
    )
    ''')
    
    # Перенос данных в таблицу
    selected_columns.to_sql('auto', conn, if_exists='append', index=False)

    # Проверка, что таблица создана 
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='auto';") 
    table_exists = cursor.fetchone() 
    if table_exists: 
        print("Таблица успешно создана.") 
    else: 
        print("Таблица не найдена.")
        
    conn.close()