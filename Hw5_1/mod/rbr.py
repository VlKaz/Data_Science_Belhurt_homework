import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor

def gbr(data):
    # Определение признаков и целевой переменной
    X = data.drop(columns=['Цена_завтра'])
    y = data['Цена_завтра']
    # Гиперпараметры подбор
    param_grid = {
        'n_estimators': [100, 200, 300],
        'learning_rate': [0.01, 0.05, 0.1],
        'max_depth': [3, 4, 5],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'subsample': [0.8, 0.9, 1.0]
    }
    gbr = GradientBoostingRegressor()
    grid_search = GridSearchCV(estimator=gbr, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1, verbose=2)
    grid_search.fit(X, y)
    print("Лучшие параметры:", grid_search.best_params_)
    print("Лучшее значение MSE:", -grid_search.best_score_)
    model = grid_search.best_estimator_
    # Разделение данных на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

   # Обучение
    model.fit(X_train, y_train)

    # Предсказание на тестовой выборке
    y_pred = model.predict(X_test)
    
    return y_test,y_pred