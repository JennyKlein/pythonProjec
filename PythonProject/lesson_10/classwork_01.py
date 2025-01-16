"""
Создать чат-бота, который поможет пользователю оформить заказ через пошаговый диалог.
Бот предложит основные блюда, салаты, десерты и напитки, даст возможность добавлять "экстра" опции
и предложит дополнительные товары для увеличения чека. Все цены указаны в евро.

Экстра для основного блюда:
Пицца:
"Хотите добавить экстра: 1) Сыр (+1.50€), 2) Бекон (+2.00€), 3) Острый соус (+1.00€)?"
Паста:
"Хотите добавить экстра: 1) Пармезан (+1.20€), 2) Грибы (+1.50€), 3) Трюфельное масло (+3.00€)?"
Стейк:
"Хотите добавить экстра: 1) Соус барбекю (+1.50€), 2) Гарнир (картофель/овощи, +2.50€), 3) Перечный соус ( +2.00€)?"

Бот:
Привет! Я помогу вам оформить заказ. Давайте начнем с выбора основного блюда.
Выберите основное блюдо:

Пицца
Паста
Стейк
"""
mainCourseCash = 0
mainCourseExtraCash = 0


def mainCourse (dish):
    if dish == "Пицца":
        mainCourseCash = 5
        extraDishFpizza(input("Можете выбрать добавку: Сыр (+1.50€), Бекон (+2.00€), Острый соус (+1.00€)? или Отказаться \n" ).capitalize())
        return print(f"Вы выбрали {dish}")
    elif dish == "Паста":
        mainCourseCash = 6
        extraDishFPasta(input("Хотите добавить экстра: 1) Пармезан (+1.20€), 2) Грибы (+1.50€), 3) Трюфельное масло (+3.00€)? \n ").capitalize())
        return print(f"Вы выбрали {dish}")
    elif dish == "Стейк":
        extraDishFStaike(input("Хотите добавить экстра: 1) Соус барбекю (+1.50€), 2) Гарнир (картофель/овощи, +2.50€), 3) Перечный соус  ( +2.00€)? \n ").capitalize())
        mainCourseCash = 7
        return print(f"Вы выбрали {dish}")
    else:
        return print("Вы отказались от заказа основного блюда!")

def extraDishFpizza (extra):
    if extra == "Сыр":
        mainCourseExtraCash = 1.5
        return print(f"Вы выбрали Сыр, его цена: {mainCourseExtraCash}€")
    elif extra == "Бекон":
        mainCourseExtraCash = 1.6
        return print(f"Вы выбрали Бекон, его цена: {mainCourseExtraCash}€")
    elif extra == "Соус":
        mainCourseExtraCash = 1.7
        return print(f"Вы выбрали Соус, его цена: {mainCourseExtraCash}€")
    else:
        return print("Вы отказались от добавки")

def extraDishFPasta (extra):
    if extra == "Пармезан":
        mainCourseExtraCash = 1.8
        return print(f"Вы выбрали Пармезан, его цена: {mainCourseExtraCash}€")
    elif extra == "Грибы":
        mainCourseExtraCash = 1.9
        return print(f"Вы выбрали Грибы, его цена: {mainCourseExtraCash}€")
    elif extra == "Трюфельное масло":
        mainCourseExtraCash = 2
        return print(f"Вы выбрали Трюфельное масло, его цена: {mainCourseExtraCash}€")
    else:
        return print("Вы отказались от добавки")

def extraDishFStaike (extra):
    if extra == "Соус барбекю":
        mainCourseExtraCash = 2.1
        return print(f"Вы выбрали Соус барбекю, его цена: {mainCourseExtraCash}€")
    elif extra == "Гарнир":
        mainCourseExtraCash = 2.2
        return print(f"Вы выбрали Гарнир, его цена: {mainCourseExtraCash}€")
    elif extra == "Перечный соус":
        mainCourseExtraCash = 2.3
        return print(f"Вы выбрали Перечный соус, его цена: {mainCourseExtraCash}€")
    else:
        return print("Вы отказались от добавки")

print("Привет! Я помогу вам оформить заказ. Давайте начнем с выбора основного блюда. ")

mainCourse(input("Выберите основное блюдо: Пицца / Паста / Стейк: или Отказаться\n ").capitalize())


