"""
пользователь вводит числа в консоль, если сумма нечетных чисел больше 100, то останвливаемся
если четное, то coninue,
если не четное, то просто суммируем его со всеми остальными

"""

sum = 0
num = int(input("enter your number:"))

while True:

    if num % 2 == 0:
        print("введено четное число, пропускаем суммирование")
        num = int(input("enter your number:"))
        continue

    sum = sum + num

    if sum > 100:
        print("сумма больше 100б останавливаем работу цикла")
        break

    num = int(input("enter your number:"))

print(sum)