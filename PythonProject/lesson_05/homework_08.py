#4. Персональное сообщение о книге
#Напишите метод favorite_book, который принимает имя пользователя и название его любимой книги.
#Метод должен вернуть строку в формате: "Привет, [Имя]! Твоя любимая книга — '[Название книги]'!"

def favorite_book(name, book_title):
    return f"Привет, {name}! Твоя любимая книга — '{book_title}'!"

name = input("Введите ваше имя: ")
book_title = input("Введите название вашей любимой книги: ")
message = favorite_book(name, book_title)
print(message)
