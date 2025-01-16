# Задание 1: Преобразование регистра
"""
Создайте строку с текстом "Python Programming IS Awesome!".
Выполните следующие операции:
- Преобразуйте строку в нижний регистр.
- Преобразуйте строку в верхний регистр.
- Сделайте первую букву строки заглавной.
"""
# Ваш код здесь

text = "Python Programming IS Awesome!"

text = text.lower()
print(text)

text = text.upper()
print(text)

text = "Python Programming IS Awesome!"
part_one = text[0]  # part_one = text[0:1] oder part_one = text[:1]
part_two = text[1:]

part_one = part_one.upper()

result = part_one + part_two

print(result)