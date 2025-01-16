#1.Сравнение температур:
#Напишите метод is_warmer_than, который принимает два аргумента: две температуры.
#Метод должен возвращать True, если первая температура выше второй.
#Иначе метод должен возвращать False.

def is_warmer_than(temperature_01, temperature_02):

    return temperature_01 > temperature_01

#2.Проверка порядка строк:
#Напишите метод is_substring_first, который принимает две строки.
#Метод должен возвращать True, если первая строка находится раньше второй в алфавитном порядке.
#Иначе метод должен возвращать False.

def is_substring_first(str1, str2):

    return str1 < str2

print(is_substring_first("house", "mouse"))

#3.Кратность числа:
#Напишите метод is_multiple_of, который принимает два числа.
#Метод должен возвращать True, если первое число кратно второму.
#Иначе метод должен возвращать False.

def is_multiple_of(number_1, number_2):

    if number_2 == 0:
        return False
    return number_1 % number_2 == 0

print(is_multiple_of(10,5))

#4.Сравнение длины строк:
#Напишите метод is_longer_than, который принимает две строки.
#Метод должен возвращать True, если первая строка длиннее второй.
#Иначе метод должен возвращать False.

def is_longer_than(str1, str2):

    if str1 < str2:
        return False
    return len(str1) > (str2)

#5.Строка содержит цифру:
#Напишите метод contains_digit, который принимает строку.
#Метод должен возвращать True, если строка содержит хотя бы одну цифру.
#Иначе метод должен возвращать False.

def contains_digit(str)


