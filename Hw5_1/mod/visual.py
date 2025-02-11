import matplotlib.pyplot as plt
import numpy as np

def visual(y_test, y_pred):
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(y_test)), y_test, label='Фактические значения', marker='o')
    plt.plot(range(len(y_pred)), y_pred, label='Предсказанные значения', marker='x')
    plt.xlabel('Наблюдения')
    plt.ylabel('Значения')
    plt.title('Сравнение истинных и предсказанных значений')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Визуализация предсказанных и фактических значений
    plt.figure(figsize=(20, 10))
    plt.scatter(range(len(y_test)), y_test, color='blue', label='Фактические значения')
    plt.scatter(range(len(y_test)), y_pred, color='red', label='Предсказанные значения')
    plt.xlabel('Наблюдение')
    plt.ylabel('Значение')
    plt.title('Фактические и предсказанные значения')
    plt.legend()
    plt.show()
