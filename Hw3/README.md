# Automobile Data Analysis Project

## Описание проекта

Этот проект предназначен для анализа данных об автомобилях, содержащихся в файле CSV, и их переноса в базу данных SQLite. Проект включает в себя создание таблиц, выполнение различных вычислений и построение графиков с использованием библиотеки `seaborn`.

## Структура проекта

- `data/automobile.csv`: Исходный файл CSV с данными об автомобилях.
- `data/auto.db`: База данных SQLite, содержащая таблицу с данными об автомобилях.
- `main.ipynb`: Основной Jupyter Notebook, содержащий код для выполнения всех операций.
- `mod/create_table.py`: Модуль для переноса данных в SQLite из CSV файла.
- `mod/clear_table.py`: Модуль для удаления строк с определенными значениями из базы данных.
- `mod/calculations.py`: Модуль для выполнения вычислений.
- `mod/visual.py`: Модуль для построения графиков на основе данных из базы данных.