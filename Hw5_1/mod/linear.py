import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def linear(data):

    
    # Определение признаков и целевой переменной
    X = data.drop(columns=['Цена_завтра'])
    y = data['Цена_завтра']
    
    # Разделение данных на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Проверка размера обучающих и тестовых выборок
    print("Размер обучающей выборки:", len(X_train))
    print("Размер тестовой выборки:", len(X_test))
    
    # Определение и обучение модели линейной регрессии
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Прогнозирование
    y_pred = model.predict(X_test)
    return y_test,y_pred