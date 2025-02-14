from sklearn.model_selection import cross_val_score
from catboost import CatBoostRegressor
import numpy as np
best_params = {
    'border_count': 128,
    'depth': 3,
    'iterations': 500,
    'l2_leaf_reg': 1,
    'learning_rate': 0.05,
    'subsample': 1.0
}
def crossvalcatb(data):
    X = data.drop(columns=['Цена_завтра'])
    y = data['Цена_завтра']
    
    model = CatBoostRegressor(
        border_count=best_params['border_count'],
        depth=best_params['depth'],
        iterations=best_params['iterations'],
        l2_leaf_reg=best_params['l2_leaf_reg'],
        learning_rate=best_params['learning_rate'],
        subsample=best_params['subsample'],
        silent=True
    )
    
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