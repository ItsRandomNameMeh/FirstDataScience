import sqlite3

import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import pandas as pd

payment_amount = [] #сумма какого-то платежа
zip_address = [] #адрес где мы сдавали DVD в аренду
month_custom = [] #День+Месяц когда был осуществлен платеж
film_cost = [] #стоимость текущего фильма

conn = sqlite3.connect('FirstLab.db')
print("Подключение к базе данных установлено");
counter = 0

cursor = conn.cursor()
cursor.execute("SELECT * FROM film;")
payment_rows = cursor.fetchall() # Извлекаем все строки результата запроса
# Выполнение запроса PRAGMA для получения информации о структуре таблицы
cursor.execute("PRAGMA table_info(film)")
# Получение результатов запроса
payment_columns_info = cursor.fetchall()
# Извлечение имен столбцов из таблицы
payment_columns = [info[1] for info in payment_columns_info]
print(payment_columns)
for row in payment_rows:
    if (row[9] not in film_cost):
        film_cost.append(row[9])
        counter+=1
    if counter > 1000:
        break

counter = 0
cursor.execute("SELECT * FROM rental;")
payment_rows = cursor.fetchall() # Извлекаем все строки результата запроса
# Выполнение запроса PRAGMA для получения информации о структуре таблицы
cursor.execute("PRAGMA table_info(rental)")
# Получение результатов запроса
payment_columns_info = cursor.fetchall()
# Извлечение имен столбцов из таблицы
payment_columns = [info[1] for info in payment_columns_info]
print(payment_columns)
for row in payment_rows:
    try:
        date_obj = datetime.strptime(row[4], '%Y-%m-%d %H:%M:%S.%f')
    except:
        continue
    # Извлекаем дату
    # day = date_obj.day
    # month = date_obj.month
    data = str(date_obj.date())
    month_custom.append(data)
    counter+=1
    if counter > 1000:
        break

counter = 0
cursor.execute("SELECT * FROM payment;")
payment_rows = cursor.fetchall()  # Извлекаем все строки результата запроса
# Выполнение запроса PRAGMA для получения информации о структуре таблицы
cursor.execute("PRAGMA table_info(payment)")
# Получение результатов запроса
payment_columns_info = cursor.fetchall()
# Извлечение имен столбцов из таблицы
payment_columns = [info[1] for info in payment_columns_info]
print(payment_columns)
for row in payment_rows:
    print(row)
    payment_amount.append(row[4])
    counter+=1
    if counter > 1000:
        break


counter = 0
cursor.execute("SELECT * FROM address;")
payment_rows = cursor.fetchall() # Извлекаем все строки результата запроса
# Выполнение запроса PRAGMA для получения информации о структуре таблицы
cursor.execute("PRAGMA table_info(address)")
# Получение результатов запроса
payment_columns_info = cursor.fetchall()
# Извлечение имен столбцов из таблицы
payment_columns = [info[1] for info in payment_columns_info]
print(payment_columns)
for row in payment_rows:
    if (row[5] != ' ' and row[5] not in zip_address):
        counter+=1
        zip_address.append(row[5])
        print(row)
    if counter > 1000:
        break

mini = min(len(film_cost),len(zip_address), len(month_custom), len(payment_amount))



# Устанавливаем заголовок и метки осей
plt.title('Завивисиомсть стоимости билеты и места показа фильма')
plt.ylabel('стоимость билета')
plt.xlabel('район (zip-code)')
# mini = min(len(film_cost),len(zip_address))
#
# Создаем график рассеяния
sns.lineplot(y=film_cost[:mini], x=zip_address[:mini])

# Устанавливаем заголовок и метки осей
plt.title('Завивисиомсть стоимости билеты и места показа фильма')
plt.ylabel('стоимость билета')
plt.xlabel('район (zip-code)')

# Отображаем график
# plt.show()
mini = min(len(payment_amount),len(month_custom))

# Создаем график рассеяния
sns.lineplot(x=payment_amount[:mini], y=month_custom[:mini])

# Устанавливаем заголовок и метки осей
plt.title('Даты платежей, zip-коды и стоимости проката фильма')
plt.ylabel('стоимость 1 фильма и дата')
plt.xlabel('zip и сумма трат')
#
# # Отображаем график
# plt.show()
#
# mini = min(len(zip_address),len(month_custom))
#
# # Создаем график рассеяния
# sns.lineplot(y=zip_address[:mini], x=month_custom[:mini])
#
# # Устанавливаем заголовок и метки осей
# plt.title('Связь где и в какое время брали в прокат фильмы в целом')
# plt.ylabel('место аренды')
# plt.xlabel('дата')
#
# Отображаем график
plt.show()