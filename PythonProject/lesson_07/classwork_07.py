Методы, которые выполняют действие, но ничего не возвращают

# Метод 1: Выводит приветствие
def say_hello():
    print("Привет, мир!")


# Метод 2: Печатает результат сложения двух чисел
def print_sum(a, b):
    print(f"Сумма чисел {a} и {b} равна {a + b}")


# Методы, которые возвращают значение

# Метод 3: Возвращает сумму двух чисел
def add_numbers(a, b):
    return a + b


# Метод 4: Возвращает строку с приветствием
def get_greeting(name):
    return f"Привет, {name}!"


# Метод 5: Возвращает длину строки
def get_length(message):
    return len(message)


# Демонстрация использования методов
# Методы без возвращаемого значения
say_hello()  # Привет, мир!
print_sum(3, 5)  # Сумма чисел 3 и 5 равна 8

# Методы с возвращаемым значением
result = add_numbers(4, 6)
print(f"Результат сложения: {result}")  # Результат сложения: 10

greeting = get_greeting("Ильяс")
print(greeting)  # Привет, Ильяс!

message_length = get_length("Python")
print(f"Длина строки 'Python': {message_length}")  # Длина строки 'Python': 6