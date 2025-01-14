from sklearn.metrics import mean_squared_error, r2_score

def mser2(y_test, y_pred):
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse,r2
    