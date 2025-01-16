# Задание 1: Преобразование регистра
text = "Python Programming IS Awesome!"
lowercase_text = text.lower()
uppercase_text = text.upper()
capitalized_text = text.capitalize()

print("Lowercase:", lowercase_text)
print("Uppercase:", uppercase_text)
print("Capitalized:", capitalized_text)


# Задание 2: Удаление лишних пробелов
text_with_spaces = "   Привет, Python!   "
trimmed_text = text_with_spaces.strip()
print("Trimmed text:", trimmed_text)


# Задание 3: Замена подстроки
text_java = "Я изучаю Java"
replaced_text = text_java.replace("Java", "Python")
print("Replaced text:", replaced_text)


# Задание 4: Разделение строки
fruits = "яблоко,банан,вишня"
fruit_list = fruits.split(",")
print("Fruit list:", fruit_list)


# Задание 5: Объединение строки
words = ["Привет", "мир", "Python"]
joined_text = " ".join(words)
print("Joined text:", joined_text)


# Задание 6: Комбинированное использование методов
text_combined = "  Hello, PYTHON WORLD!  "
cleaned_text = text_combined.strip().lower().replace("python", "Java")
print("Combined text:", cleaned_text)


# Задание 7: Работа со списком слов
text_words = "учеба, кодинг, отдых, прогулка"
words_list = text_words.split(", ")
capitalized_words = [word.capitalize() for word in words_list]
joined_words = ", ".join(capitalized_words)
print("Capitalized words:", joined_words)


# Задание 8: Частотный анализ
text_frequency = "Python Python Python Java Java C++"
words_frequency = text_frequency.split()
frequency_count = {word: words_frequency.count(word) for word in set(words_frequency)}
print("Frequency count:", frequency_count)