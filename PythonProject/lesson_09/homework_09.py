#1.Диапазон температуры:
#Напишите метод is_in_temperature_range, который принимает температуру и два предела (min и max) в качестве аргументов.
#Метод должен возвращать True, если температура находится в диапазоне [min, max].
#Иначе метод должен возвращать False.

def is_in_temperature_range(temp, temp_min,temp_max):
    return temp_min <= temp <= temp_max
print(is_in_temperature_range(27, 5, 35))
print(is_in_temperature_range(5, 10, 15))

#2.Алфавитное сравнение:
#Напишите метод compare_alphabetical_order, который принимает два слова.
#Метод должен возвращать "Первое", если первое слово идёт раньше в алфавите,
#"Второе", если второе идёт раньше, или "Равно", если слова одинаковые.

def compare_alphabetical_order(word1, word2):

    if word1 < word2:
        return "Первое"
    elif word1 > word2:
        return "Второе"
    else:
        return "Равно"

#3.Проверка чётности и положительности:
#Напишите метод is_even_and_positive, который принимает число.
#Метод должен возвращать True, если число чётное и положительное.
#Иначе метод должен возвращать False.

def is_even_and_positive(number):

    return number > 0 and number % 2 == 0

#4.Проверка возрастной группы:
#Напишите метод get_age_group, который принимает возраст.
#Метод должен возвращать:

#"Младенец", если возраст меньше 3.
#"Ребёнок", если возраст от 3 до 12.
#"Подросток", если возраст от 13 до 19.
#"Взрослый", если возраст 20 и старше.

def get_age_group(age):

    if age < 3:
        return "Младенец"

    elif 3 <= age <= 12:
        return "Ребёнок"

    elif 13 <= age <= 19:
        return "Подросток"

    else:
        return "Взрослый"

#5.Проверка надёжности пароля:
#Напишите метод is_strong_password, который принимает строку пароля.
#Метод должен возвращать True, если пароль содержит не менее 8 символов и включает как буквы, так и цифры.
#Иначе метод должен возвращать False.

def is_strong_password(password):
    return len(password) >= 8

#6.Определение сезона:
#Напишите метод get_season, который принимает номер месяца (1 для января, 12 для декабря).
#Метод должен возвращать сезон ("Зима", "Весна", "Лето", "Осень") в зависимости от месяца.

def get_season(month):

    if month == 12 or month == 1 or month == 2:
        return "Зима"
    elif month == 3 or month == 4 or month == 5:
        return "Весна"
    elif month == 6 or month == 7 or month == 8:
        return "Лето"
    elif month == 9 or month == 10 or month == 11:
        return "Осень"
    else:
        return "Некорректный месяц"


#7.Проверка длины строки:
#Напишите метод is_valid_length, который принимает строку и максимальную длину.
#Метод должен возвращать True, если длина строки меньше или равна максимальной длине.
#Иначе метод должен возвращать False.

def is_valid_length(string, max_length):

    if len(string) <= max_length:
        return True
    else:
        return False

#8.Тип треугольника:
#Напишите метод get_triangle_type, который принимает три стороны треугольника.
#Метод должен возвращать:

#"Равносторонний", если все стороны равны.
#"Равнобедренный", если две стороны равны.
#"Разносторонний", если все стороны разные.

def get_triangle_type(a, b, c):

    if a == b == c:
        return "Равносторонний"
    elif a == b or b == c or a == c:
        return "Равнобедренный"
    else:
        return "Разносторонний"