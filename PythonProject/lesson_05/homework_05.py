#1. Калькулятор периметра квадрата
#Напишите метод calculate_perimeter, который принимает длину стороны квадрата в качестве аргумента.
#Метод должен рассчитать и вернуть периметр квадрата.
#Формула: Периметр = 4 * длина стороны.

def calculate_perimeter(side_length):
    return 4 * side_length

side_length = float(input("Введите длину стороны квадрата: "))
perimeter = calculate_perimeter(side_length)

print(f"Периметр квадрата: {perimeter}")
