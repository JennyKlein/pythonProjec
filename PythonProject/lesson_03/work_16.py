# Задание 1: Представление профиля пользователя
username = "Алиса"
points = 145
profile_message = "Пользователь %s заработал %d баллов." % (username, points)
print(profile_message)


# Задание 2: Подстановка данных о продукте
product = "ноутбук"
price = 799.99
product_message = "Продукт: %s, Цена: %.2f$." % (product, price)
print(product_message)


# Задание 3: Вывод температуры
temperature = 36.678
temperature_message = "Текущая температура: %.2f градусов." % round(temperature, 2)
print(temperature_message)


# Задание 4: Расписание дня
task1 = "встреча"
time1 = 10
task2 = "обед"
time2 = 13
schedule_message = "%02d:00 - %s, %02d:00 - %s." % (time1, task1, time2, task2)
print(schedule_message)


# Задание 5: Выравнивание полей в таблице
item1 = "Яблоки"
count1 = 5
price1 = 1.50
item2 = "Бананы"
count2 = 12
price2 = 0.80
table_header = "Товар      Кол-во    Цена"
table_row1 = "%-10s %5d %8.2f" % (item1, count1, price1)
table_row2 = "%-10s %5d %8.2f" % (item2, count2, price2)
print(table_header)
print(table_row1)
print(table_row2)


# Задание 6: Разделы книги
chapter1 = "Введение"
pages1 = 12
chapter2 = "Основы"
pages2 = 45
book_sections = "1. %s (%d стр.)\n2. %s (%d стр.)" % (chapter1, pages1, chapter2, pages2)
print(book_sections)


# Задание 7: Работа с курсами валют
currency = "доллар"
rate = 0.92367
currency_message = "Текущий курс %s: %.2f EUR." % (currency, round(rate, 2))
print(currency_message)


# Задание 8: Ошибка при формате
age = "двадцать пять"
try:
    age_message = "Возраст: %d лет." % age
except TypeError as e:
    print("Ошибка:", e)


# Задание 9: Комбинация разных типов
user = "Максим"
score = 92.456
level = 5
combined_message = "Игрок %s, уровень: %d, очки: %.2f." % (user, level, round(score, 2))
print(combined_message)