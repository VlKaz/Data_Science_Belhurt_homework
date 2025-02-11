import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor

def catboost(data):
    # Определение признаков и целевой переменной
    X = data.drop(columns=["Откр.","Объём"])
    y = data["Откр."]
    
    # Разделение данных на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


    # Создание и обучение модели CatBoost для регрессии
    regressor = CatBoostRegressor(iterations=1000, learning_rate=0.05, depth=6, random_state=42, verbose=0)
    regressor.fit(X_train, y_train)
    
   
    # Предсказание на тестовой выборке
    y_pred = regressor.predict(X_test)
    
    return y_test,y_pred