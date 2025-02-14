from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np
best_params = {
    'learning_rate': 0.05,
    'max_depth': 3,
    'min_samples_leaf': 2,
    'min_samples_split': 10,
    'n_estimators': 300,
    'subsample': 0.8
}

def crossvalgbr(data):
    X = data.drop(columns=['Цена_завтра'])
    y = data['Цена_завтра']
    
    model = GradientBoostingRegressor(**best_params)
    
    # 5-кратная кросс-валидация
    mse_scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
    r2_scores = cross_val_score(model, X, y, cv=5, scoring='r2')
    mae_scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_absolute_error')
    mape_scores = np.mean(np.abs(cross_val_score(model, X, y, cv=5, scoring='neg_mean_absolute_percentage_error'))) * 100

    mse_scores = -mse_scores  
    mae_scores = -mae_scores

    print(f"Среднее MSE при кросс-валидации: {np.mean(mse_scores)}")
    print(f"Среднее R² при кросс-валидации: {np.mean(r2_scores)}")
    print(f"Среднее MAE при кросс-валидации: {np.mean(mae_scores)}")
    print(f"Среднее MAPE при кросс-валидации: {mape_scores}%")