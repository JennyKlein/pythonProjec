# Примеры применения полезных методов для работы со строками

# .lower() — Преобразует строку в нижний регистр
text = "PYTHON IS GREAT"
lower_case_text = text.lower()
print(lower_case_text)  # Вывод: python is great

# Python != python

# чтобы привести всю строку к нижнему регистру,
# можно воспользоваться встроенной функцией str.lower()

print('"Python".lower() = ' + "Python".lower())

# применяя функцию lower(), также, как и любую другую,
# мы не изменяем исходную строку, а создаем новую с новым значением
text = "Some text"
text.lower()
print("text = " + text)

# чтобы все же присвоить переменной новое значение,
# можно переопределить его или создать новую переменную
lowerCaseText = text.lower()
print("lowerCaseText = " + lowerCaseText)

# переопределение:
text = text.lower()
print("text = " + text)

nonCharStr = "123132)_)__-!@#$%^&*&^%"

print("nonCharStr = " + nonCharStr)
print(nonCharStr)
nonCharStr = "123132)_)__-!@#$%^&*&^%"

print("nonCharStr = " + nonCharStr)
print('nonCharStr.lower() = ' + nonCharStr.lower())
# переопределение:
text = text.lower()
print("text = " + text)


text = text.upper()
print('text.upper() = ' + text.upper())