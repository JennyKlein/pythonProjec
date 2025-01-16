"""Самостоятельная работа.Даны два списка строк – ["A", "B", "C", "D", "E"]
и["D", "E", "F", "G"].Напишите функцию, которая возвращает
третий список, содержащий все элементы обоих списков.Ожидаемый
результат - ["A", "B", "C", "D", "E", "D", "E", "F", "G"]."""

def bring_together_lists(list1, list2):
    return list1 + list2

list1 = ["A", "B", "C", "D", "E"]
list2 = ["D", "E", "F", "G"]
result = bring_together_lists(list1, list2)

print(result)


"""Создайте список, который содержит несколько названий фруктов. Выведите
его на экран так, чтобы каждое название выводилось с новой строки."""

fruits = ["яблоко", "банан", "апельсин", "груша"]

for fruit in fruits:
    print(fruit)
    

"""Создайте список, который состоит из нескольких положительных целых чисел. 
Напишите программу, которая определяет и выводит на экран максимальное из чётных чисел списка."""

def max_even_numbers(numbers):

    even_numbers = [num for num in numbers if num % 2 == 0]
    if even_numbers:
        return max(even_numbers)
    else:
        return None

numbers = [5, 10, 6, 2, 1, 6]
result = max_even_numbers(numbers)

print(result)
