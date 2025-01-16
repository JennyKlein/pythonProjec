name = "World"
greeting = "Hello, " + name + "! "
print(greeting * 3)  # Вывод Hello, World!


word = "Python" #['P', 'y', 't', 'h', 'o', 'n']
                # [ 0,   1,   2,   3,   4,   5 ]

print(word[5])
print(word[5])


startIndex = 4
endtIndex = 6


file = "code.py"
print(file[startIndex:endtIndex]) # подобная конструкция называется "срез" или подстрока.
# Что это такое? Это часть строки начиная с символа, находящегося под индексом startIndex
# и заканчивая индексом endIndex, но не включая символ под индексом endIndex


# поэтому, если мы хотим увидеть строку, начиная от какого-то индекса, до конца, то мы можем использовать следующее:
print(file[startIndex:])



path = "/lesson_03/code/teachers_code_1.py"
path_len = len(path)

print(path_len)