print("Привет! Придумайте пожалуйста пароль для нашего сервиса:\n")

password = input()

while len(password.strip()) < 10:
    print(f"Длина пароля не достаточна. Ваш пароль {password.strip()} содержит только {len(password.strip())} символов. \n "
          f"Если вы хотите закончить работу, то введите 0\n"
          f"Введите новый пароль:\n")
    password = input()
    if password == "0":
        print("Так как вы ввели 0, пароль не был установлен")
        break