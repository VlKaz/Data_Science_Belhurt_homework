import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd
def visual(filedb):
    # Подключение к базе данных sql
    conn = sqlite3.connect(filedb)
    
    # Загрузка данных из sql в df
    df = pd.read_sql_query("SELECT * FROM auto", conn)
    
    # Закрытие соединения c DB
    conn.close()
    
    # Построение графиков с использованием seaborn
    # График распределения цен автомобилей
    plt.figure(figsize=(10, 6))
    sns.histplot(df['price'], kde=True)
    plt.title('Распределение цен автомобилей')
    plt.xlabel('Цена')
    plt.ylabel('Количество')
    plt.show()
    
    # График зависимости мощности от цены
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='horsepower', y='price', data=df)
    plt.title('Зависимость мощности от цены')
    plt.xlabel('Мощность')
    plt.ylabel('Цена')
    plt.show()
    
    # График распределения типов кузова
    plt.figure(figsize=(10, 6))
    sns.countplot(x='body-style', data=df)
    plt.title('Распределение типов кузова')
    plt.xlabel('Тип кузова')
    plt.ylabel('Количество')
    plt.show()