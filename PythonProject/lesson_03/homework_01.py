# 1.Напишите программу, которая принимает имя и фамилию пользователя,
# объединяет их в полное имя и выводит полное имя заглавными буквами.

first_name = "Jenny"
last_name = "Klein"

name = first_name +" "+ last_name
name = name.upper()
print("Полное имя: " + name)


#2.Индексация, срезы и длина строк:
#Создайте программу, которая хранит строку
# "Программирование на Python — это весело!".
# Найдите и выведите:

text = "Python — это весело!"

print(text[:10]) # Первые 10 символов строки.
print(text[-5:]) # Последние 5 символов строки.
print(len(text)) # Общую длину строки.

#3.Методы работы со строками:
#Напишите программу, которая:
#Принимает на вход предложение (например, " Программировать — это круто! ").

text = " Программировать — это круто! "
text = text.strip() # Убирает лишние пробелы в начале и конце.
text = text.replace("круто", "здорово") # Заменяет слово "круто" на "здорово".
text = text.upper()#Выводит изменённое предложение в верхнем регистре.

print(text)


#4.тарый стиль форматирования:
#Напишите программу, которая сохраняет ваше имя, возраст и любимое число в переменных и форматирует предложение с помощью старого стиля % так, чтобы получилось:
#"Меня зовут [Имя], мне [Возраст] лет, а моё любимое число — [Число]."

name = "Jenny"
age = 38
number = 5.55

print("Меня зовут %s, мне %d лет, моё любимое число %.2f" % (name, age, number))

#5.Напишите программу, которая сохраняет цену $1 $123.456789 в переменной и выводит её:
#Округлённой до 2 знаков после запятой.
#В двоичной, восьмеричной и шестнадцатеричной системах счисления.

price = 123.456789

print("Полная цена: %f " %(price) + "$")
print("Округлённая цена: %.2f " % price + "$")

decimal_price = 123

binary_price = bin(decimal_price) # Преобразование в двоичную систему
octal_price = oct(decimal_price) # Преобразование в восьмеричную систему
hexadecimal_price = hex(decimal_price) # Преобразование в шестнадцатеричную систему

print("Двоичное представление: ", binary_price)
print("Восьмеричное представление: ", octal_price)
print("Шестнадцатеричное представление: ", hexadecimal_price)