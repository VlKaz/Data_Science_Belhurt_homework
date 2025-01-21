import sqlite3
from mod import (create_table, clear_table, calculations, visual)

def main():
    # Создание SQLite
    filedata = 'data/automobile.csv'
    filedb = 'data/auto.db'
    create_table(filedata,filedb)
    # Удоляем строки если в колонке лошадиные силы есть "?"(это надо чтобы позже построить график)
    clear_table(filedb)
    # Занимаемся подсчетами всякого разного формируя запросы к SQLite
    calculations(filedb)
    # Выводим графики 
    visual(filedb)
        
if __name__ == "__main__":
    main()