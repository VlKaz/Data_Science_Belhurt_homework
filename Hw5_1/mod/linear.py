import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def linear(data):
    # Определение признаков и целевой переменной
    X = data.drop(columns=["Откр.","Объём"])
    y = data["Откр."]
    
    # Разделение данных на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Определение и обучение модели линейной регрессии
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Прогнозирование
    y_pred = model.predict(X_test)
    return y_test,y_pred