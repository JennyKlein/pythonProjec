#1.Калькулятор площади круга:
#Напишите метод calculate_circle_area, который принимает радиус круга в качестве аргумента.
#Метод должен рассчитать и вернуть площадь круга.
#Формула: Площадь = π * радиус^2 (используйте 3.14 вместо π).

def calculate_circle_area(radius):

    pi = 3.14
    area = pi * (radius ** 2)
    return area

#2.Объединение имени и фамилии:
#Напишите метод concat_names, который принимает имя и фамилию в качестве аргументов.
#Метод должен вернуть строку в формате: "Имя Фамилия".

def concat_names(first_name, last_name):

    return f"{first_name} {last_name}"


#3.Форматирование сообщения:
#Напишите метод format_message, который принимает имя пользователя и сообщение в качестве аргументов.
#Метод должен вернуть строку в формате: "[Имя пользователя]: [Сообщение]".

def format_message(name, message):

    return f"[{name}]: {message}"

#4.Дублирование слова:
#Напишите метод duplicate_word, который принимает слово и число в качестве аргументов.
#Метод должен вернуть строку, где слово повторяется указанное количество раз без пробелов.
#Пример: Для "Привет" и 3 метод должен вернуть "ПриветПриветПривет".

def duplicate_word(word, count):

    return word * count

result = duplicate_word("Привет", 3)
print(result)
