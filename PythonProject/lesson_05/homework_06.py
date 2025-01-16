#2. Приветствие с титулом
#Напишите метод greet_with_title, который принимает титул (например, "доктор") и имя.
#Метод должен вернуть строку: "Привет, [Титул] [Имя]!".

def greet_with_title(title, name):
    return f"Привет, {title} {name}!"

input_title = input("Введите титул (например, 'доктор'): ")
input_name = input("Введите ваше имя: ")

greeting = greet_with_title(input_title, input_name)
print(greeting)