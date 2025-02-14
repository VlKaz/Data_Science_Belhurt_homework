import pandas as pd


def clean_data(filedata):
    # Загрузка данных
    data = pd.read_csv(filedata)

    # Удаление столбца "Объем"
    data = data.drop(columns=['Объём'])
    
    # Удаление кавычек из всех строковых значений в DataFrame
    for column in data.columns:
        data[column] = data[column].apply(lambda x: x.replace('"', '') if isinstance(x, str) else x)
    
    # Преобразование числовых строк в числовые значения
    numeric_columns = ['Цена', 'Откр.', 'Макс.', 'Мин.']
    for column in numeric_columns:
        data[column] = data[column].str.replace('.', '').str.replace(',', '.').str.replace('K', '000').astype(float, errors='ignore')
    
    # Преобразование столбца с датами в числовой формат
    data['Дата'] = pd.to_datetime(data['Дата'], format='%d.%m.%Y').map(pd.Timestamp.timestamp)
    
    # Преобразование столбца 'Изм. %' в числовой формат
    data['Изм. %'] = data['Изм. %'].str.replace('%', '').str.replace(',', '.').astype(float) / 100

    data['Цена_завтра'] = data['Цена'].shift(-1)    
    data = data.dropna()
    return data


