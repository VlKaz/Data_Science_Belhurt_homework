import pandas as pd
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor
from sklearn.model_selection import GridSearchCV

def catboost(data):
    # Определение признаков и целевой переменной
    X = data.drop(columns=['Цена_завтра'])
    y = data['Цена_завтра']
    # Гиперпараметры
    param_grid = {
        'iterations': [100, 300, 500],
        'learning_rate': [0.01, 0.05, 0.1],
        'depth': [3, 4, 5, 6],
        'l2_leaf_reg': [1, 3, 5, 7],
        'border_count': [32, 64, 128],
        'subsample': [0.8, 0.9, 1.0]
    }

    model = CatBoostRegressor(silent=True)
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1, verbose=2)
    grid_search.fit(X, y)
    
    print("Лучшие параметры:", grid_search.best_params_)
    print("Лучшее значение MSE:", -grid_search.best_score_)
    
    bestmodel = grid_search.best_estimator_
    # Разделение данных на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


    # Создание и обучение модели CatBoost для регрессии
    bestmodel = CatBoostRegressor(iterations=1000, learning_rate=0.05, depth=6, random_state=42, verbose=0)
    bestmodel.fit(X_train, y_train)
    
   
    # Предсказание на тестовой выборке
    y_pred = bestmodel.predict(X_test)
    
    return y_test,y_pred