from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np

def mser2(y_test, y_pred):
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
    return mse, r2, mae, mape
    