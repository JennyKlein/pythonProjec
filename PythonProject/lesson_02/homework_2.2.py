# Исходные данные
exchange_rate = 1.09  # Курс евро к доллару
cookie_price_per_kg = 3.25  # Цена килограмма печенья в долларах
waffle_price_per_kg = 4.40  # Цена килограмма вафель в долларах
euros_available = 10  # Сумма денег в евро

# Количество для покупки
cookies_to_buy_kg = 0.5  # Полкилограмма печенья
waffles_to_buy_kg = 1.5  # Полтора килограмма вафель

# Расчет общей стоимости в долларах
total_cost_dollars = (cookie_price_per_kg * cookies_to_buy_kg) + (waffle_price_per_kg * waffles_to_buy_kg)

# Конвертация доступных евро в доллары
available_dollars = euros_available * exchange_rate

# Расчет оставшихся денег в долларах после покупки
remaining_dollars = available_dollars - total_cost_dollars

# Конвертация оставшихся долларов обратно в евро
remaining_euros = remaining_dollars / exchange_rate

# Вывод оставшейся суммы в евро
print(f'Остаток денег в евро: {remaining_euros:.2f} евро.')