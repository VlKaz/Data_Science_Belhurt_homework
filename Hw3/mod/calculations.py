import sqlite3

def calculations(filedb):
    # Подключение к базе данных SQLite
    conn = sqlite3.connect(filedb)
    cursor = conn.cursor()
    
    # Вычисляем средню стоимости седанов
    avg_price_sedan = cursor.execute('SELECT AVG(price) FROM auto WHERE "body-style" = "sedan"').fetchone()[0]
    # Вычисляем средню стоимость универсалов
    avg_price_wagon = cursor.execute('SELECT AVG(price) FROM auto WHERE "body-style" = "wagon"').fetchone()[0]
    
    print(f"Средняя стоимость седанов: {round(avg_price_sedan)} в $")
    print(f"Средняя стоимость универсалов: {round(avg_price_wagon)} в $")

    # Подсчитываем сколько машин на бензине и сколько на дизеле
    count_fueltype = cursor.execute('SELECT "fuel-type", COUNT(*) FROM auto GROUP BY "fuel-type"').fetchall()
    print(f"На каком топливе и сколько: {count_fueltype}")

    # Вычисляем средню стоимости седанов
    max_price = cursor.execute('SELECT * FROM auto ORDER BY price DESC LIMIT 1').fetchone()
    min_price = cursor.execute('SELECT * FROM auto ORDER BY price ASC LIMIT 1').fetchone()
    
    print(f"Самая дорогая машина: {max_price[1]} стоимостью {max_price[7]} $")
    print(f"Самая дешовая машина: {min_price[1]} стоимостью {min_price[7]} $")
    conn.close()