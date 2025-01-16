
# Задание 6: Комбинированное использование методов
"""
Создайте строку с текстом "  Hello, PYTHON WORLD!  ".
- Удалите пробелы в начале и конце строки.
- Преобразуйте строку в нижний регистр.
- Замените слово "python" на "Java".
"""
# Ваш код здесь

str4 = "  Hello, PYTHON WORLD!  "
str4 = str4.strip()
print(str4)

str4 = str4.lower()
print(str4)

str4 = str4.replace("python", "Java")

print(str4)


str5 = "  Hello, PYTHON WORLD!  "
str5 = str5.strip().lower().replace("python", "Java")
print(str5)