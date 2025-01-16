# "python" используя срезы - создать две отдельгные переменные, первая будет хранить только первый символ,
# вторая переменная - остаток строки. После этого, следует перевести первую переменную в верхний регистр,
# а вторую - в нижний и склеить обратно, так, чтобы получилось "Python"

text = "programming"
part_one = text[0]  # part_one = text[0:1] oder part_one = text[:1]
part_two = text[1:]

part_one = part_one.upper()

result = part_one + part_two

print(result)


#python".capitalize() -> "Python" - große BUchstaben
