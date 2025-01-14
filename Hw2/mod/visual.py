import matplotlib.pyplot as plt

def visual(y_test, y_pred):
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(y_test)), y_test, label='Истинные значения', marker='o')
    plt.plot(range(len(y_pred)), y_pred, label='Предсказанные значения', marker='x')
    plt.xlabel('Наблюдения')
    plt.ylabel('Значения')
    plt.title('Сравнение истинных и предсказанных значений')
    plt.legend()
    plt.grid(True)
    plt.show()