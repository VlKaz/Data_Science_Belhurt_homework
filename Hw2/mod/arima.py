import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

def arima(filedata):
    # Загрузка данных
    data = pd.read_csv(filedata)
    series = data['close']
    # Разделение на обучающую и тестовую
    train = series[:-30]
    test = series[-30:]
    # Определение модели ARIMA
    model = ARIMA(train, order=(5, 1, 0))
    model_fit = model.fit()
    
    # Прогнозирование
    forecast = model_fit.forecast(steps=30)
    return test, forecast